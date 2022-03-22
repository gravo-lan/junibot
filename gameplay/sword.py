import json

def find_sword(author):
    file = json.load(open('./sword.json', 'r'))
    matchedLine = file[str(author)]
    return str(matchedLine)

def change_sword(sword, author):
    coins = json.load(open('./sword.json', 'r'))
    coins[str(author)] = str(sword)
    json.dump(coins, open('./sword.json', 'w'))
    return

