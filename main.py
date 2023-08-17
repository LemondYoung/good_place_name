
from constants import *
import random

from utils.file import File
from utils.widget import only_accept_specific_values, filter_list

# 地名三部分组成：adj_part(形容词部分) + stuff_part(物体部分) + place_part(地方部分)
# 以下预设三部分的可选列表范围
adj_part_list = [nature_color, derivative_color, plant_color, stuff_color, climate_adj, fruit_color,]
stuff_part_list = [climate_stuff, animal_stuff, culture_stuff]
place_part_list = [site_place]


# 预设一些主题（更好听一些）
theme_list = {
    'fruit_animal': [fruit_color, animal_stuff],  # 水果动物主题，比如桃马公园，栗鼠公园，芒鸟公园
    'plant_animal': [plant_color, animal_stuff],  # 植物动物主题，比如茶马乐园，竹鼠乐园，瑰鱼乐园，麦龙乐园
    'climate': [climate_adj, climate_stuff],  # 天气主题，比如清风广场，碧云广场，熏风广场，密云广场
    'climate_scene': [climate_adj, culture_stuff],  # 天气+文化主题，比如弥音社区，朗琴社区，翠棋社区，漫梦社区
    'random': [sum(adj_part_list, []), sum(stuff_part_list, [])],
}

accept_theme_list = list(theme_list.keys())


# 生成一个地名
@only_accept_specific_values({0: accept_theme_list})
def generate_place_name(theme=None, place=None):
    """
    生成一个地名
    :param theme: 主题：从accept_theme_list中选，可以为空
    :param place: 地方名：比如公园、广场、市
    :return:
    """
    if not theme_list.get(theme):
        adj_part = sum(adj_part_list, [])
        stuff_part = sum(stuff_part_list, [])
    else:
        adj_part = theme_list.get(theme)[0]
        stuff_part = theme_list.get(theme)[1]

    if not place:  # 包含空串
        place = random.choice(site_place)

    place_name = random.choice(adj_part) + random.choice(stuff_part) + place
    return place_name


# 批量生成地名
@only_accept_specific_values({0: accept_theme_list})
def batch_generate_name(theme='random', place='random', count=10):
    """
    :param theme: 主题：从accept_theme_list中选，可以为空
    :param place: 地方名：比如公园、广场、市
    :param count:
    :return:
    """
    theme_str = theme or '随机'
    place_str = place or '地名'
    print(f'需要生成{count}个{theme_str}主题的{place_str}')
    name_list = [generate_place_name(theme, place) for i in range(count)]
    name_list = filter_list(name_list, rules=['repetition', 'homophone'])  # 列表去重（去除重复词，谐音字）
    print(f"{theme_str}主题的{len(name_list)}个地名:", name_list)

    File.save_txt(name_list, file='result.txt')
    return name_list


# 1. 基本功能：能指定主题生成地名列表
# 2. 添加随机功能
# 3. 外部参数限制指定列表输入
# 4. 列表去重
# 5. 文件保存


if __name__ == '__main__':
    # 根据主题生成并打印随机地名
    selected_theme = 'fruit_animal'  # 在这里选择主题，请从accept_theme_list列表中选择，如果None代表随机
    place = '公园'  # 如果空代表随机
    result = batch_generate_name(theme=selected_theme, place=place, count=20)

