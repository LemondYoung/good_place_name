好地名（good_place_name）
===

# 介绍
最近在玩都市天际线时每次新拉一条道路、区域，都会分配一个默认名称，区域还好，有英文翻译过来的（摩尔公园，维多利亚公园等），也有顺口点的（秋日山、棕土公园），但道路的命名就一言难尽了，像奶奶街、孙街郑街、前男友街...强迫症决不允许这么难听的名字，所以想尽量自己命名一些比较符合游戏场景的地名。

但要涉及到大量命名的时候，脑洞有点不够用了，参考过一些常见的命名法则（可以参考知乎类似问题）：方位命名法（山东、山西、临沂、济南）、地貌命名法（双鸭山、金沙江）、历史命名法（兰陵、琅琊）等等，但都适用于单个命名，如果要大量的类似地名的就不够用了，比如我想某个区域都用水果命名（甜石榴公园、荔枝公园、番茄社区）、或者动物命名（御猫公园、奈马公园、桃马公园），可以让整个区域名称的规划更加系统和有趣

市场上好多命名器，都是小说专供的，不太符合我的审美要求，所以顺便练手写了这个地名的小工具，目前根据一些动物、植物、颜色生成的，后续会逐步扩展更多的主题

# 功能
## 内容
该项目的地名三部分由组成：adj_part(形容词部分) + stuff_part(物体部分) + place_part(地方部分)，根据不同的主题，拼配不同的形容词和名词，预设了一些比较不错的主题，具体如下，其他名词可以参考constants.py
* fruit_animal： 水果动物主题，比如桃马公园，栗鼠公园，芒鸟公园
* plant_animal：  植物动物主题，比如茶马乐园，竹鼠乐园，瑰鱼乐园，麦龙乐园
* climate： 天气主题，比如清风广场，碧云广场，熏风广场，密云广
* climate_scene： 天气+文化主题，比如弥音社区，朗琴社区，翠棋社区，漫梦社区
* random：随机主题
## 实现的功能
* 基本功能：能指定主题生成地名列表，或者随机生成
* 指定规则地名去重（重复地名、谐音地名）
* 地名文件保存到本地


# 运行
环境python3.7
1. 检查python环境和pip包
```
pip install -r requirements.txt
```
注：目前仅依赖pypinyin三方包，主要是检查相邻的谐音字，做了兼容处理，不安装也不影响

2. 执行`python main.py`运行程序
主要运行batch_generate_name批量生成函数
* 参数1：theme，可以指定主题，为空就是随机
* 参数2：place，地名后缀
* 参数3：count，生成个数

3. 看输出日志，或者保存的本地文件result.txt


--- 
Create By LemondYoung