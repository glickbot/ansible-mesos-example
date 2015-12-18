hachiman-stack
================
### Ansible scripts to start mesos, mesos-dns, marathon, and docker

### Requirements
##### Ansible
Install Ansible following the [installation instructions for your platform](http://docs.ansible.com/ansible/intro_installation.html).

##### Environment
* Hosts to install Mesos on:
	* Hostnames/IPs
	* SSH configured for non-interactive access
	* Hosts must have DNS or /etc/hosts configured
		* peer hostnames should resolve to internal interface



### OS DCOS Installation
Checkout the [hachiman-stack repo](https://github.com/basho-labs/hachiman-stack):

	git clone https://github.com/basho-labs/hachiman-stack.git
	cd hachiman-stack

Copy and modify ```hosts.ini.example``` to ```hosts.ini``` with information pertaining to your enviornment:

	cp hosts.ini.example hosts.ini
	
Example hosts.ini:

```[local]
localhost

[mesos_masters]
172.22.1.1

[mesos_dns]
172.22.1.2

[mesos_slaves]
172.22.1.2
172.22.1.3
172.22.1.4
172.22.1.5
172.22.1.6
172.22.1.7
172.22.1.8
172.22.1.9
172.22.1.10

[mesos:children]
mesos_masters
mesos_slaves

[mesos:vars]
ansible_ssh_user=root
ns1=10.0.80.11
ns2=10.0.80.12
```

execute:

	ansible-playbook -i hosts.ini playbook.yml

### Installing Kafka/Riak/Spark with the DCOS-CLI

##### Install the DCOS-CLI
Install DCOS-CLI following the [installation instructions here](https://github.com/mesosphere/dcos-cli).

Configure DCOC-CLI for [OS Mesos/Marathon Deployment](https://github.com/mesosphere/dcos-cli#using-the-cli-without-dcos)


	dcos config set core.mesos_master_url http://<mesos-master-host>:5050
	dcos config set marathon.url http://<marathon-host>:8080

Update Packages
	
	dcos package update

#### Installing Kafka

Install the DCOS-CLI Kafka package:

	dcos package install kafka
	
View dcos help for broker/topic instructions:

	dcos kafka help
	
#### Installing Spark

Install the DCOS-CLI Spark package:

	dcos package install spark

View dcos help for spark usage:

	dcos spark help
	
#### Installing Riak

Add the Riak Repo to dcos package.sources (see [http://github.com/basho-labs/riak-mesos](http://github.com/basho-labs/riak-mesos) for url):

	dcos config prepend package.sources "<riak-dcos repo zip>"

Install the DCOS-CLI Riak package:

	dcos pacakge install riak

View dcos help for Riak usage:

	dcos riak help
