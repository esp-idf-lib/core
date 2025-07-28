# frozen_string_literal: true

require "rubocop/rake_task"
require "rspec/core/rake_task"
require "pry"

$LOAD_PATH.unshift("lib")
require "eil"

RSpec::Core::RakeTask.new(:spec)
RuboCop::RakeTask.new

# files under `rakelib` with .rake extension are automatically loaded.
# see `bundle exec rake -T` to see all the available tasks.
