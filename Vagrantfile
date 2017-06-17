Vagrant.configure(2) do |config|

  config.vm.define "dev" do |dev|
    dev.vm.box = "elastic/centos-7-x86_64"

    dev.vm.provider :virtualbox do |prov|
      prov.customize ['modifyvm', :id,'--memory', '1024']
    end

    # allow port forwarding to hit webserver from host machine
    dev.vm.network "forwarded_port", guest: 8081, host: 8081, auto_correct: true

    dev.vm.provision :puppet do |puppet|
      puppet.environment_path = "puppet/environments"
      puppet.environment = "dev"
    end
  end

end