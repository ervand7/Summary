import csv
from django.core.management.base import BaseCommand
from measurements.models import Project, Measurement


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('objects_on_the_map.csv', 'r') as csvfile:
            objects_on_the_map_reader = csv.DictReader(csvfile, delimiter=';')
            for item in objects_on_the_map_reader:
                obj = Project(**{key: value for key, value in item.items() if key})
                obj.save()

        with open('measurements_results.csv', 'r') as csvfile:
            measurements_results_reader = csv.DictReader(csvfile, delimiter=';')
            for item in measurements_results_reader:
                measurement_result = Measurement(**{key: value for key, value in item.items() if key})
                measurement_result.save()

