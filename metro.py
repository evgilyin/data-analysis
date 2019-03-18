#На каких станциях московского метро сейчас идёт ремонт эскалаторов и вывести на экран их названия

from datetime import datetime, timedelta
import csv

with open('metro.csv', 'r', encoding='utf-8') as file:
	
	fields = ["ID", "Name", "Longitude_WGS84", "Latitude_WGS84", "NameOfStation", "Line", "ModeOnEvenDays", "ModeOnOddDays", "FullFeaturedBPAAmount", "LittleFunctionalBPAAmount", "BPAAmount", "RepairOfEscalators", "global_id", "geoData"]
	stations = csv.DictReader(file, fields, delimiter=';')
	repair_stations = []
	file.readline()
	for row in stations:
		name = row["Name"]
		repair_option = row["RepairOfEscalators"]
		if repair_option:
			splitted = repair_option.split('-')
			if datetime.now() > datetime.strptime(splitted[0], '%d.%m.%Y') and datetime.now() < datetime.strptime(splitted[1], '%d.%m.%Y'):
				repair_stations.append(name)
for elements in repair_stations:
	print(elements)
