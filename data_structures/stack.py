#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/8 22:59
# @Author  : zhangss
# @Software: PyCharm
"""


class Stack:
    def __init__(self):
        self.data = list()
        self.size = 0

    def push(self, data):
        self.size += 1
        self.data.append(data)

    def pop(self):
        self.data.pop()

    def peek(self):
        return self.data[self.size - 1]

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def show(self):
        print self.data


if __name__ == '__main__':
    stack = Stack()
    stack.push(0)
    stack.push(2)
    stack.push(4)
    stack.push('a')
    stack.push('b')
    stack.push('c')

    stack.show()
    print stack.is_empty()
    print stack.peek()
    print stack.get_size()
    print stack.pop()
    print stack.get_size()
    pass
