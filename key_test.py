import datetime
import random

import kdtree

# This class emulates a tuple, but contains a useful payload
class Item(object):
    def __init__(self, data,name):
        self.coords = data
        self.name = name

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, i):
        return self.coords[i]

    def __repr__(self):
        return 'Item({}, {})'.format(self.name,self.coords )

data=[]
for i in range(2):
    ran_d1= [random.randint(0,255) for _ in range(100)]
    point1 = Item(ran_d1, str(i))
    data.append(point1)

# Again, from a list of points
tree = kdtree.create(data)

for i in range(100):
    ran_d1= [random.randint(0,255) for _ in range(100)]
    point1 = Item(ran_d1, str(i+2))
    tree.add(point1)


# print(tree)#  The root node

# ...contains "data" field with an Item, which contains the payload in "data" field
print(tree.data.name)

# All functions work as intended, a payload is never lost
time1=datetime.datetime.now()
print(tree.search_nn([random.randint(0,255) for _ in range(100)]))
print("time",(datetime.datetime.now()-time1).microseconds)