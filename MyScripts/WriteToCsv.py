import csv
DeviceData = [['router4', 'Lou', 'Passw0rd1!']]
file = open('newfile', 'w')
with file:
	writer = csv.writer(file)
	writer.writerows(DeviceData)
print('the file has been created')