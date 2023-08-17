#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/17 16:56
# @Author  : lemondyoung
# @File    : widget.py
# @Description: 工具类

try:
    import pypinyin
except Exception as e:
    is_check_homophone = False
else:
    is_check_homophone = True

# 限制参数的接受值，在指定列表范围内
def only_accept_specific_values(allow_values_dict):
    """
    :param allow_values_dict: {0: ['a','b'], 1: [4, 5]}，key代表参数的index位置
    :return:
    """
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            for i, value in enumerate(args):
                if value is None or not allow_values_dict.get(i):
                    continue
                elif value not in allow_values_dict[i]:
                    print(f'{value}参数值不在{allow_values_dict[i]}范围内')
                    return None
            for i, (key, value) in enumerate(kwargs.items()):
                if value is None or not allow_values_dict.get(i):
                    continue
                elif value not in allow_values_dict[i]:
                    print(f'{value}参数值不在参数{key}的{allow_values_dict[i]}范围内')
                    return None
            return func(*args, **kwargs)
        return wrapper
    return out_wrapper


def filter_list(data_list, rules=['repetition', 'homophone']):
    """
    过滤列表
    :param data_list:
    :param rules: 规则，repetition：去重，homophone：去除相邻谐音
    :return:
    """
    if 'repetition' in rules:
        data_list = list(set(data_list))
    if 'homophone' in rules and is_check_homophone:
        # 浅拷贝一个列表，如果相邻两个字谐音，就从原来的列表里移除该item
        new_list = data_list.copy()
        for item in new_list:
            is_homophone = False
            pinyin_list = pypinyin.lazy_pinyin(item)
            for index in range(len(pinyin_list)):
                sub_list = pinyin_list[index: index + 2]
                if len(sub_list) == 2 and sub_list[0] == sub_list[1]:
                    is_homophone = True
                    break
            if is_homophone:
                data_list.remove(item)
    elif 'homophone' in rules and not is_check_homophone:
        print('地名列表筛选：未安装pypinyin包，跳过谐音去重')
    return data_list


# 测试
print(filter_list(data_list=['杨公园', '杨公园', '杨洋公园']))




