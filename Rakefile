# frozen_string_literal: true

require "rubocop/rake_task"
require "rspec/core/rake_task"
require "pry"

require "erb"
require "redcarpet"

$LOAD_PATH.unshift("lib")
require "eil"

RSpec::Core::RakeTask.new(:spec)
RuboCop::RakeTask.new

def components
  return @components if @components

  @components = EIL::Component.all
end

def groups
  EIL::Groups.all
end

def persons
  EIL::Person.all
end

def person_credit(person)
  name = person.full_name ? person.full_name : person.name
  name_url = person.gh_id ? "https://github.com/#{person.gh_id}" : person.url
  name_url ? "[#{name}](#{name_url})" : name
end

def person_contribution(person)
  person.contributed_components.map { |c| "`#{c.name}`" }.join(" ")
end

def erb
  template_file = "README.md.erb"
  ERB.new(File.read(template_file), trim_mode: "<>")
end

desc "Generate README.md"
task :readme do
  puts erb.result
end

desc "Generate README.html"
task :readme_html do
  renderer = Redcarpet::Render::HTML.new(prettify: true)
  markdown = Redcarpet::Markdown.new(renderer, fenced_code_blocks: true, tables: true)
  puts markdown.render(erb.result)
end
