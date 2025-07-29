require "shellwords"

# Increment the version number of a component. Whnen `part` is `major` and the
# current version is `1.2.3`, it returns `2.0.0`.
#
# @param component [EIL::Component] The component
# @param part [String] the part of version string to increment. One of `major`,
# `minor`, and `patch`.
def increment_version(component, part)
  major, minor, patch = component.version.split(".")
  case part.to_sym
  when :major
    [major.to_i + 1, 0, 0].join(".")
  when :minor
    [major, minor.to_i + 1, 0].join(".")
  when :patch
    [major, minor, patch.to_i + 1].join(".")
  end
end

# Update `file` with `new_version`.
#
# @param file [String] File to update
# @param new_version [String] New version string
def update_version(file, new_version)
  new_content = ""
  File.readlines(file).each do |line|
    new_content += /^version:/.match(line) ? "version: #{new_version}\n" : line
  end

  File.write(file, new_content)
end

# Changes the working directoty into dir. The given block is executed in the
# directoty.
#
# @param dir [String] The directory to change into. When block is given, the
# block is executed in the directory.
def enter_into(dir)
  Dir.chdir dir do
    puts "in #{dir}"
    yield
  end
end

# Create and checkout new branch.
#
# @param branch_name [String] The branch name to check out.
def checkout_release_branch(branch_name)
  sh "git checkout -b #{branch_name.shellescape}" do |ok, _res|
    raise StandardError, "failed to create #{branch_name}" unless ok
  end
end

# Update .eil.yml and idf_component.yml with new version. Shows diff after the
# modification.
#
# @param new_version [String] New version string
def increment_version_of_files(new_version)
  update_version(".eil.yml", new_version)
  update_version("idf_component.yml", new_version)
  sh "git diff"
  sh "git status"
end

# Commit everything with a commit message, "Release #{version}"
#
# @param version [String] The version string.
def commit_all(version)
  commit_message = "Release #{version}"
  sh "git add ."
  sh "git commit -m #{commit_message.shellescape}" do |ok, _res|
    raise StandardError, "failed to commit" unless ok
  end
end

# Push everything to origin from the current branch.
#
# @param branch_name [String] The branch name to push
def push_all(branch_name)
  sh "git push --set-upstream origin #{branch_name.shellescape}" do |ok, _res|
    raise StandardError, "failed to git push" unless ok
  end
end

# Revert all the changes in the branch and remove the branch.
#
# @param branch_name [String] The branch name
def revert(branch_name)
  sh "git reset ."
  sh "git checkout ."
  sh "git checkout main"
  sh "git branch -D #{branch_name.shellescape}" do |ok, _res|
    raise StandardError, "failed to delete branch #{branch_name}" unless ok
  end
end

desc "Release component `name`. `part` is one of `major`, `minor`, and `patch`"
task :release, [:name, :part] do |_t, args|
  component = EIL::Component.new(args[:name])
  new_version = increment_version(component, args[:part])
  branch_name = "release/#{new_version}"
  enter_into component.path do
    checkout_release_branch(branch_name)
    increment_version_of_files(new_version)
    commit_all(new_version)
    push_all(branch_name)
  rescue StandardError => e
    revert(branch_name)
    raise e
  end
end
