import json

file = open('navigate.json')
data = json.load(file)

# all
print('all: ')
print(data)

# first layer
print('first layer: ')
print(data.keys())
print(data.values())

# second layer
print('second layer: ')
print(data['Key'])
print(data['Key5'])

# third layer
print('third layer: ')
print(data['Key'][0])
print(data['Key'][1])

# fourth layer
print('fourth layer: ')
print(data['Key'][0]['Key2'])