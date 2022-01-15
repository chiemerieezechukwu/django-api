import csv
import os
import sys
from django.core.management.base import BaseCommand
from cars.tests.factories import CarFactory


class Command(BaseCommand):
    help = "Populates the db from a CSV"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The location of the csv file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]
        if not os.path.exists(csv_file):
            self.stdout.write(self.style.ERROR("There's no such file at that location"))
            sys.exit(2)

        with open(csv_file, "r") as f:
            csv_reader = csv.reader(f)

            next(csv_reader)  # skip the csv header

            for line in csv_reader:
                if not "".join(line).strip():
                    continue

                manufacturer, model, car_type = line
                car = CarFactory.create(manufacturer=manufacturer, model=model, car_type=car_type)
                self.stdout.write(self.style.SUCCESS(f"Added {str(car)} with Reg no: {car.reg_no}"))
