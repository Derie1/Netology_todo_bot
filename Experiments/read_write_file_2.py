tasks = {"id": [1948, 2545, 5485], "name": "Washer", "size": 3}


def to_file(tasks):
    with open('tasks.txt','w') as out:
        for key,val in tasks.items():
            out.write('{}: {}\n'.format(key, val))


def from_file():
    tasks = {}
    with open('tasks.txt', 'r') as inp:
        for i in inp.readlines():
            key, val = i.strip().split(': ')
            tasks[key] = list(val)
    return tasks


print(tasks)

# to_file(tasks)
print(tasks)
print(type(tasks))

tasks = from_file()

print(tasks)
print(type(tasks))
for task in tasks:
    print(type(tasks[task]))
