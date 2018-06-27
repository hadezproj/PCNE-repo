import csv
with open('devices.csv') as csvfile:
	testreader = csv.reader(csvfile, delimiter = ' ', quotechar ='|')
	# adsfadfasdf
	# asdfasdfasfds
	for line_number, row in zip(range(3), csvfile):
			print row