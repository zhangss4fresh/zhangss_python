#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/27 22:47
# @Author  : zhangss
# @Software: PyCharm
These are some frequently used functions:
zip max min range pow round abs divmod enumerate filter lambda map raw_input
"""

print max([2, 3, 42, 3, 4, ])
print min([2, 3, 42, 3, 4, ])
print range(3, 12, 3)
print abs(-3)
print pow(4, 3)  # 4的3次方
# print raw_input("input:")
print divmod(5, 2)
print round(number=4.391, ndigits=1)  # 精确到小数点后哪一位

list_ = [1, 2, 3, 4]
# for i in range(len(list_)):
#     print i
# for i in list_:
#     print i
# for i, value in enumerate(list_):
#     print i, value

list_2 = ['a', 'b', 'c']
zip_ = zip(list_, list_2)
print zip_, zip_[2][1]

fun1 = lambda x: pow(x, 3)
print fun1(2)

print filter(lambda x: x % 3 == 0, range(1, 11))

print map(lambda x: x % 5, range(25, 36))

print reduce(lambda x, y: x+y, range(1, 4))

if __name__ == '__main__':
    pass
