import csv

with open('mos-data.csv', 'r', encoding='utf-8') as file:
    fields = ["ID", "Name", "Longitude_WGS84", "Latitude_WGS84", "Street", "AdmArea", "District", "RouteNumbers", "StationName", "Direction", "Pavilion", "OperatingOrgName", "EntryState", "global_id", "geoData"]
    stations = csv.DictReader(file, fields, delimiter=';')
    streets = {}
    max_stations = 0
    name_max_stations_street = []
    for row in stations:
        street = row["Street"]
        if street not in streets:
            streets[street] = 1
        else: 
            streets[street] = streets[street] + 1
    
        if streets[street] > max_stations:
            max_stations = streets[street]
            name_max_stations_street = [street,]
        elif streets[street] ==  max_stations:
            max_stations = streets[street]
            name_max_stations_street.append(street)
    print(f"Больше всего остановок здесь: {(', '.join(name_max_stations_street))} - {max_stations}")


        