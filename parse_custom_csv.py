import csv
# context manager - file closes automatically
with open("custom.csv", encoding="utf-8") as my_file:
  file_reader = csv.reader(my_file, delimiter="¤", quotechar='"')
  next(file_reader) # Go to next row
  print("Users\n")
  for row in file_reader:
    print(row[0], row[1], row[2])

