import json

def find_sword(author):
    file = json.load(open('sword.txt', 'r'))
    matchedLine = file[str(author)]
    return str(matchedLine)

def change_sword(sword, author):
    coins = json.load(open('sword.txt', 'r'))
    coins[str(author)] = str(sword)
    json.dump(coins, open('sword.txt', 'w'))
    return

