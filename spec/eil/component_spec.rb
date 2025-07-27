require "spec_helper"

RSpec.describe EIL::Component do
  let(:c) { EIL::Component.all.first }

  describe ".all" do
    it "returns array of components" do
      expect(described_class.all).to be_a(Array).and all(be_an described_class)
    end
  end

  describe "#eil" do
    it "returns hashed YAML" do
      expect(c.eil).to be_a Hash
    end
  end

  describe "#groups" do
    it "returns Array of groups" do
      expect(c.groups).to be_a(Array).and all(be_an String)
    end
  end

  describe "#group_of?" do
    it "returns true" do
      expect(c.group_of? c.groups.first).to be true
    end
  end
end
