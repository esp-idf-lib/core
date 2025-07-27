require_relative "eil/component"

require "pathname"

class EIL
  def self.root
    Pathname.new(__FILE__).parent.parent
  end
end
