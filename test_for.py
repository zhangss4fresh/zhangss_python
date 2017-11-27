#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = xiaofei.ding
@time: 2017-1126 23:42

公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买一百只鸡,其中公鸡，母鸡，小鸡都必须要有，
问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱。
"""
import time
start = time.clock()


if __name__ == '__main__':
    # t = 1
    # x, y, z = 1, 1, 1

    # i, j ,k = 1, 1, 1
    for x in range(1, 20):
        for y in range(1, 34):
            for z in range(3, 100, 3):
                xx = 5 * x
                yy = 3 * y
                zz = z / 3
                if x + y + z == 100 and xx + yy + zz == 100:
                    print x, y, z
                    continue
                else:
                    pass
                    # print 'no'
                    # pass
end = time.clock()
print(end - start)
