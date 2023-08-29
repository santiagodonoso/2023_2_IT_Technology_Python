import yaml
with open("data.yaml", "r") as yaml_file:
  data = yaml.safe_load(yaml_file)

print(data["name"])
print(data["last_name"])

# Loop through siblings and show their name
for sibling in data["siblings"]:
  print(sibling.get("name"))
  print(sibling["name"])