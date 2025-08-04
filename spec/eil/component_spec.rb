require "spec_helper"

RSpec.describe EIL::Component do
  let(:c) { EIL::Component.all.first }

  describe ".all" do
    it "returns array of components" do
      expect(described_class.all).to be_a(Array).and all(be_an described_class)
    end
  end

  describe ".new" do
    context "when the component does not exist" do
      it "raises" do
        expect { described_class.new("foo") }.to raise_error ArgumentError
      end
    end

    context "when the component exists" do
      it "does not raise" do
        expect { described_class.new("esp_idf_lib_helpers") }.not_to raise_error
      end
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

  describe "#contributed_by?" do
    it "retruns true" do
      c = described_class.new("esp_idf_lib_helpers")
      expect(c.contributed_by? "trombik").to be true
    end
  end
end
