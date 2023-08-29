# Context manager
with open("write_to_csv.csv", "a", encoding="utf-8") as my_file:
  while True:
    name = input("Name:")
    last_name = input("Last name:")
    data = (f"\n{name}¤{last_name}")
    my_file.write(data)


