import json

def add_location_member(person):
    data = json.load(open("./location.json"))
    if person not in data:
        data[person] = "farm"
        json.dump(data, open("./location.json", "w"))

def change_location(location, person):
    data = json.load(open("./location.json"))
    location = str(location.lower())
    data[person] = location
    json.dump(data, open("./location.json", "w"))


def find_location(person):
    data = json.load(open("./location.json"))
    location = data[person]
    return location
