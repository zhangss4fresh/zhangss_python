#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/27 17:38
# @Author  : zhangss
# @Software: PyCharm
求两个正整数m和n的最大公约数和最小公倍数
"""


def max_divisor(m, n):
    if m > n:
        num_big = m
        num_small = n
    else:
        num_big = n
        num_small = m

    while num_big % num_small != 0:
        temp = num_small
        num_small = num_big % num_small
        num_big = temp

    return num_small


def min_multiple(m, n):
    maxyueshu = max_divisor(m, n)
    return m * n /maxyueshu


if __name__ == '__main__':
    yueshu = max_divisor(1515, 600)
    print yueshu

    beishu = min_multiple(1515, 600)
    print beishu
    pass
