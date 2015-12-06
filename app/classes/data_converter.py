import csv
import json


class Coverters:

    def covert_to_dict(self, filename):
        """ Read data from file and transform it to dictionary """
        out = []
        with open(filename, "r") as file:
            output = csv.DictReader(file, fieldnames=self.__labels)
            print(output)
            for row in output:
                print(row)
                out.append(row)
            # for line in file:
            # out.append(dict(zip(self.__labels, line.split('#'))))
        return out

    def json_to_csv_file(self, csv_filename, json_filename):
        """  Helper function to conver JSON to CSV file"""
        with open(json_filename) as file:
            data = json.load(file)

        with open(csv_filename, "wb+") as file:
            csv_file = csv.writer(file)
            for item in data:
                # Need to add all indexes for items
                csv_file.writerow([item['ts'], item['visitor_uuid']] + item['fields'].values())