import traceback

from django.core.management.base import BaseCommand
# import function file to run here
from csvgeneration.functions import generate_csv


class Command(BaseCommand):

    def add_arguments(self, parser):
        # pass in argument and url
        # normal conversion to csv
        parser.add_argument('-b', '--base', type=str)
        # upper bound of threshold
        parser.add_argument('-u', '--upper', type=str)
        # lower bound of threshold
        parser.add_argument('-l', '--lower', type=str)

    def handle(self, *args, **options):
        try:
            print(f"Converting json file to csv...")
            if options['base']:
                path = options['base']
                generate_csv.vehicular_data(path)
                print("Successfully converted to csv")
            if options['upper']:
                path = options['upper']
                generate_csv.mag_high(path)
                print("Converted to csv with magy > 0.09")
            if options['lower']:
                path = options['lower']
                generate_csv.mag_low(path)
                print("Converted to csv with magy < 0.09")
        except Exception as e:
            traceback.print_exc()
            print(f"Generate CSV: {e}")
            raise Exception("Generation of csv failed")

