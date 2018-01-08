#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/8 22:40
# @Author  : zhangss
# @Software: PyCharm
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OrderList:   # ascending
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.size() == 0:
            self.head = Node(data)
            return

        last = None
        current = self.head
        while current is not None:
            if data < current.data:
                node = Node(data)

                if last is None:
                    node.next = self.head
                    self.head = node
                else:
                    node.next = current
                    last.next = node

                return

            last = current
            current = current.next

        node = Node(data)
        last.next = node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def is_empty(self):
        return self.head is None

    def search(self, data):
        current = self.head
        while current is not None and data >= current.data:
            if current.data == data:
                return True
            current = current.next

        return False

    def pop(self, index=None):
        if index and (index < 0 or index >= self.size() or self.size() <= 0):
            raise Exception("error when pop index:%d list size:%d" % (index, self.size()))

        last = None
        current = self.head
        count = -1
        if index is None:  # remove the last one
            while current is not None:
                if current.next is None:
                    last.next = None
                    return
                last = current
                current = current.next
        else:
            while current is not None:
                count += 1
                if index == count:
                    if last is None:  # head node
                        self.head = current.next
                    else:
                        last.next = current.next
                    return

                last = current
                current = current.next

    def remove(self, data):
        last = None
        current = self.head
        while current is not None:
            if current.data == data:
                if last is None:  # head node
                    self.head = current.data.next
                else:
                    last.next = current.next
                return

            last = current
            current = current.next

    def index(self, data):
        current = self.head
        count = -1
        while current is not None:
            count += 1
            if current.data == data:
                return count
            current = current.next

        return count

    def print_list(self):
        out = list()
        current = self.head
        while current is not None:
            out.append(current.data)
            current = current.next

        print out


if __name__ == '__main__':
    order_list = OrderList()
    order_list.add(0)
    order_list.add(1)
    order_list.add(2)

    order_list.print_list()
    print order_list.is_empty()
    print order_list.size()
    print order_list.search(2)
    print order_list.index(0)

    order_list.pop()
    order_list.print_list()

    order_list.remove(1)
    order_list.print_list()
