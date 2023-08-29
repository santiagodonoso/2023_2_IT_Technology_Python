import csv
# context manager - file closes automatically
with open("data.csv") as my_file:
  file_reader = csv.reader(my_file, delimiter=",", quotechar='"')
  for row in file_reader:
    print(row[0], row[1], row[2])

