from collections import deque

# create a graph
graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}


def is_seller(name: str):
    if name[-1] == 'm':
        return True
    return False


def search(name):
    queue = deque()
    queue += graph[name]
    searched = []
    while queue:
        person = queue.popleft()
        if person not in searched:
            if is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                queue += graph[person]
                searched.append(person)
    return False


search('you')
