# DevOps-Challenge
A response to https://github.com/gbaker-blackbirdit/DevOps-Consultant-Challenge


The solution uses the following tools: 
Vagrant 1.8.5 
Ansible 2.1.0.0 
Python 2.7.10

How To: 
- Make sure the host machine has vagrant (min 1.8.4) installed, 
- Make sure the host machine has ansible (pref 2.1) installed,
- Make sure a Virtual Machine required by vagrant is installed 
- From project directory, open vagrantfile
- set DEFAULT_NETWORK_INTERFACE in vagrantfile 
- if not set, VirtualBox might ask you to choose an interface
- execute "vagrant up"
- the solution installs and configures apache, and runs a python script that quries http://checkip.dyndns.org and prints the output to a file, along with timestamp. 
- by default output.txt is stored in /opt/pythonscripts/output.txt on the vagrant machine
- Note that the timestamp of the vagrant machine is UTC-01:00

