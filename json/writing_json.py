import json

data = {
    'foo': [
        'bar_1',
        'bar_2',
        'bar_3'
    ]
}

with open('writedconfig.json', 'w') as outfile:
    json.dump(data, outfile)