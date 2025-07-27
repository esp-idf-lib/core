require "spec_helper"

RSpec.describe EIL::Component do
  let(:c) { EIL::Component.new }

  describe ".all" do
    it "returns array of components" do
      expect(described_class.all).to be_a(Array).and all(be_an described_class)
    end
  end
end
