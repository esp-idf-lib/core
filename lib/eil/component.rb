# frozen_string_literal: true

require "open3"

class EIL
  # A class represents esp-idf-lib components
  class Component
    ORG = "esp-idf-lib"
    GITHUB_URL = "https://github.com"
    GITHUB_PAGES_URL = "https://esp-idf-lib.github.io"
    ESP_COMPONENT_REGISTRY_URL = "https://components.espressif.com"

    attr_reader :name, :path

    def initialize(name, path)
      @name = name.chomp
      @path = path
    end

    def org
      ORG
    end

    def fqdn
      "#{org}/#{name}"
    end

    def repo_url
      "#{GITHUB_URL}/#{fqdn}"
    end

    def esp_url
      "#{ESP_COMPONENT_REGISTRY_URL}/components/#{fqdn}"
    end

    def doc_url
      "#{GITHUB_PAGES_URL}/#{name}"
    end

    def issues_url
      "#{repo_url}/issues"
    end

    def badge_svg_url(workflow_file)
      "#{workflow_url(workflow_file)}/badge.svg"
    end

    def workflow_url(workflow_file)
      "#{repo_url}/actions/workflows/#{workflow_file}"
    end

    def badge(workflow_file)
      workflow_name = workflow_file.split(".").first
      "[![#{workflow_name}](#{badge_svg_url(workflow_file)})](#{workflow_url(workflow_file)})"
    end

    def self.all
      stdout, stderr, status = Open3.capture3("git submodule")
      raise StandardError, "failed to run `git submodule`: #{stderr}" if status != 0

      memo = []
      stdout.each_line(chomp: true) do |line|
        # 1d24b0da13e9c0aae9ad985e4348d2fe50263e3c components/tda74xx (1.0.3-2-g1d24b0d)
        component_path = line.split(" ")[1]
        next unless component_path.start_with? "components"

        memo << Component.new(component_path.split("/").last, component_path)
      end
      memo
    end
  end
end
