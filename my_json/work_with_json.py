import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)


json_string = json.dumps(data)
print(json_string)
json_string = json.dumps(data, indent=4)
print(json_string)

with open("input.json", "r") as read_file:
    data = json.load(read_file)

print(data)
print(data['firstName'])
print(data['children'])
print(data['children'][0])
print(data['children'][0]['firstName'])