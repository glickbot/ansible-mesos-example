hachiman-stack
================
### Ansible scripts to start mesos, mesos-dns, marathon, and docker

### Usage

- Install Ansible following the [http://docs.ansible.com/ansible/intro_installation.html](installation instructions for your platform).

- Checkout the [https://github.com/basho-labs/hachiman-stack](hachiman-stack repo):
```
git clone https://github.com/basho-labs/hachiman-stack.git
```

- Change to the `hachiman-stack` directory of the newly checked-out repo:
```
cd hachiman-stack
```

- Gather the following information about the environment you will be deploying to:

    - IPs of the various nodes



configure playbook.yml if need be

execute:

	ansible-playbook -i hosts.ini playbook.yml
