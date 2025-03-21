import json

# load Json form file
file = open('einstein_quotes.json')
data1 = json.load(file)
print(data1)
print(type(data1))
print(data1[0]['_id'])
print(data1[0]['author'])

# load Json form String
string = '''[
    {
    "_id": 1,
    "author": "Albert Einstein",
    "quote": "Everything should be as simple as it can be, but not simpler!",
    "source": null
    },
    {
    "_id": 2,
    "author": "Albert Einstein",
    "quote": "Logic will get you from A to Z; imagination will get you everywhere.",
    "source": null
    },
    {
    "_id": 3,
    "author": "Albert Einstein",
    "quote": "Try not to become a man of success. Rather become a man of value.",
    "source": null
    },
    {
    "_id": 4,
    "author": "Albert Einstein",
    "quote": "It is not that I'm so smart. But I stay with the questions much longer.",
    "source": null
    }
]'''
data2 = json.loads(string)
print(data2)
print(type(data2))