require "spec_helper"

RSpec.describe EIL::Groups do
  describe ".all" do
    it "returns Array of all groups" do
      expect(described_class.all).to be_a(Array)
    end

    it "has name" do
      expect(described_class.all).to all(have_key "name")
    end

    it "has description" do
      expect(described_class.all).to all(have_key "description")
    end
  end
end
