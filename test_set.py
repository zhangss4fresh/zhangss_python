#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/27 20:22
# @Author  : zhangss
# @Software: PyCharm
题目：有1、2、3、4、5  五个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""

if __name__ == '__main__':
    set_num = set()
    set_ = {1, 2, 3, 4, 5}
    for i in set_:
        for j in set_ - {i}:
            for k in set_ - {i, j}:
                num = 100 * i + 10 * j + k
                set_num.add(num)
    print "The count of nums is :", len(set_num)
    print set_num
