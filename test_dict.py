#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/27 19:14
# @Author  : zhangss
# @Software: PyCharm
题目：输入某年某月某日，判断这一天是这一年的第几天？
"""


def parse(time_str_):
    if len(time_str_) != 10:
        print "please check length of input!"
        exit(0)

    year_ = int(time_str_[0:4])
    month_ = int(time_str_[5:7])
    day_ = int(time_str_[8:10])
    return year_, month_, day_


def is_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    time_str = raw_input("please input the time")
    year, month, day = parse(time_str)

    month_dict = dict()
    for i in range(1, 13):
        if i in {1, 3, 5, 7, 8, 10, 12}:
            month_dict[i] = 31
        elif i == 2:
            month_dict[i] = 28
        else:
            month_dict[i] = 30
    if is_leap(year):
        month_dict[2] = 29

    if 13 > month > 0:
        pass
    else:
        print "please check month!"
        exit(0)

    if day in range(1, month_dict[month]+1):
        pass
    else:
        print "please check day!"
        exit(0)

    days = day
    for i in range(1, month):
        days += month_dict[i]

    print "您输入的时间是这一年的第%d天" % days
    print "您输入的时间是这一年的第", days, "天"
    pass
