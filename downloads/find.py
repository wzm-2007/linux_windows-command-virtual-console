import sys
import os
import re
help_d = ('Search file from /','*(file\'s name)')
com_dict = ['find', [1,2], []]
sys.path.append(os.path.abspath('..\\'))
import CMD
find_list = []
file = CMD.file_load()
path = []

def find_fun(file_c,string,f_type = ''):
    global find_list,path
    for key in file_c.keys():
        if type(file_c[key]) == type({}):
            path.append(key)
            find_fun(file_c[key],string,f_type)
            if path:
                path.pop(-1)
        else:
            path.append(key)
            if string in key:
                if f_type:
                    if CMD.get_type(file_c[key]) == f_type:
                        find_list.append('/'+CMD.re_path(path)[:-1])
                else:
                    find_list.append('/'+CMD.re_path(path)[:-1])
            if path:
                path = path[:-1]
            continue

def find(file_name,string = ''):
    global file,find_list,path
    file = CMD.file_load()
    file_c = file.copy()
    find_list = []
    path = []
    find_fun(file_c.copy(),file_name,string)
    a=0
    for n in find_list:
        a+=1
        print(f'{a} {n}')
    find_list = []
    path = []
    