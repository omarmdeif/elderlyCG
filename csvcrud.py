import csv
import os
import pandas as pd

class ccrud():
    def __init__(self) -> None:
        pass

    def createFile(self, filename, field):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(field) #["COL1", "COL2", "COL3"]
            print("File Created!!!")
        pass

    def readFile(self, filename):
        df = pd.read_csv(filename)
        return df

    def updateFile(self, filename):
        # df = pd.read_csv(filename)
        # df.loc[entryid, attr] = change
        # df.to_csv(filename, index=False)
        pass

    def deleteFile(self, filename):
        if(os.path.exists(filename) and os.path.isfile(filename)):
            os.remove(filename)
            print("File Deleted!!")
        else:
            print("File not found!!!!")
        pass

    def writeRow(self, filename, field):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(field)
            print("Row Written!!!!")
        pass

    def updateRow(self, filename, attr, entryid, change):
        df = pd.read_csv(filename)
        df.loc[entryid, attr] = change
        df.to_csv(filename, index=False)
        pass
    