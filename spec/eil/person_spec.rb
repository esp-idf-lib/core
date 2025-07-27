require "spec_helper"

RSpec.describe EIL::Person do
  describe ".new" do
    it "finds trombik" do
      expect(described_class.new "trombik").to be_a described_class
    end
  end
end
