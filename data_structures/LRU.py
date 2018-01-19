#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/10 22:30
# @Author  : zhangss
# @Software: PyCharm

缓存淘汰算法--LRU算法
http://flychao88.iteye.com/blog/1977653
"""

buffer_list = list()  # 缓存内容
buffer_size = 5  #


def get(value):
    """
    return True if value is in the buffer, false else
    :param value:
    :return:
    """
    return value in buffer_list


def set_(value):
    """
    update buffer based on the given value
    :param value:
    :return:
    """
    global buffer_list
    if value not in buffer_list:
        new_buffer = [value]

        if len(buffer_list) == buffer_size:
            new_buffer.extend(buffer_list[:buffer_size - 1])
        else:
            new_buffer.extend(buffer_list)
    else:
        index = buffer_list.index(value)
        new_buffer = list([value])
        new_buffer.extend(buffer_list[:index])
        new_buffer.extend(buffer_list[index + 1:])

    buffer_list = new_buffer
    print buffer_list


if __name__ == '__main__':
    set_(1)
    set_(2)
    set_(3)
    set_(4)
    set_(5)
    set_(6)
    print get(4), get(1)
    set_(3)
    pass
