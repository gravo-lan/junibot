import json

def add_forage_member(person):
    data = json.load(open("forage.txt", "r"))
    if person not in data:
        data[person] = {}
        data[person]["wild horseradish"] = 0
        data[person]["daffodil"] = 0
        data[person]["leek"] = 0
        data[person]["dandelion"] = 0
        data[person]["spring onion"] = 0
        data[person]["morel"] = 0
        data[person]["common mushroom"] = 0
        data[person]["salmonberry"] = 0
        data[person]["spice berry"] = 0
        data[person]["grape"] = 0
        data[person]["sweet pea"] = 0
        data[person]["red mushroom"] = 0
        data[person]["fiddlehead fern"] = 0
        data[person]["wild plum"] = 0
        data[person]["hazelnut"] = 0
        data[person]["blackberry"] = 0
        data[person]["chanterelle"] = 0
        data[person]["purple mushroom"] = 0
        data[person]["winter root"] = 0
        data[person]["crystal fruit"] = 0
        data[person]["snow yam"] = 0
        data[person]["crocus"] = 0
        data[person]["holly"] = 0
        data[person]["nautilus shell"] = 0
        data[person]["coral"] = 0
        data[person]["sea urchin"] = 0
        data[person]["rainbow shell"] = 0
        data[person]["clam"] = 0
        data[person]["cockle"] = 0
        data[person]["mussel"] = 0
        data[person]["oyster"] = 0
        data[person]["cave carrot"] = 0
        data[person]["cactus fruit"] = 0
        data[person]["coconut"] = 0
        json.dump(data, open("forage.txt", "w"))

def add_forageable(item, number, person):
    data = json.load(open("forage.txt", "r"))
    item = str(item.lower())
    data[person][item] = data[person][item] + number
    json.dump(data, open("forage.txt", "w"))
        
def remove_forageable(item, number, person):
    data = json.load(open("forage.txt", "r"))
    item = str(item.lower())
    data[person][item] = data[person][item] - number
    json.dump(data, open("forage.txt", "w"))

def find_forageable(item, person):
    data = json.load(open("forage.txt", "r"))
    item = str(item.lower())
    return data[person][item]
