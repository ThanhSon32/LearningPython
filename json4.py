import json

file = open('einstein_quotes.json', 'r')
data = json.load(file)
file.close

print('Original data: ')
print(data)

data.append({'author': 'Son Phan'})
data.insert(0,{'_id': 0})
data.pop(1)

extension = [
    {'_id': 5, 'author': 'Isaac Newton', 'quote': 'If I have seen further it is by standing on the shoulders of Giants.', 'source': None}
]
data.extend(extension)

data.reverse()
print('Modified data: ')
print(data)