# -*- coding:utf-8 -*-

'''
Created on 2016-11-18
@author: yaodao
目标目录命令行传入 python main.py  /data
'''

import os
import sys

def getFileList(dir , fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, fileList)
    return fileList

def main():
    dir = sys.argv[1]
    print("target dir is  ", dir)
    fileList = getFileList(dir, [])
    for path in fileList:
        print(path)


if __name__ == "__main__":
    main()