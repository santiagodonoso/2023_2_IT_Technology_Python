import yaml
with open("data.yaml", "r") as yaml_file:
  data = yaml.safe_load(yaml_file)

print(data["name"])
print(data["last_name"])

# Loop trhought siblings and show their name

