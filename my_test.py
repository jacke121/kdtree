from __future__ import absolute_import

import sys
import random
import logging
import unittest
import doctest
import collections
from itertools import islice

# import after starting coverage, to ensure that import-time code is covered
import kdtree

def random_point(dimensions=3, minval=0, maxval=100):
    return tuple(random.randint(minval, maxval) for _ in range(dimensions))

def random_points(dimensions=3, minval=0, maxval=100):
    while True:
        yield random_point(dimensions, minval, maxval)

def random_tree(nodes=20, dimensions=3, minval=0, maxval=100):
    points = list(islice(random_points(), 0, nodes))
    tree = kdtree.create(points)
    return tree

def do_random_add(num_points=100):
    points = list(set(islice(random_points(), 0, num_points)))
    tree = kdtree.create(dimensions=len(points[0]))
    for n, point in enumerate(points, 1):
        tree.add(point)
        print(tree.is_valid())
        print(point in [node.data for node in tree.inorder()])
        nodes_in_tree = len(list(tree.inorder()))
        print(nodes_in_tree, n)
tree = random_tree()

inorder_len = len(list(tree.inorder()))
preorder_len = len(list(tree.preorder()))
postorder_len = len(list(tree.postorder()))
print(inorder_len,preorder_len,postorder_len)

for i in range(10):
    do_random_add()


