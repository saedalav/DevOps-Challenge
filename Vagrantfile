# -*- mode: ruby -*-
# vi: set ft=ruby :
# Written By: Saed Alavinia (saedalav@gmail.com)

# on vagrant up
# 1. Deploys an Ubuntu 14 (64bit)



# Variables
MIN_VER = "1.8.4"
DEFAULT_NETWORK_INTERFACE = "en0: Wi-Fi (AirPort)"


# Forces the use of Vagrant 1.8.4 and higher, as specified in the requirement
Vagrant.require_version ">= #{MIN_VER}"

# Configure Linux Ubuntu Box
Vagrant.configure("2") do |config|
  	config.vm.box = "ubuntu14-cloudimage"
  	config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

	#Configuring VM with a public network address with DHCP assigned IP
	config.vm.network "public_network",bridge: "#{DEFAULT_NETWORK_INTERFACE}"

	#Provision vagrant with Ansible Remote
	config.vm.provision "ansible" do |ansible|
		ansible.playbook = "playbook.yml"
	end

end
