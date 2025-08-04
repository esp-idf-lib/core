require "erb"
require "redcarpet"

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
  # If the person has full name, use it. Otherwise use name.
  name = person.full_name || person.name

  # Link the name to one of available URLs.
  name_url = person.gh_id ? "https://github.com/#{person.gh_id}" : person.url
  name_url ? "[#{name}](#{name_url})" : name
end

# Create a string of all the components `person` has contributed to.
def person_contribution(person)
  person.contributed_components.map { |c| "`#{c.name}`" }.join(" ")
end

def erb(template_file)
  ERB.new(File.read(template_file), trim_mode: "<>")
end

namespace :docs do
  desc "Generate status page"
  task :status do
    puts erb("STATUS.md.erb").result
  end

  # Generate Markdown from `README.md.erb`.
  #
  # ```sh
  # bundle exec rake docss:readme
  # ```
  desc "Generate README.md"
  task :readme do
    puts erb("README.md.erb").result
  end

  namespace :readme do

    # Generate HTML from `README.md.erb`.
    #
    # ```sh
    # bundle exec rake docs:readme:html
    # ```
    desc "Generate README.html"
    task :html do
      renderer = Redcarpet::Render::HTML.new(prettify: true)
      markdown = Redcarpet::Markdown.new(renderer, fenced_code_blocks: true, tables: true)
      puts markdown.render(erb("README.md.erb").result)
    end
  end
end
