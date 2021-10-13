import csv


def get_csv_file_content():
    csv.register_dialect(
        'customcsv', delimiter=',',
        doublequote=True,
        lineterminator='\r\n',
        quotechar='"',
        quoting=0,
        skipinitialspace=False,
        escapechar=None,
        strict=False
    )

    file = 'bus_stations.csv'
    with open(file=file, newline='', encoding='cp1251') as file:
        reader_object = csv.DictReader(file, dialect='customcsv')
        csv_content = [
            bus_station_data for bus_station_data in reader_object
        ]
    return csv_content



