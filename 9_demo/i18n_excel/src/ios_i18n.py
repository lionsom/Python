import time  # 引入time模块
import xlrd

import os;
import re;
from collections import Counter
import shutil

from StringsFileUtil import StringsFileUtil

# 初始国际化表
origin_excel_Path = '/Users/qiyeyun/Desktop/i18n_excel/多语言词条ALL.xls'

# excel具体参数
origin_excel_WordBarCode = {'name': 'WordBarCode', 'col_index': 7 }  # 词条码， 第7列
origin_excel_rows = [
                     {'name': 'en-US', 'col_index': 10 },       # 英文，第10行
                     {'name': 'ja-JP', 'col_index': 11 },       # 日文
                     {'name': 'ms-MY', 'col_index': 12 },       # 马来文
                     {'name': 'ko-KR', 'col_index': 13 },       # 韩文
                     {'name': 'hi-IN', 'col_index': 14 },       # 印地语
                     {'name': 'id-ID', 'col_index': 15 },       # 印度尼西亚语
                     {'name': 'th-TH', 'col_index': 16 },       # 泰语
                     {'name': 'vi-VN', 'col_index': 17 },       # 越南语
                     {'name': 'ta-IN', 'col_index': 18 },       # 泰米尔语
                     {'name': 'my_mm', 'col_index': 19 },       # 缅甸语
                     ]


# 打印当前时间
def printCurrentTime():
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 格式化成2016-03-20 11:45:39形式
    print('当前时间：' + currentTime)

# 读取Excel文件
def readExcel(excelPath):
    workbook = xlrd.open_workbook(excelPath)
    # print(workbook)

    sheet1 = workbook.sheet_by_index(0) # 获取第一个工作表
    # print('工作表共有' + str(sheet1.ncols) + '列') # 获取工作表有效列数

    # 获取词条码数组
    allCodes = sheet1.col_values(origin_excel_WordBarCode['col_index'])

    # 数据源
    allDict = {}
    # 遍历获取指定列的数据
    for value in origin_excel_rows:
        # print(value['name'], value['col_index']) 
        allValues = sheet1.col_values(value['col_index']) # 该列单元格对象组成的列表       
        allDict[value['name']] = allValues
    
    return (allCodes, allDict)

# 读取.Strings文件内容
def readStringsFile(strings_file_path):
    (keys, values) = StringsFileUtil.getKeysAndValues(strings_file_path)
    # print(keys, values)
    return keys

def main():
    printCurrentTime()

    # 读取原始Excel
    (allCodes, dataSources) = readExcel(origin_excel_Path)
    # enUSArr = dataSources['en-US']
    # jaJPArr = dataSources['ja-JP']

    # 获取中文strings中的keys
    module_path = os.path.dirname(__file__)
    filepath = module_path + '/pods_i18n'

    # 遍历所有模块，并在模块中新建对应语言的文件夹，新建文件夹

    dirlist = os.listdir(filepath)
    for dir in dirlist:
        # 过滤掉.DS_Store
        if dir.startswith('.'):
            continue
        # print(dir)

        # 遍历每个模块中的每个语言文件夹
        lporjpath = filepath + '/' + dir
        lporjlist = os.listdir(lporjpath)
        # print(lporjlist)
        for lporjdir in lporjlist:
            # 中文的模块文件夹不删除，其他都删除
            if lporjdir.startswith('zh-Hans') or lporjdir.startswith('.'): 
                # print('zh-Hans .DS_Store文件夹不删除')
                continue
            # 其他文件夹都删除
            removePath = lporjpath + '/' + lporjdir
            # os.remove(removePath)       # 删除文件
            # os.rmdir(removePath)        # 删除空文件夹
            shutil.rmtree(removePath)   # 递归删除文件夹，即：删除非空文件夹

        # 新语言
        for value in origin_excel_rows:
            # 哪一种语言
            name = value['name']

            # 再根据语言创建对应的文件夹
            newPath = lporjpath + '/' + name + '.lproj'
            os.makedirs(newPath) 
            # print(newPath)

            # 再创建对应的.string
            newfilePath = newPath + '/' + dir + '.strings'
            # print(newfilePath)
            fp = open(newfilePath, 'w')

            # 该语言在总表中的所有文本
            arr = dataSources[name]
            # print(name, arr) 

            # 获取中文模板中的keys
            filename = module_path + '/pods_i18n/' + dir + '/zh-Hans.lproj/' + dir + '.strings'
            zhKeys = readStringsFile(filename)
            # print(zhKeys)

            # 具体key
            for zhkey in zhKeys:
                try:
                    # 获取在总表中的位置
                    index_in_All = allCodes.index(zhkey)
                except Exception as e:
                    print('紧急：改字段不在里面' + zhkey)

                # print( str(index_in_All) + ': ' + zhkey + ' >|< ' + arr[index_in_All])
                tempValue = arr[index_in_All].rstrip()  # 去除左右两边空格
                # 将数据整理，塞入.strings文件中
                string = '\"' + zhkey + '\"' + ' = ' + '\"' + tempValue + '\"' + ';' + '\n'
                fp.write(string)

# 运行
main()