#!/usr/bin/python

# Define variables
PUPPET_MASTER_IP = '192.168.0.10'
PUPPET_HOSTNAME = 'puppet-agent-01'
PUPPET_CERT_NAME = 'puppet-agent-01.example.com'

import subprocess

# Install Puppet agent dependencies
subprocess.run(['yum', 'install', '-y', 'curl', 'policycoreutils-python', 'selinux-policy-targeted'])

# Download and install Puppet agent
subprocess.run(['curl', '-O', 'https://yum.puppetlabs.com/puppet6/puppet6-release-el-7.noarch.rpm'])
subprocess.run(['rpm', '-Uvh', 'puppet6-release-el-7.noarch.rpm'])
subprocess.run(['yum', 'install', '-y', 'puppet-agent'])

# Configure Puppet agent
with open('/etc/puppetlabs/puppet/puppet.conf', 'w') as f:
    f.write('[main]\n')
    f.write('server=' + PUPPET_MASTER_IP + '\n')
    f.write('certname=' + PUPPET_CERT_NAME + '\n')
    f.write('environment=production\n')

# Start Puppet agent
subprocess.run(['systemctl', 'start', 'puppet'])
subprocess.run(['systemctl', 'enable', 'puppet'])