import json

def add_tool_member(person):
    data = json.load(open("./tools.json"))
    if person not in data:
        data[person] = {}
        data[person]["pickaxe"] = "basic"
        data[person]["axe"] = "basic"
        data[person]["hoe"] = "basic"
        data[person]["watering can"] = "basic"
        json.dump(data, open("./tools.json", "w"))

def change_tool(value, tool, person):
    data = json.load(open("./tools.json"))
    value = str(value.lower())
    data[person][tool] = value
    json.dump(data, open("./tools.json", "w"))

def find_tool(tool, person):
    data = json.load(open("./tools.json"))
    thetool = data[person][tool]
    return thetool
