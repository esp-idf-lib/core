require "spec_helper"

RSpec.describe "persons.yml" do
  let(:file) { Pathname.new "persons.yml" }
  let(:doc) { YAML.safe_load(File.read(file)) }
  let(:known_attr) { ["name", "gh_id", "email", "url", "full_name" ].sort }

  it "exists" do
    expect(file).to exist
  end

  it "has Array of person" do
    expect(doc).to be_a Array
  end

  it "has records with name" do
    expect(doc).to all(have_key "name")
  end

  it "has no duplicated names" do
    all = doc.map { |p| p["name"] }
    uniq = all.uniq
    expect(all).to eq uniq
  end

  it "has valid records with known attributes" do
    expect(known_attr).to eq(doc.map { |r| r.keys }.flatten.uniq.sort)
  end
end
