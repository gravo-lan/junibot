import json

def add_money(added_number, author):
    coins = json.load(open('./money.json', 'r'))
    matchedLine = int(coins[str(author)])
    newvalue = matchedLine + added_number
    coins[str(author)] = str(newvalue)
    json.dump(coins, open('./money.json', 'w'))

def remove_money(removed_number, author):
    coins = json.load(open('./money.json', 'r'))
    matchedLine = int(coins[str(author)])
    newvalue = matchedLine - removed_number
    if newvalue <= 0:
        newvalue = 0
    coins[str(author)] = str(newvalue)
    json.dump(coins, open('./money.json', 'w'))

def find_money(author):
    file = json.load(open('./money.json', 'r'))
    matchedLine = file[str(author)]
    return int(matchedLine)
