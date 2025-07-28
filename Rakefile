# frozen_string_literal: true

require "rspec/core/rake_task"
require "rake/clean"
begin
  require "rubocop/rake_task"
  require "pry"
rescue LoadError
  # ignore LoadError if gems for development are not available
end

$LOAD_PATH.unshift("lib")
require "eil"

RSpec::Core::RakeTask.new(:spec)
RuboCop::RakeTask.new

# Add build directory and sdkconfig under examples to files to clean.
CLEAN << FileList[
  "components/examples/**/build",
  "components/examples/**/sdkconfig",
  "components/examples/**/sdkconfig.old",
]

# files under `rakelib` with .rake extension are automatically loaded.
# see `bundle exec rake -T` to see all the available tasks.
