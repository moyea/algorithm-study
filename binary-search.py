#!/usr/bin/python
# coding: utf-8

"""
@desc:二分法查找
@version: ??
@author: Qinghua
@contact: muyea@hotmail.com
@file: binary-search.py
@time: 2017/11/7 17:33
"""

term = 56789
arr = range(1, 240001)
low = 0
high = len(arr) - 1
count = 0
while low <= high:
    count += 1
    mid = (low + high) / 2
    guess = arr[mid]
    print '第%d次,guess:%d,low:%d,high:%d' % (count, guess, low, high)
    if guess == term:
        break
    if guess > term:
        high = mid - 1
    else:
        low = mid + 1
