namespace :component do
  desc "Update component to main branch"
  task :update, [:name] do |_t, args|
    component = EIL::Component.new(args[:name])
    enter_into component.path do
      sh "git checkout main"
      sh "git pull"
    end
    enter_into component.path / "common"  do
      sh "git checkout main"
      sh "git pull"
    end
  end

  desc "Update all components to main branch"
  task :update_all do
    EIL::Component.all.each do |component|
      pp component.name
      Rake::Task["component:update"].execute(name: component.name)
    end
  end

  desc "Run sh file in each component directory"
  task :each, [:file] do |_t, args|
    file = Pathname.new(args[:file]).realpath
    EIL::Component.all.each do |component|
      ENV["NAME"] = component.name
      enter_into component.path do
        sh "sh #{file}"
      end
    end
  end
end
