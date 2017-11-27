#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
"""

n_price = int(raw_input("input your price: "))
if 100 >= n_price >= 50:
    payment = n_price * 0.9
elif n_price > 100:
    payment = n_price * 0.8
else:
    payment = n_price
print("you should pay : %d" % payment)

if __name__ == '__main__':
    pass
