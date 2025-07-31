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

# Revert all the changes in the branch and remove the branch.
#
def revert
  sh "git reset ."
  sh "git checkout ."
  sh "git checkout main"
end

desc "Release component `name`. `part` is one of `major`, `minor`, and `patch`"
task :release, [:name, :part] do |_t, args|
  component = EIL::Component.new(args[:name])
  new_version = increment_version(component, args[:part])
  release_title = "Release #{new_version}"
  enter_into component.path do
    sh "git checkout main"
    increment_version_of_files(new_version)
    commit_all(new_version)
    sh "git push"
    sh "gh release create #{new_version.shellescape} --notes #{release_title.shellescape} --title #{release_title.shellescape}"
  rescue StandardError => e
    revert
    raise e
  end
end

desc "Release all components"
task :release_all, [:part] do |_t, args|
  EIL::Component.all.each do |component|
    pp component.name
    Rake::Task["release"].execute(name: component.name, part: args[:part])
  end
end
