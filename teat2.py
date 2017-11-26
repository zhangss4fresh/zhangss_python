#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = xiaofei.ding
@time: 2017-1126 23:42

公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买一百只鸡,其中公鸡，母鸡，小鸡都必须要有，
问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱。
"""


if __name__ == '__main__':
    t = 1
    x, y, z = 1, 1, 3*t
    xx = 5*x
    yy = 3*y
    zz = t
    # i, j ,k = 1, 1, 1
    while x>0 and y>0 and z>0:
        if x+y+z==100 and xx+yy+zz==100:
            print x,y,z
    # i+=1
    # j+=1
    # k+=1
    pass
