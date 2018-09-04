#!/usr/bin/python
# coding: utf-8

"""
@desc: D&C算法 利用递归求数组的和
@version: ??
@author: Qinghua
@contact: muyea@hotmail.com
@file: d&c.py
@time: 2017/11/8 10:47
"""


# D&C工作原理(D&C并非可用于解决问题的算法，只是一种解决思路)：
# 1)找出简单的基线条件
# 2)确定如何缩小问题的规模，使其符合基线条件


def dSum(arr):
    """
    使用递归对一个数组求和
    思路:
    1)找出基线条件，什么是最简单的数组?当数组没有数据或者只有一个数据n,那么该数组的和为0或n
    2)缩小问题的规模，将数组中元素逐渐减少，使其符合基线条件
    对于dSum([2,4,6]) = 2+dSum([4,6]) = 2+4+dSum([4])
    所以dSum工作原理为，接收一个数组，若数组元素个数为0，返回0，
    否则返回第一个元素与剩余元素之和，再返回结果
    :param arr:
    :return:
    """
    if len(arr) == 0:
        return 0
    else:
        return arr.pop() + dSum(arr)


def dCount(arr):
    # if len(arr) == 1:
        # return 1
    if arr == []:
        return 0
    else:
        arr.pop()
        return 1 + dCount(arr)


def dMax(arr):
    if len(arr) == 0:
        return 0
    else:
        max = arr.pop()
        m = dMax(arr)
        if max > m:
            return max
        else:
            return m


if __name__ == '__main__':
    print dSum([2, 3, 4, 6])
    print dCount([2, 3, 4, 5, 6, 7])
    print dMax([2, 9, 4, 8, 6, 7])
