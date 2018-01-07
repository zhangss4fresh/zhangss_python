#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/7 20:17
# @Author  : zhangss
# @Software: PyCharm
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnOrderList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

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
        while current is not None:
            if current.data == data:
                return True
            current = current.next

        return False

    def insert(self, pos, data):
        assert pos >= 0
        if pos >= self.size():
            raise Exception("pos:%d is out of index:%d" % (pos, self.size()-1))

        last = None
        current = self.head
        count = -1
        while current is not None:
            count += 1
            if count == pos:
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
    list_ = UnOrderList()
    list_.add(0)
    list_.add(1)
    list_.add(2)

    list_.print_list()
    print list_.is_empty()
    print list_.size()
    print list_.search(2)
    print list_.index(0)

    list_.print_list()
    list_.insert(2, -1)
    list_.print_list()

    list_.pop()
    list_.print_list()

    list_.remove(1)
    list_.print_list()
