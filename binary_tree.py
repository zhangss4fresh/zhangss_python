#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = xiaofei.ding
@time: 2017-1205 22:23
"""

tree = {
    1: [3, 2],
    2: [5, 4],
    3: [6],
    4: [8],
    5: [],
    6: [7],
    7: [],
    8: []
}


def breadth_first_iterate(node_list):
    if len(node_list) == 0:
        return

    next_nodes = list()
    for node in node_list:
        print node
        next_nodes.extend(list(tree[node]))

    breadth_first_iterate(next_nodes)


def depth_first_iterate(node):
    print node
    node_list = tree[node]
    for node in node_list:
        depth_first_iterate(node)


if __name__ == '__main__':
    breadth_first_iterate([1])
    print '-' * 10
    depth_first_iterate(1)
    pass
