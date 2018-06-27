#!/usr/bin/env python
import csv

with open("devices.csv") as csvfile:
	testreader = csv.reader(csvfile, delimiter = " ", quotechar= "|")
	for row in testreader:
#		print ",".join(row)
		print row[1]