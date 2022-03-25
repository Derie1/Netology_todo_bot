import json


tasks = {"id": [1948, 2545, 6525], "name": "Washer", "size": 3}
print(tasks)

def to_file(tasks):
    json.dump(tasks, open("tasks.txt", "w"))

def from_file():
    return open("tasks.txt").read()

to_file(tasks)

print(tasks)
print(type(tasks))


# tasks = from_file()

# print(tasks)
# print(type(tasks))
