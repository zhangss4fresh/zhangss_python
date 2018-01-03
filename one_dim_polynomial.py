#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/3 22:00
# @Author  : zhangss
# @Software: PyCharm
"""


class Node:
    def __init__(self, coefficient, exponent, index):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next_index = index


class Polynomial:
    def __init__(self):
        self.head_node = Node(None, None, None)
        self.nodes = list()

    def create_poly(self, parameters):
        if parameters is None or len(parameters) == 0:
            return

        self.head_node.next_index = 0
        next_index = self.head_node.next_index
        for c, e in parameters:
            next_index += 1
            node = Node(c, e, next_index)
            self.nodes.append(node)

        # note that the next_index of last node is None, meaning ending
        last_node = self.nodes[-1]
        last_node.next_index = None
        self.nodes[-1] = last_node

        return self

    def print_poly(self):
        line = ''
        index = self.head_node.next_index
        while index is not None and index < len(self.nodes):
            node = self.nodes[index]
            line += ' + %d*x^%d' % (node.coefficient, node.exponent)
            index = node.next_index
        print line.strip(' ').strip('+')

    def ploy_length(self):
        if self.head_node.next_index is None or len(self.nodes) == 0:
            return 0

        length = 0
        index = self.head_node.next_index
        while index is not None and index < len(self.nodes):
            length += 1
            node = self.nodes[index]
            index = node.next_index
        return length

    def add_poly(self, another_poly):
        head_a = self.head_node
        head_b = another_poly.head_node

        nodes_a = self.nodes
        nodes_b = another_poly.nodes

        len_a = self.ploy_length()
        len_b = another_poly.ploy_length()

        if head_a.next_index is None or len_a == 0:
            return another_poly

        if head_b.next_index is None or len_b == 0:
            return self

        new_paras = list()
        index_a = head_a.next_index
        index_b = head_b.next_index
        while index_a is not None and index_b is not None and index_a < len(nodes_a) and index_b < len(nodes_b):
            exp_a = nodes_a[index_a].exponent
            exp_b = nodes_b[index_b].exponent
            if exp_a == exp_b:
                new_coef = nodes_a[index_a].coefficient + nodes_b[index_b].coefficient
                if new_coef == 0:
                    pass
                else:
                    new_paras.append((new_coef, exp_a))

                index_a = nodes_a[index_a].next_index
                index_b = nodes_b[index_b].next_index
            elif exp_a < exp_b:
                new_paras.append((nodes_a[index_a].coefficient, exp_a))
                index_a = nodes_a[index_a].next_index
            else:
                new_paras.append((nodes_b[index_b].coefficient, exp_b))
                index_b = nodes_b[index_b].next_index

        # 至少一个为None
        if index_a is None and index_b is None:
            pass
        elif index_a is None:
            while index_b:
                new_paras.append((nodes_b[index_b].coefficient, nodes_b[index_b].exponent))
                index_b = nodes_b[index_b].next_index
        else:
            while index_a:
                new_paras.append((nodes_a[index_a].coefficient, nodes_a[index_a].exponent))
                index_a = nodes_a[index_a].next_index

        new_poly = Polynomial()
        new_poly.create_poly(new_paras)
        return new_poly

    def suntract_poly(self, another_poly):
        return None

    def multiply_poly(self, another_poly):
        return None


if __name__ == '__main__':
    paras = list()
    for i in range(1, 5):
        paras.append((i, i+1))

    p_a = Polynomial()
    p_a.create_poly(paras)
    print "poly a, len(%d):" % p_a.ploy_length()
    p_a.print_poly()

    paras.remove((1, 2))
    paras.append((5, 6))
    p_b = Polynomial()
    p_b.create_poly(paras)
    print "poly b, len(%d):" % p_b.ploy_length()
    p_b.print_poly()

    p_c = p_a.add_poly(p_b)
    print "poly c, len(%d):" % p_c.ploy_length()
    p_c.print_poly()
    pass
