"""pulls the data and extracts the relevent information from it."""

import csv


class PullingData:

    def __init__(self, datacount):
        self.datacount = datacount

    def GetData(self):
        fulldata = open('mpst_full_data.csv', encoding='utf-8')
        readdata = csv.reader(fulldata)
        data = list(readdata)
        titles = []
        synopses = []
        countvar = 0
        for i in data:
            titles.append(i[1])
            synopses.append(i[2])
            if countvar == self.datacount:
                break
            countvar += 1
        del titles[0]
        del synopses[0]
        return titles, synopses
