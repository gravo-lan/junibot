import json

def add_location_member(person):
    data = json.load(open("location.txt"))
    if person not in data:
        data[person] = "farm"
        json.dump(data, open("location.txt", "w"))

def change_location(location, person):
    data = json.load(open("location.txt"))
    location = str(location.lower())
    data[person] = location
    json.dump(data, open("location.txt", "w"))


def find_location(person):
    data = json.load(open("location.txt"))
    location = data[person]
    return location
