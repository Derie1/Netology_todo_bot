import pickle


tasks = {"id": [1948, 2545, 6525], "name": "Washer", "size": 3}
print(tasks)

def to_file(tasks):
    with open("tasks.txt", "wb") as f:
        pickle.dump(tasks, f)

def from_file():
    with open("tasks.txt", "rb") as f:
        return pickle.load(f)

# to_file(tasks)

# print(tasks)
# print(type(tasks))


tasks = from_file()

print(tasks)
print(type(tasks))
for task in tasks:
    print(type(tasks[task]))
