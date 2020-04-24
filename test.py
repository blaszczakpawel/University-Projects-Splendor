import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.json', mode='r+') as file:
    dataFromFile=None
    json.dump(dataFromFile,file)
    for i in data:
        dataFromFile.append(i)
    file.seek(0)
    json.dump(dataFromFile,file)