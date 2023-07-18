#!/usr/bin/env python3
# Author: pr0rat
# This is a wifi simulation environment for practicing wireless network penetration testing.
# Usage: python3 mini-wifi.py
# In terminal you can type help or spawn shell for the attacker host.

from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

# Instantiate Mininet_wifi
print('********* Initializing Mininet Wifi ************\n')
net = Mininet_wifi()

# Create stations
print('********* Creating stations ************\n')
attacker = net.addStation('attacker')
host1 = net.addStation('host1', passwd='december', encrypt='wpa2')
host2 = net.addStation('host2', passwd='december', encrypt='wpa2')

print('********* Creating the Access Point ************\n')
ap = net.addAccessPoint('ap1', ssid='mywifi', passwd='december', encrypt='wpa2', mode='g', channel='6')

def create_net():
	net.configureNodes()
	print('********* Adding stations ************\n')
	net.addLink(host1, ap)
	net.addLink(host2, ap)

	net.build()
	ap.start([])
	print('********* Mininet started successfully ************\n')
	print('Run help command on the terminal to receive all the \n commands you can run in the given terminal')
	CLI(net)
	net.stop()

create_net()
