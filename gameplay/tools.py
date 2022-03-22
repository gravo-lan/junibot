import json

def add_tool_member(person):
    data = json.load(open("tools.txt"))
    if person not in data:
        data[person] = {}
        data[person]["pickaxe"] = "basic"
        data[person]["axe"] = "basic"
        data[person]["hoe"] = "basic"
        data[person]["watering can"] = "basic"
        json.dump(data, open("tools.txt", "w"))

def change_tool(value, tool, person):
    data = json.load(open("tools.txt"))
    value = str(value.lower())
    data[person][tool] = value
    json.dump(data, open("tools.txt", "w"))

def find_tool(tool, person):
    data = json.load(open("tools.txt"))
    thetool = data[person][tool]
    return thetool
