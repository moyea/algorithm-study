#!/usr/bin/python
# coding: utf-8

"""
@desc:简单排序
@version: ??
@author: Qinghua
@contact: muyea@hotmail.com
@file: simple-sort.py
@time: 2017/11/7 20:50
"""


def smallest(arr):
    smallestIdx = 0
    smallest = arr[smallestIdx]
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallestIdx = i
    return smallestIdx


def simpleSort(arr):
    newArr = []
    for i in range(0, len(arr)):
        small = smallest(arr)
        newArr.append(arr.pop(small))
    return newArr


if __name__ == '__main__':
    print simpleSort([5, 6, 7, 4, 3, 2])
