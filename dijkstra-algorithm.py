#!/usr/bin/python
# coding: utf-8

"""
@desc:迪克斯特拉算法
@version: ??
@author: Qinghua
@contact: muyea@hotmail.com
@file: dijkstra-algorithm.py
@time: 2017/11/8 16:30
"""
"""
start -- 6 --> a -- 1 --> end
   \           
    \ -- 2 --> b -- 5 --> end
                \
                 \-- 3 --> a
"""
graph = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'end': 1
    },
    'b': {
        'end': 5,
        'a': 3
    },
    'end': {}
}

# 迪克斯特拉算法用于在权重为正的加权图中寻找最短路径
# 广度优先算法用于在非加权图中查找最短路径
# 贝尔曼-福德算法用于包含权重为负的加权图

# 无穷大
infinity = float('inf')
# 从起点到该节点的开销
costs = {
    'a': 6,
    'b': 2,
    'end': infinity
}
# 存储父节点
parents = {
    'a': 'start',
    'b': 'start',
    'end': None
}
# 存储处理过的节点
processed = []


def find_smallest_cost_node(costs):
    """
    找到最小开销的节点
    :param costs:
    :return:
    """
    smallest_cost = float('inf')
    smallest_node = None
    for node in costs:
        cost = costs[node]
        if cost < smallest_cost and node not in processed:
            smallest_node = node
            smallest_cost = cost
    return smallest_node


node = find_smallest_cost_node(costs)
while node is not None:
    # 到达最近节点的开销
    cost = costs[node]
    # 最近节点的邻近节点
    neighbors = graph[node]
    # 遍历最小开销节点的邻近节点
    for n in neighbors.keys():
        # 经由最近节点到达节点n的开销
        new_cost = cost + neighbors[n]
        # 原来到达节点n的开销 > 经最近节点到达n的开销
        if costs[n] > new_cost:
            # 更新到达节点n开销
            costs[n] = new_cost
            # 更新节点n的父节点为最近节点
            parents[n] = node
    # 将最近节点标记为已处理
    processed.append(node)
    # 找到node下更小开销的节点
    node = find_smallest_cost_node(costs)

print costs['end']
