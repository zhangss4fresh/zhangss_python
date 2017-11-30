#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/27 23:36
# @Author  : zhangss
# @Software: PyCharm
"""

str_ = 'Sdknn84u*_-cd '
print str.count(str_, 'n'), str_.count('n')
print str_.find('x')  # 返回第一个位置的下标,如果找不到就返回-1
print str_.replace('n', 'N')
print str_.split('_')
print str_.join(['j', 'k'])
print str_.strip()  # remove the sign at start and ending
print str_.startswith('fff')
print str_.endswith('cd ')

print str.isalpha('djd3j')
print str.isalnum('424324e')
print str.islower('dsfSds')
print str_