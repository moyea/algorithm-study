#!/usr/bin/python
# coding: utf-8

"""
@desc:动态规划解决背包问题
@version: ??
@author: Qinghua
@contact: muyea@hotmail.com
@file: dp.py
@time: 2017/11/9 11:52
"""
"""
物品信息\背包         1	    2	    3	    4
G吉他$1500/1磅 	    1500G	1500G	1500G	1500G
S音响$3000/4磅	    1500G	1500G	1500G	3000S
C笔记本电脑$2000/3磅	1500G	1500G	2000C	3500GC
M iphone $2000/1磅	2000M	3500GM	3500GM	4000CM
Mp3 $1000/1磅	    2000M	3500GM	4500GMP	4500GMP
"""


# 可拿取的所有产品信息
products = {
    'guitar': {
        'weight': 1,
        'worth': 1500
    },
    'sound': {
        'weight': 4,
        'worth': 3000
    },
    'laptop': {
        'weight': 3,
        'worth': 2000
    },
    'iphone': {
        'weight': 1,
        'worth': 2000
    },
    'mp3': {
        'weight': 1,
        'worth': 1000
    },
    'watch': {
        'weight': 1,
        'worth': 1500
    }
}
# 所有产品的重量信息
weights = [product['weight'] for key, product in products.items()]
# 背包总容量
total_bag_weight = 4
# 最小规划单位(最小背包容量)
min_weight = min(weights)
# 背包容量信息(根据最小背包容量及背包总容量生成一系列背包)
bags_weight_info = range(min_weight, total_bag_weight / min_weight + min_weight, min_weight)
# 规划的背包里存放的最值钱的产品
bags_info = []


def get_bag_item_info(bag):
    """
    获取指定背包的总重量及总价值
    :param bag:
    :return:
    """
    total_weight = 0
    total_worth = 0
    for i, p in bag.items():
        total_weight += p['weight']
        total_worth += p['worth']
    return total_weight, total_worth


def get_bag_by_space(space):
    """
    根据给定的空间，返回该空间大小的背包的位置及背包信息
    :param space:
    :return:
    """
    weight = int(space)
    idx = bags_weight_info.index(weight)
    return idx, bags_info[idx]


from copy import copy

# 用不同的产品填充背包
for idx, bag_weight in enumerate(bags_weight_info):
    tmp = {}
    for k, p in products.items():
        current_product_weight = p['weight']
        current_product_worth = p['worth']
        item_total_weight, item_total_worth = get_bag_item_info(tmp)
        if current_product_weight > bag_weight:
            continue
        if current_product_weight <= bag_weight - item_total_weight:
            tmp[k] = p
        else:
            extra_space = bag_weight - current_product_weight
            if extra_space == 0:
                if current_product_worth > item_total_worth:
                    tmp.clear()
                    tmp[k] = p
            else:
                index, bag = get_bag_by_space(extra_space)

                if k in bag.keys():
                    new_bag = copy(bag)
                    del new_bag[k]
                    wei, wor = get_bag_item_info(new_bag)
                    if current_product_worth + wor > item_total_worth:
                        tmp = copy(new_bag)
                        tmp[k] = p
                else:
                    wei, wor = get_bag_item_info(bag)
                    if current_product_worth + wor > item_total_worth:
                        tmp = copy(bag)
                        tmp[k] = p
    bags_info.append(tmp)

for idx, bag_weight in enumerate(bags_weight_info):
    print bag_weight, bags_info[idx]
