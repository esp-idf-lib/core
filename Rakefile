# frozen_string_literal: true

require "rubocop/rake_task"
require "rspec/core/rake_task"
require "pry"

require "erb"
require "redcarpet"

$LOAD_PATH.unshift("lib")
require "eil/component"

RSpec::Core::RakeTask.new(:spec)
RuboCop::RakeTask.new

def components
  return @components if @components

  @components = File.readlines("components.txt").sort.map { |line| EIL::Component.new(line) }
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
