#!/usr/bin/env python
def vlans_exist(vlan_id):
	Vlan_List = [1, 5, 10, 20]
	return vlan_id in Vlan_List

""" def ip():
	print "10.10.10.10"
	print "20.20.20.20"

def both():
	device()
	ip()
"""
if __name__ == "__main__":
#	device()
#	ip()
#	both()
#	Vlans_exist = vlans_exist
	vlan = [10, 20, 100, 200]
	for Vlan in vlan:
		"""
		if Vlan == vlans_exist(Vlan): 
			print "This vlan id {}".format(Vlan)," exists."
		else:
			print "This vlan id {}".format(Vlan)," does not exists."
		"""
		print Vlan, vlans_exist(Vlan)