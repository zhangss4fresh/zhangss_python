#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/3 22:00
# @Author  : zhangss
# @Software: PyCharm
"""

import copy


class Node:
    def __init__(self, coef, expn, index):
        """
        :param coef: coefficient, 系数
        :param expn: exponent, 指数
        :param index: index of next node, 下一个节点在list的index
        """
        self.coef = coef
        self.expn = expn
        self.next_index = index


class Polynomial:
    def __init__(self, parameters=None):
        self.head_node = Node(None, None, None)
        self.nodes = list()

        if parameters is None or len(parameters) == 0:
            return

        self.head_node.next_index = 0
        next_index = self.head_node.next_index
        for coef, expn in parameters:
            if coef == 0:  # pass
                continue

            next_index += 1
            node = Node(coef, expn, next_index)
            self.nodes.append(node)

        # next_index of last node is None, meaning ending
        self.nodes[-1].next_index = None

    def print_poly(self, variable='x'):
        line = ''
        index = self.head_node.next_index
        while index is not None and index < len(self.nodes):
            node = self.nodes[index]
            line += ' + %d*%s^%d' % (node.coef, variable, node.expn)
            index = node.next_index
        return line.strip(' ').strip('+')

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
        while last_node_a.next_index is not None and last_node_b.next_index is not None:
            index_a = last_node_a.next_index
            index_b = last_node_b.next_index
            exp_a = self.nodes[index_a].expn
            exp_b = nodes_b[index_b].expn
            if exp_a == exp_b:
                new_coef = self.nodes[index_a].coef + nodes_b[index_b].coef
                if new_coef == 0:
                    last_node_a.next_index = self.nodes[index_a].next_index
                    if last_index_a is not None:  # is not head node
                        self.nodes[last_index_a] = last_node_a
                    else:  # todo 由于 last_node_a 是引用，这里逻辑多余了
                        self.head_node.next_index = self.nodes[index_a].next_index
                        last_node_a = self.head_node
                else:
                    self.nodes[index_a].coef = new_coef
                    last_node_a = self.nodes[index_a]
                    last_index_a = index_a

                last_node_b = nodes_b[index_b]
            elif exp_a < exp_b:
                last_index_a = index_a
                last_node_a = self.nodes[index_a]
            else:
                new_node = Node(nodes_b[index_b].coef, exp_b, index_a)
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

                new_node = Node(nodes_b[index_b].coef, nodes_b[index_b].expn, None)
                self.nodes.append(new_node)

                self.nodes[last_index_a].next_index = self.nodes.index(new_node)
                last_node_b = nodes_b[index_b]
        else:
            pass

        return self

    def subtract_poly(self, another_poly):
        another_poly = another_poly.multiply_poly(Polynomial([(-1, 0)]))
        return self.add_poly(another_poly)

    def multiply_poly(self, another_poly):
        if self.ploy_length() == 0 or another_poly.ploy_length() == 0:
            raise Exception("please check poly length")

        if another_poly.ploy_length() == 1:
            out_poly = copy.deepcopy(self)  # deep copy

            node_b = another_poly.nodes[another_poly.head_node.next_index]
            if node_b.coef == 0:
                return Polynomial()

            last_node = self.head_node
            while last_node.next_index is not None:
                index_a = last_node.next_index
                old_node = self.nodes[index_a]
                new_coef = old_node.coef * node_b.coef
                new_expn = old_node.expn + node_b.expn
                out_poly.nodes[index_a] = Node(new_coef, new_expn, old_node.next_index)

                last_node = old_node

            return out_poly

        out_poly = Polynomial()
        last_node = another_poly.head_node
        while last_node.next_index is not None:
            index_b = last_node.next_index
            node_b = another_poly.nodes[index_b]
            p_tmp = Polynomial([(node_b.coef, node_b.expn)])
            out_poly = out_poly.add_poly(self.multiply_poly(p_tmp))  # todo a.add(b)

            last_node = node_b

        return out_poly


def test_add():
    print "-------------- test add ------------------"
    p_a = Polynomial([(1, 1), (2, 2), (3, 3)])
    print "poly a, len(%d): %s" % (p_a.ploy_length(), p_a.print_poly())

    p_b = Polynomial([(1, 1), (-2, 2), (3, 3), (4, 4)])
    print "poly b, len(%d): %s" % (p_b.ploy_length(), p_b.print_poly())

    p_c = p_a.add_poly(p_b)
    print "poly a+b, len(%d): %s" % (p_c.ploy_length(), p_c.print_poly())

    p_c = p_a.add_poly(Polynomial())
    print "poly a+0, len(%d): %s" % (p_c.ploy_length(), p_c.print_poly())


def test_subtract():
    print "-------------- test subtract ------------------"
    p_a = Polynomial([(1, 1), (2, 2), (3, 3), (0, 4)])
    print "poly a, len(%d): %s" % (p_a.ploy_length(), p_a.print_poly())

    p_b = Polynomial([(1, 1), (-2, 2), (3, 3), (4, 4)])
    print "poly b, len(%d): %s" % (p_b.ploy_length(), p_b.print_poly())

    p_c = p_a.subtract_poly(p_b)
    print "poly a-b, len(%d): %s" % (p_c.ploy_length(), p_c.print_poly())


def test_multiply():
    print "-------------- test multiply ------------------"
    p_a = Polynomial([(1, 1), (2, 2), (3, 3)])
    print "poly a, len(%d): %s" % (p_a.ploy_length(), p_a.print_poly(variable='y'))

    p_d = Polynomial([(1, 1), (2, 2)])
    print "poly d, len(%d): %s" % (p_d.ploy_length(), p_d.print_poly(variable='y'))

    p_e = p_a.multiply_poly(p_d)
    print "poly a*d, len(%d): %s" % (p_e.ploy_length(), p_e.print_poly(variable='y'))


if __name__ == '__main__':
    test_add()
    test_subtract()
    test_multiply()
    pass
