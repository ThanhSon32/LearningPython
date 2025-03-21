import json
import pandas as pd

file = open('sea_level_rise.json', 'r')
data = json.load(file)
file.close

print('defaultArgument: ')
defaultArgument = pd.json_normalize(data)
print(defaultArgument)

print('recordPathArgument: ')
recordPathArgument = pd.json_normalize(data, record_path=['meta','view','columns'])
print(recordPathArgument)

print('metaArgument: ')
metaArgument = pd.json_normalize(data, record_path='data', meta = 'meta')
print(metaArgument)