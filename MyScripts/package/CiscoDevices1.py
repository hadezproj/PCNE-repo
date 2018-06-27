#!/usr/bin/env python
#from nexus import nexus
#from catalyst import catalyst
#from asa import asa
#import nexus
#import catalyst
#import asa

def nexusd():
	from nexus import nexus
	devn = nexus.nexus()
	print devn

def catd():
	from catalyst import catalyst
	devc = catalyst.catalyst()
	print devc

def asad():
	from asa import asa
	deva = asa.asa()
	print deva

if __name__ == "__main__":
	print nexusd()
	print catd()
	print asad()