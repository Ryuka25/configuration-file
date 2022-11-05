import json

with open("fileconfig.json") as json_data_file:
    data = json.load(json_data_file)

print(data)