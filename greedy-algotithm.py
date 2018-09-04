#!/usr/bin/python
# coding: utf-8

"""
@desc:贪婪算法
@version: ??
@author: Qinghua
@contact: muyea@hotmail.com
@file: greedy-algotithm.py
@time: 2017/11/9 10:22
"""
# 需要覆盖的州
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

# 广播台清单，key为广播台名称，键为广播台覆盖的州
sections = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}

# 最终选择的电台
selected_sections = set()


def find_largest_section():
    largest_section = None
    largest_covered = None
    for sec in sections:
        # 覆盖的州
        covered = sections[sec] & states_needed
        if len(covered) < 1:
            continue
        if largest_section == None or len(largest_covered) < len(covered):
            largest_section = sec
            largest_covered = covered
    return largest_section, largest_covered


section, union = find_largest_section()
while section != None:
    selected_sections.add(section)
    # 从需要的集合中去除在另一个集合出现的元素
    states_needed = states_needed - union
    section, union = find_largest_section()

print selected_sections
