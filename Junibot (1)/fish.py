import json

def change_rod(rod, person):
    data = json.load(open("fish.txt", "r"))
    data[person]["rod"] = rod
    json.dump(data, open("fish.txt", "w"))

def add_member(person):
    data = json.load(open("fish.txt", "r"))
    if person not in data:
        data[person] = {}
        data[person]["rod"] = "no rod"
        data[person]["carp"] = 0
        data[person]["herring"] = 0
        data[person]["smallmouth bass"] = 0
        data[person]["anchovy"] = 0
        data[person]["sardine"] = 0
        data[person]["sunfish"] = 0
        data[person]["bream"] = 0
        data[person]["perch"] = 0
        data[person]["chub"] = 0
        data[person]["red snapper"] = 0
        data[person]["sea cucumber"] = 0
        data[person]["rainbow trout"] = 0
        data[person]["walleye"] = 0
        data[person]["bullhead"] = 0
        data[person]["shad"] = 0
        data[person]["largemouth bass"] = 0
        data[person]["salmon"] = 0
        data[person]["ghostfish"] = 0
        data[person]["flounder"] = 0
        data[person]["tilapia"] = 0
        data[person]["halibut"] = 0
        data[person]["woodskip"] = 0
        data[person]["red mullet"] = 0
        data[person]["midnight carp"] = 0
        data[person]["slimejack"] = 0
        data[person]["tiger trout"] = 0
        data[person]["albacore"] = 0
        data[person]["stonefish"] = 0
        data[person]["sandfish"] = 0
        data[person]["tuna"] = 0
        data[person]["eel"] = 0
        data[person]["catfish"] = 0
        data[person]["squid"] = 0
        data[person]["pufferfish"] = 0
        data[person]["super cucumber"] = 0
        data[person]["sturgeon"] = 0
        data[person]["dorado"] = 0
        data[person]["void salmon"] = 0
        data[person]["ice pip"] = 0
        data[person]["lingcod"] = 0
        data[person]["lava eel"] = 0
        data[person]["scorpion carp"] = 0
        data[person]["octopus"] = 0
        data[person]["midnight squid"] = 0
        data[person]["spook fish"] = 0
        data[person]["blobfish"] = 0
        data[person]["crimsonfish"] = 0
        data[person]["angler"] = 0
        data[person]["legend"] = 0
        data[person]["glacierfish"] = 0
        data[person]["mutant carp"] = 0
        data[person]["seaweed"] = 0
        data[person]["green algae"] = 0
        data[person]["white algae"] = 0
        json.dump(data, open("fish.txt", "w"))

def add_fish(fish, number, person):
    data = json.load(open("fish.txt", "r"))
    fishy = str(fish.lower())
    data[person][fishy] = data[person][fishy] + number
    json.dump(data, open("fish.txt", "w"))
        
def remove_fish(fish, number, person):
    data = json.load(open("fish.txt", "r"))
    fishy = str(fish.lower())
    data[person][fishy] = data[person][fishy] - number
    json.dump(data, open("fish.txt", "w"))

def find_fish(fish, person):
    data = json.load(open("fish.txt", "r"))
    fishy = str(fish.lower())
    return data[person][fishy]
