import csv

def storeRecommendation(firstName, lastName, recommendation):
    file = open("dataStorage.csv", "r+")
    reader = csv.reader(file)

    rowCount = sum(1 for line in reader)

    row = [str(rowCount+1), firstName, lastName, recommendation]
    fileWriter = csv.writer(file)
    fileWriter.writerow(row)

    file.close()

