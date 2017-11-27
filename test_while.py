#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = xiaofei.ding
@time: 2017-1126 22:59
"""


def fun1():
    var1 = (43, 'abc', [54, 'edf'], {'one': 78, 2: 0.5, 'first': 300l, '1': 'dd', 1: '44', 'a': 78})
    print var1[3], type(var1[3])


count = 0
while count < 9:
    print 'The count is:', count
    count = count + 1

print "Good bye!"

if __name__ == '__main__':
    # fun1()
    # print int('3')
    # print ord('A')
    pass
