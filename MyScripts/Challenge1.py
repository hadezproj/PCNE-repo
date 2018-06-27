#!/usr/bin/env python
router_list = ["router1", "router2", "router3"]

def devices():
	List = router_list
#	routers = ["router1", "router2", "router3"]
	#print "The routers are:\n"
	print List
def security():
	passwd = "passw0rd1"
	List = router_list
	credentials = {}
#	for key in List:
#		credentials[key].append(List[key])
	credentials = {List[0]: passwd, List[1]: passwd, List[2]: passwd}
	#print " The credentials are:\n"
	print credentials
def combined():
	devices()
	security()

if __name__ == "__main__":
	print "The routers are:"
	devices()
	print "The credentials are:"
	security()
	print "All data is"
	combined()
