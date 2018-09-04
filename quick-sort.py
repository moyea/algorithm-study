#!/usr/bin/python
# coding: utf-8

"""
@desc:快速排序
@version: ??
@author: Qinghua
@contact: muyea@hotmail.com
@file: quick-sort.py
@time: 2017/11/8 11:37
"""

"""
快速排序原理
1)基线条件：数组长度为0或1时，该数组不需要排序
2)如何缩小问题的规模：从数组中取出一个基准值，
将剩余值拆分为一个小于基准值得数组和一个大于基准值得数组，
对于拆分的数组继续拆分，直至满足基线条件
最后小于基准值得数组，基准值，大于基准值合并为一个数组
"""

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        print 'left:=>', left, 'pivot:=>', pivot, 'right:=>', right
        return quickSort(left) + [pivot] + quickSort(right)


if __name__ == '__main__':
    print quickSort([10, 8, 4, 3])
