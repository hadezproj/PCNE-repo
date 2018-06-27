import re

interface = "Hardware is CSR vNIC, address is 0050.5602.415a (bia 0050.5602.415a)"
# mac = re.search("0050.56", interface)
mac = re.search("0050.56.......", interface)
# print "There is a device OUI: ", mac.group(0), "\n"
print "The MAC of the devices is ", mac.group(0), "\n"
print "Vendor is VMware."

# print (mac.group(0))