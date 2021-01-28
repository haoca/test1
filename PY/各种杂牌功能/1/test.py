def sorter(item):
    return item['name']


presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Thristopher', 'age': 47}
]
print(presenters)
presenters.sort(key=sorter)
print(presenters)
