# -*- mode: ruby -*-
# vi: set ft=ruby :
# Written By: Saed Alavinia (saedalav@gmail.com)

#Requirement: 
# ansible 2.x must be available on host machine
# DEFAULT_NETWORK_INTERFACE needs to be set if multiple interface are available. 
# See: https://www.vagrantup.com/docs/networking/public_network.html

# on vagrant up
# 1. Checks to see if minimum vagrant version is being used: 
# 	Forces the use of Vagrant 1.8.4 and higher, as specified in the requirement
# 2. Deploys an Ubuntu 14 (64bit) from https://cloud-images.ubuntu.com
# 3. Configures vm to be accessible in public/bridge mode
# 	NOTE: To avoid having to set the default_network_interface, its value
# 	is defined in the file a variable (See: DEFAULT_NETWORK_INTERFACE)
# 	you may need to reset the value or commend out if not needed
# 	see: https://www.vagrantup.com/docs/networking/public_network.html
# 4. sets up vagrant synced folder (default is used)
# 5. Delegates the provisioning task to ansible via playbook.yml
# 	ansible must be installed on the host environment



# Variables
MIN_VER = "1.8.4"										
DEFAULT_NETWORK_INTERFACE = "en0: Wi-Fi (AirPort)"		#This likely needs to be set
HOST_SYNCED_FOLDER = "."								
VM_SYNCED_FOLDER = "/vagrant"
ANSIBLE_VERBOSE = false


# Forces the use of Vagrant 1.8.4 and higher, as specified in the requirement
Vagrant.require_version ">= #{MIN_VER}"

# Configure Linux Ubuntu Box
Vagrant.configure("2") do |config|
  	config.vm.box = "ubuntu14-cloudimage"
  	config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

	#Configuring VM with a public network address with DHCP assigned IP
	config.vm.network "public_network",bridge: DEFAULT_NETWORK_INTERFACE

	#Setup Vagrant Synced folder to be modified by vars 
	config.vm.synced_folder HOST_SYNCED_FOLDER,VM_SYNCED_FOLDER

	#Provision vagrant with Ansible Remote
	config.vm.provision "ansible" do |ansible|
		ansible.playbook = "provisioning/playbook.yml"
		ansible.verbose = ANSIBLE_VERBOSE
  		ansible.extra_vars = {HOST_SYNCED_FOLDER: HOST_SYNCED_FOLDER,  VM_SYNCED_FOLDER: VM_SYNCED_FOLDER}
	end

end
