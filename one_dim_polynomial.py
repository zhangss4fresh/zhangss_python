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

        # next_index of last node is None, meaning ending
        self.nodes[-1].next_index = None

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
        head_b = another_poly.head_node
        nodes_b = another_poly.nodes
        len_b = another_poly.ploy_length()

        if self.head_node.next_index is None or self.ploy_length() == 0:
            return another_poly

        if head_b.next_index is None or len_b == 0:
            return self

        last_node_a = self.head_node
        last_node_b = head_b
        last_index_a = None
        while last_node_a.next_index is not None and last_node_b.next_index is not None \
                and last_node_a.next_index < len(self.nodes) and last_node_b.next_index < len(nodes_b):
            index_a = last_node_a.next_index
            index_b = last_node_b.next_index
            exp_a = self.nodes[index_a].exponent
            exp_b = nodes_b[index_b].exponent
            if exp_a == exp_b:
                new_coef = self.nodes[index_a].coefficient + nodes_b[index_b].coefficient
                if new_coef == 0:
                    last_node_a.next_index = self.nodes[index_a].next_index
                    if last_index_a is not None:  # is not head node
                        self.nodes[last_index_a] = last_node_a
                    else:  # todo 由于引用 last_node_a，这里的逻辑其实多余了
                        self.head_node.next_index = self.nodes[index_a].next_index
                        last_node_a = self.head_node
                else:
                    self.nodes[index_a].coefficient = new_coef
                    last_node_a = self.nodes[index_a]
                    last_index_a = index_a

                last_node_b = nodes_b[index_b]
            elif exp_a < exp_b:
                last_index_a = index_a
                last_node_a = self.nodes[index_a]
            else:
                new_node = Node(nodes_b[index_b].coefficient, exp_b, index_a)
                self.nodes.append(new_node)

                if last_index_a is not None:  # is not head node
                    self.nodes[last_index_a].next_index = self.nodes.index(new_node)
                else:  # is head node
                    self.head_node.next_index = self.nodes.index(new_node)
                    last_node_a = self.head_node

                last_node_b = nodes_b[index_b]

        # there is a None at least
        if last_node_a.next_index is None and last_node_b.next_index is None:
            pass
        elif last_node_a.next_index is None:
            while last_node_b.next_index:
                index_b = last_node_b.next_index

                new_node = Node(nodes_b[index_b].coefficient, nodes_b[index_b].exponent, None)
                self.nodes.append(new_node)

                self.nodes[last_index_a].next_index = self.nodes.index(new_node)
                last_node_b = nodes_b[index_b]
        else:
            pass

        return self

    def suntract_poly(self, another_poly):
        return None

    def multiply_poly(self, another_poly):
        return None


if __name__ == '__main__':
    paras_a = [(1, 1), (2, 2), (3, 3)]
    p_a = Polynomial()
    p_a.create_poly(paras_a)
    print "poly a, len(%d):" % p_a.ploy_length()
    p_a.print_poly()

    paras_b = [(1, 1), (-2, 2), (3, 3), (4, 4)]
    p_b = Polynomial()
    p_b.create_poly(paras_b)
    print "poly b, len(%d):" % p_b.ploy_length()
    p_b.print_poly()

    p_c = p_a.add_poly(p_b)
    print "poly c, len(%d):" % p_c.ploy_length()
    p_c.print_poly()
    pass
