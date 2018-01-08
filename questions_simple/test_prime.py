#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/27 18:13
# @Author  : zhangss
# @Software: PyCharm
题目：判断101-200之间有多少个素数(prime)，并输出所有素数。
"""


def discriminate(num):
    '''
    如果是素数就输出T
    :param num:
    :return:
    '''

    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

    return flag


if __name__ == '__main__':
    line = ''
    for num in range(101, 200):
        flag = discriminate(num)
        if flag:
            line += " " + str(num)
            # line += str(num) + " "
            # line = '%s %d' % (line, num)
    print line
    pass
