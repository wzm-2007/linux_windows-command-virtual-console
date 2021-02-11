help_d = ('List the files/folders','*(path)')
com_dict = ['tree',[0,1],[0]]
import sys,os
sys.path.append(os.path.abspath('..\\'))
import CMD
file = CMD.file_load()
tree_list = []
level=0
def traverse(dict_):
    global tree_list,level
    for key in dict_.keys():
        if key == list(dict_.keys())[-1]:
            level -= 1
        if type(dict_[key]) == type({}):
            if key == list(dict_.keys())[-1]:
                print('  '*(level+1)+key)
                level += 2
            else:
                print('  '*(level)+key)
                level += 1
            traverse(dict_[key])
            level -= 1
        else:
            if key == list(dict_.keys())[-1]:
                print('  '*(level+1)+'|'+key)
                level += 1
            else:
                print('  '*(level)+'|'+key)
            continue
def tree(path = ''):
    global file,level
    level=0
    file = CMD.file_load()
    if not path:
        path = '/'
    print(f'[Tree]:From {path}:')
    if path == '':
        path = CMD.re_path(CMD.fun_workspace())
    else:
        path = CMD.path(path)
    if CMD.file_TF(path):
        traverse(CMD.file_TF(path))
    else:
        print('[Tree]:Error Path!!(It maybe an empty folder)')