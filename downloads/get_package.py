import glob
import os
except_com = ['get_package']


def get_package():
    files = []
    com_dict = {}
    help_d = {}
    for filename in glob.glob(__package__+'\\*.py'):
        if not os.path.splitext(os.path.basename(filename))[0] in except_com:
            files.append(os.path.splitext(os.path.basename(filename))[0])
    for n in files:
        exec(f'from downloads import {n}')
        com_dict.update({n:eval(f'{n}.com_dict')})
        help_d.update({n:eval(f'{n}.help_d')})
    return (com_dict,help_d,files)