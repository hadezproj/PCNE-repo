#!/usr/bin/env python
def device():
	print "Router1"
	print "Router2"

def ip():
	print "10.10.10.10"
	print "20.20.20.20"

def both():
	device()
	ip()

if __name__ == "__main__":
	device()
	ip()
	both()
