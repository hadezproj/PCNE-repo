""" interface = 1

while interface <=10:
	print "Interface G1/{}".format(interface)
	print "\t no switchport"
	interface +=1
"""
switch = ""
if "Catalyst" in switch:
	print "Switch is a Catalyst."
elif "Nexus" in switch:
	print "Switch is a Nexus."
else:
	print "Switch is non Cisco."
