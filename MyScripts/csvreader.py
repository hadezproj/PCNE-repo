#!/usr/bin/env python
import csv

with open("devices.csv") as csvfile:
	testreader = csv.reader(csvfile)
	for row in testreader:
		print ",".join(row)