from werkzeug.datastructures import FileStorage


def parse_csv(file: FileStorage):
    text = codecs.getreader("utf-8")(file.stream)
    reader = csv.DictReader(text, delimiter=';', fieldnames=['something'])
    for row in reader:
        yield row
