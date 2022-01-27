import json

def add_unlocked_member(person):
    data = json.load(open("unlocked.txt"))
    if person not in data:
        data[person] = {}
        data[person]["tide pools"] = False
        data[person]["secret woods"] = False
        data[person]["sewers"] = False
        data[person]["quarry"] = False
        data[person]["desert"] = False
        data[person]["casino"] = False
        data[person]["skull cavern"] = False
        data[person]["mutant bug lair"] = False
        data[person]["witch's hut"] = False
        json.dump(data, open("unlocked.txt", "w"))

def unlock_location(location, person):
    data = json.load(open("unlocked.txt"))
    data[person][location] = True
    json.dump(data, open("unlocked.txt", "w"))


def find_location_lock(location, person):
    data = json.load(open("unlocked.txt"))
    unlock = data[person][location]
    return unlock
