box      = 'precise64'
url      = 'http://files.vagrantup.com/precise64.box'
hostname = 'dev64'
domain   = 'example.com'
ram      = '512'

Vagrant.configure(2) do |config|

  config.vm.define "dev" do |dev|
    dev.vm.box = box
    dev.vm.box_url = url
    dev.vm.host_name = hostname + '.' + domain

    dev.vm.provider :virtualbox do |prov|
      prov.customize ['modifyvm', :id,'--memory', '512']
    end

    # allow port forwarding to hit webserver from host machine
    dev.vm.network "forwarded_port", guest: 80, host: 8081

    dev.vm.provision :puppet do |puppet|
      puppet.manifests_path = 'puppet/manifests'
      puppet.manifest_file = 'site.pp'
      puppet.module_path = 'puppet/modules'
    end
  end

end
