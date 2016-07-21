# DevOps-Challenge
A response to https://github.com/gbaker-blackbirdit/DevOps-Consultant-Challenge


The solution uses the following tools: 
Vagrant 1.8.5 
Ansible 2.1.0.0 #On branch ansible-local, ansible runs on vagrant
Python 2.7.10

How To: 
- Make sure the host machine has vagrant (min 1.8.4) installed, 
- Make sure a Virtual Machine required by vagrant is installed 
- From project directory, open vagrantfile
- set DEFAULT_NETWORK_INTERFACE in vagrantfile 
- if not set, VirtualBox might ask you to choose an interface
- execute "vagrant up"
- the solution installs and configures apache, and runs a python script that quries http://checkip.dyndns.org and prints the output to a file, along with timestamp. 
- by default output.txt is stored in /opt/pythonscripts/output.txt on the vagrant machine
- Note that the timestamp of the vagrant machine is UTC-01:00

On this branch: 
- ansible runs locally on the vagrant machine. This might be useful as you do not need to have ansible installed on the host machine (especially if the host machine is a windows where ansible is not supported). On the other hand, this is usually not a DevOps friendly practice as master controller needs to exit. 
- ansibles creates a new virtualhost.conf file and configures apache to use it
- Python script creates a basic html page that displays the output as document root of apache 
- Additionally, ansible outputs the ip address in terminal so that it is easy to test apache.
