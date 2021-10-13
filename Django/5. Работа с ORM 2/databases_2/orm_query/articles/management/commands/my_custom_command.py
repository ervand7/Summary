import csv
from django.core.management.base import BaseCommand
from articles.models import Author, Genre


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('authors.csv', 'r') as csvfile:
            authors_reader = csv.DictReader(csvfile, delimiter=';')
            for item in authors_reader:
                author = Author(**{key: value for key, value in item.items() if key})
                author.save()

        with open('genres.csv', 'r') as csvfile:
            genres_reader = csv.DictReader(csvfile, delimiter=';')
            for item in genres_reader:
                genre = Genre(**{key: value for key, value in item.items() if key})
                genre.save()
