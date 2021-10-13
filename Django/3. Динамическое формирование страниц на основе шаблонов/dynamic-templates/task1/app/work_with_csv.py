import csv


def get_csv_file_content(delimiter=';'):

    csv.register_dialect(
        'customcsv', delimiter=delimiter,
        doublequote=True,
        lineterminator='\r\n',
        quotechar='"',
        quoting=0,
        skipinitialspace=False,
        escapechar=None,
        strict=False
    )

    file = 'inflation_russia.csv'
    with open(file=file, encoding='UTF-8') as csv_file:
        columns_names = csv_file.readline().strip().split(delimiter)
        reader_object = csv.DictReader(csv_file, dialect='customcsv')
        csv_file.seek(0)
        table_horizon_rows_as_dicts = [dct for dct in reader_object]

    return table_horizon_rows_as_dicts, columns_names
