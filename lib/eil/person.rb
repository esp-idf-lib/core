class EIL
  # A class to represents people contributed to the project
  class Person

    attr_reader :name, :person

    PERSONS_YML = EIL.root / "persons.yml"

    def initialize(name)
      @name = name
      @person = self.class.yaml.select { |p| p["name"] == name }.first
      raise StandardError, "cannot find #{name} in #{PERSONS_YML}" unless @person
    end

    def full_name
      person["full_name"]
    end

    def gh_id

      person["gh_id"]
    end

    def email
      person["email"]
    end

    def url
      person["url"]
    end

    def contributed_components
      Component.all.select { |c| c.contributed_by? name }
    end

    def self.yaml
      YAML.safe_load(File.read(PERSONS_YML))
    end

    def self.all
      yaml.map { |n| new n["name"] }
    end
  end
end
