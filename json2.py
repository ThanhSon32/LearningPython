import json

file = open('einstein_quotes.json')
data = json.load(file)

print(data)

exportFile = open('new_json.json', 'w')
json.dump(data, exportFile, indent=2)
exportFile.close