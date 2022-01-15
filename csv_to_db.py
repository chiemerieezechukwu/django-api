#!/usr/bin/python
import sys
import csv
import getopt
import os


def main(argv):
    csv_file = ""
    try:
        opts, args = getopt.getopt(argv, "h:i:", ["help=", "csv-file="])
    except getopt.GetoptError:
        print("usage: ./test.py -i <csvfile> [--csv-file=<csvfile>]")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("usage: ./test.py -i <csvfile> [--csv-file=<csvfile>]")

        elif opt in ("-i", "--csv-file"):
            csv_file = arg

            if not os.path.exists(csv_file):
                print("There's no such file at that location")
                sys.exit(2)

    def process_csv(csv_file):
        with open(csv_file, "r") as f:
            csv_reader = csv.reader(f)

            next(csv_reader)

            for line in csv_reader:
                if not ''.join(line).strip():
                    continue
                brand, model, car_type = line
                print(brand, model, car_type)

    if csv_file:
        process_csv(csv_file)


if __name__ == "__main__":
    main(sys.argv[1:])
