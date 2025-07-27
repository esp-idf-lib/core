require "yaml"

class EIL
  class Groups
    def self.all
      YAML.safe_load(File.read(EIL.root / "groups.yml"))
    end
  end
end
