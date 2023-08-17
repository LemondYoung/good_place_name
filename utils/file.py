#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/17 16:57
# @Author  : lemondyoung
# @File    : file.py
# @Description:


import csv
import json
import logging
import os, re
import tarfile
import time, datetime


# 文件基类
from config import RESULT_PATH


class File(object):
    """
    1、获取、判断文件类型
    2、打开文件(excel)
    3、保存文件
    """
    def __new__(cls, file_path=None):
        if not os.path.isfile(file_path):  # 跳过非文件对象
            logging.warning('%s非文件对象', file_path)
            return False
        else:
            return object.__new__(cls)

    def __init__(self, file_path=None):
        self.file_path = file_path
        self.path, self.file = os.path.split(file_path)
        self.file_type = self.file.split('.')[-1]
        self.file_name = self.file.replace(self.file_type, '')[0:-1]
        self.file_type_map = {
            'xlsx': 'xls',
            'xls': 'xls',
            'docx': 'doc',
            'doc': 'doc',
            'txt': 'txt',
            'tar.gz': 'tar.gz',
            'tar': 'tar',
            'sql': 'sql',
        }
        self.std_file_type = None

    def get_file_info(self, return_type=None):
        """
        判断文件类型，并标准化
        :param expect_file_type: 如果期望文件类型为空，则默认通过字典中所有文件类型
        :return:
        """
        file_info = {}
        logging.debug('获取文件类型')
        new_type = self.file_type_map.get(self.file_type)
        if not new_type:
            logging.error('%s文件类型错误！所有文件类型：%s', type, str(self.file_type_map.keys()))
            return False
        else:
            self.std_file_type = new_type
            file_info['file_type'] = new_type

        logging.debug('获取文件大小')
        info = os.stat(self.file_path)
        file_size = round(info.st_size / 1024, 4)
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info.st_ctime))
        modify_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info.st_mtime))
        file_info['file_size'] = file_size
        file_info['create_time'] = datetime.datetime.strptime(create_time, "%Y-%m-%d %H:%M:%S")
        file_info['modify_time'] = datetime.datetime.strptime(modify_time, "%Y-%m-%d %H:%M:%S")
        file_info['file_name'] = self.file_name

        if return_type == 'file_type':
            return file_info['file_type']
        elif return_type == 'file_size':
            return file_info['file_size']
        else:
            return file_info

    def is_expect_file_type(self, expect_file_type=None):
        if expect_file_type == 'xls':
            if self.file_type not in ['xlsx', 'xlsm', 'xls']:
                return False
        elif expect_file_type == 'csv':
            if self.file_type not in ['csv']:
                return False
        elif expect_file_type == 'json':
            if self.file_type not in ['json']:
                return False
        elif expect_file_type == 'doc':
            if self.file_type not in ['docx', 'doc']:
                return False
        elif expect_file_type == 'txt':
            if self.file_type not in ['txt']:
                return False
        else:
            logging.error('期望文件格式错误')
            return False
        return True

    def read_txt_data(self, num_per_line=None):
        """
        读取并解析txt文档测试数据
        :param file_name:
        :param num_per_line: 每行数据个数
        :return:
        """
        with open(self.file_path, encoding='utf-8') as file_object:
            lines = file_object.readlines()  # 读取每一行存在一个列表中

        data_string = []
        for line in lines:
            data_line = line.strip("\n").split()  # 去除首尾换行符，并按空格划分
            if num_per_line and len(data_line) != num_per_line:  # if data_line == []:
                continue
            else:
                data_string.append(data_line)
        data = []
        for i in range(len(data_string)):
            if len(data_string[i]) == 1:  # 每行只有一个
                data.append(data_string[i][0])
            else:
                for j in range(len(data_string[i])):
                    data[i][j] = float(data_string[i][j])
        return data

    @staticmethod
    def save_txt(data, file='new.txt', word_wrap=True):
        """
        保存数据都到文件
        :param data:
        :param file_name:
        :param word_wrap: 是否换行
        :return:
        """
        file_path = os.path.join(RESULT_PATH, file)
        with open(file_path, 'w', encoding='utf-8') as f:
            if word_wrap:
                [f.write(str(item)+'\n') for item in data]
            else:
                f.write(str(data))
        return None

    def save_json(self, data):
        """保存数据为json文件"""
        expect_result = self.is_expect_file_type(expect_file_type='json')
        if expect_result is False:
            logging.error('文件格式错误')
            return False
        try:
            b = json.dumps(data, ensure_ascii=False, indent=4)
            f2 = open(self.file_path, mode='w', encoding="utf-8")
            f2.write(b)
            f2.close()
            return True
        except Exception as e:
            logging.error('保存json文件错误, %s', e)
            return False


if __name__ == '__main__':
    data = File(file_path=r'D:\app\pycharm\project\tools\good_place_name\result\result.txt').get_file_info()
    print(data)

