#!/usr/bin/python
# coding: utf-8

"""
@desc:图
@version: ??
@author: Qinghua
@contact: muyea@hotmail.com
@file: graph.py
@time: 2017/11/8 15:36
"""
from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['peggy', 'anuj']
graph['claire'] = ['thom', 'jonny']
graph['peggy'] = []
graph['anuj'] = []
graph['thom'] = []
graph['jonny'] = []


def person_is_seller(name):
    """
    判断给定name是否为一个mongo经销商
    :param name:
    :return:
    """
    return name[-1] == 'm'


def find_mongo_seller():
    # 创建一个搜索队列
    search_deque = deque()
    # 将自己的朋友加入队列
    search_deque += graph['you']
    # 当队列不为空时，就一直执行查找操作
    while search_deque:
        print search_deque
        # 出队,从自己朋友队列中取出一个
        person = search_deque.popleft()
        # 查找的人是否为一个mango经销商
        if person_is_seller(person):
            print '%s is a mango seller' % person
            return True
        else:
            # 入队，将朋友的朋友加入搜索队列
            search_deque += graph[person]
    return False


"""
执行find_mongo_seller()
1->deque(['alice', 'bob', 'claire'])
2->deque(['bob', 'claire', 'peggy'])
3->deque(['claire', 'peggy', 'peggy', 'anuj'])
4->deque(['peggy', 'peggy', 'anuj', 'thom', 'jonny'])
5->deque(['peggy', 'anuj', 'thom', 'jonny'])
6->deque(['anuj', 'thom', 'jonny'])
7->deque(['thom', 'jonny'])
8->thom is a mango seller

---对于第3步，可以看到peggy在队列中出现了两次
"""


def search_mongo_seller(name):
    search_deque = deque()
    search_deque += graph[name]
    # 存储检查过的人
    searched_person = []
    while search_deque:
        print search_deque
        person = search_deque.popleft()
        # 当该人没检查过时才进行检查
        if person not in searched_person:
            if person_is_seller(person):
                print '%s is a mango seller'
                return True
            else:
                search_deque += graph[person]
                # 将该人标记为检查过
                searched_person.append(person)
    return False


if __name__ == '__main__':
    find_mongo_seller()
    print '*' * 20
    search_mongo_seller('you')
