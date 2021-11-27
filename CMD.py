#!usr/bin/python3
from threading import Timer
import urllib.request
import hashlib
import time
from PIL import Image
import importlib as il
import msvcrt as m
import os
import pickle as pic
import re
import sys
CMD_NAME = os.path.basename(__file__)
try:
    import downloads
except ModuleNotFoundError:
    os.makedirs('downloads\\__pycache__')
    import downloads
try:
    from downloads import get_package
except ImportError:
    fi = open('downloads\\get_package.py', 'w')
    fi.write("import glob\n\nimport os\n\nexcept_com = ['get_package']\ndef get_package():\n\n    files = []\n\n    com_dict = {}\n\n    help_d = {}\n\n    final_files = []\n    for filename in glob.glob(__package__+'\\\\*.py'):\n\n        if not os.path.splitext(os.path.basename(filename))[0] in except_com:\n\n            files.append(os.path.splitext(os.path.basename(filename))[0])\n\n    for j in files:\n\n        try:\n\n            exec(f'from downloads import {j}')\n        except:\n            pass\n        else:\n\n            print(j,eval(f'{j}.__dir__()'))\n\n            if 'com_dict' in eval(f'{j}.__dir__()'):\n\n                if j == eval(f'{j}.com_dict')[0] and 'help_d' in eval(f'{j}.__dir__()') and j in eval(f'{j}.__dir__()'):\n                    com_dict.update({j:eval(f'{j}.com_dict')})\n                    help_d.update({j:eval(f'{j}.help_d')})\n                    final_files.append(j)\n\n    return (com_dict,help_d,final_files)")
    fi.close()
    fi = open('downloads\\__pycache__\\get_package.cpython-38.pyc', 'wb')
    fi.write(b'U\r\r\n\x00\x00\x00\x00\xcf\x9a#`\xbd\x03\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s"\x00\x00\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x02g\x01Z\x02d\x03d\x02\x84\x00Z\x03d\x01S\x00)\x04\xe9\x00\x00\x00\x00N\xda\x0bget_packagec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x08\x00\x00\x00C\x00\x00\x00s,\x01\x00\x00g\x00}\x00i\x00}\x01i\x00}\x02g\x00}\x03t\x00\xa0\x00t\x01d\x01\x17\x00\xa1\x01D\x00]>}\x04t\x02j\x03\xa0\x04t\x02j\x03\xa0\x05|\x04\xa1\x01\xa1\x01d\x02\x19\x00t\x06k\x07r\x1e|\x00\xa0\x07t\x02j\x03\xa0\x04t\x02j\x03\xa0\x05|\x04\xa1\x01\xa1\x01d\x02\x19\x00\xa1\x01\x01\x00q\x1e|\x00D\x00]\xbe}\x05z\x12t\x08d\x03|\x05\x9b\x00\x9d\x02\x83\x01\x01\x00W\x00n\x0c\x01\x00\x01\x00\x01\x00Y\x00qbX\x00t\t|\x05t\n|\x05\x9b\x00d\x04\x9d\x02\x83\x01\x83\x02\x01\x00d\x05t\n|\x05\x9b\x00d\x04\x9d\x02\x83\x01k\x06rb|\x05t\n|\x05\x9b\x00d\x06\x9d\x02\x83\x01d\x02\x19\x00k\x02rbd\x07t\n|\x05\x9b\x00d\x04\x9d\x02\x83\x01k\x06rb|\x05t\n|\x05\x9b\x00d\x04\x9d\x02\x83\x01k\x06rb|\x01\xa0\x0b|\x05t\n|\x05\x9b\x00d\x06\x9d\x02\x83\x01i\x01\xa1\x01\x01\x00|\x02\xa0\x0b|\x05t\n|\x05\x9b\x00d\x08\x9d\x02\x83\x01i\x01\xa1\x01\x01\x00|\x03\xa0\x07|\x05\xa1\x01\x01\x00qb|\x01|\x02|\x03f\x03S\x00)\tNz\x05\\*.pyr\x01\x00\x00\x00z\x16from downloads import z\n.__dir__()\xda\x08com_dictz\t.com_dict\xda\x06help_dz\x07.help_d)\x0c\xda\x04glob\xda\x0b__package__\xda\x02os\xda\x04path\xda\x08splitext\xda\x08basename\xda\nexcept_com\xda\x06append\xda\x04exec\xda\x05print\xda\x04eval\xda\x06update)\x06\xda\x05filesr\x03\x00\x00\x00r\x04\x00\x00\x00Z\x0bfinal_files\xda\x08filename\xda\x01j\xa9\x00r\x14\x00\x00\x00\xfa6D:\\programe\\py\\CMD\\TEST-PLACE\\downloads\\get_package.pyr\x02\x00\x00\x00\x0b\x00\x00\x00s&\x00\x00\x00\x00\x02\x04\x02\x04\x02\x04\x02\x04\x01\x12\x02\x1c\x02 \x02\x08\x02\x02\x02\x12\x01\x06\x01\x06\x03\x14\x02\x12\x02:\x01\x18\x01\x18\x01\x0c\x02)\x04r\x05\x00\x00\x00r\x07\x00\x00\x00r\x0b\x00\x00\x00r\x02\x00\x00\x00r\x14\x00\x00\x00r\x14\x00\x00\x00r\x14\x00\x00\x00r\x15\x00\x00\x00\xda\x08<module>\x01\x00\x00\x00s\x06\x00\x00\x00\x08\x02\x08\x02\x06\x06')
    fi.close()
    try:
        from downloads import get_package
    except ImportError:
        os.system(f'python {CMD_NAME}')
        os.system('cls')
        exit(0)
key_dict = {b'q': 'q', b'w': 'w', b'e': 'e', b'r': 'r', b't': 't', b'y': 'y', b'g': 'g', b'j': 'j', b'u': 'u', b'i': 'i', b'o': 'o', b'p': 'p', b'[': '[', b']': ']', b'\\': '\\', b'a': 'a', b's': 's', b'd': 'd', b'f': 'f', b'h': 'h', b'k': 'k', b'l': 'l', b';': ';', b"'": "'", b'z': 'z', b'x': 'x', b'c': 'c', b'v': 'v', b'b': 'b', b'n': 'n', b'm': 'm', b',': ',', b'.': '.', b'/': '/',
            b'\t': '\t', b'`': '`', b'1': '1', b'2': '2', b'3': '3', b'4': '4', b'5': '5', b'6': '6', b'7': '7', b'8': '8', b'9': '9', b'0': '0', b'-': '-', b'=': '=', b'~': '~', b'!': '!', b'@': '@', b'#': '#', b'$': '$', b'%': '%', b'^': '^', b'&': '&', b'*': '*', b'(': '(', b')': ')', b'_': '_', b'+': '+', b'{': '{', b'}': '}', b'|': '|', b':': ':', b'"': '"', b'>': '>', b'?': '?', b'<': '<', b' ': ' ', b'Q': 'Q', b'W': 'W', b'E': 'E', b'R': 'R', b'T': 'T', b'Y': 'Y', b'U': 'U', b'I': 'I', b'O': 'O', b'P': 'P', b'A': 'A', b'S': 'S', b'D': 'D', b'F': 'F', b'G': 'G', b'H': 'H', b'J': 'J', b'K': 'K', b'L': 'L', b'Z': 'Z', b'X': 'X', b'C': 'C', b'V': 'V', b'B': 'B', b'N': 'N', b'M': 'M'}


app_dict = {}
com = ''
path = ''
doc = ''
b = '■'
path_list = []
gui_get_file_value = ''
gui_get_folder_value = ''

help_dict = {'app': ('App command.', 'app <list|uninstall|reload> [the name of the app that will be uninstalled]'),
             'bwp': ('To read a bwp file', 'bwp <path of the bwp file>'),
             'check': ('To check the update!', 'check'),
             'jump': ('To jump from a folder to the other folder', 'jump <path of a folder>)'),
             'list': ('To list all of file or folder under folder', 'list <path of folder>'),
             'move': ('To move a file or folder to the other place', 'move <path> <new path(Need a new name)>'),
             'new': ('To new a file or folder', 'new <name of file otr folder> <file|folder> <type>'),
             'nick': ('To give a nickname to a command', 'nick <command> <nickname>'),
             'print': ('To show the content of the file', 'print <path of file>'),
             'ptb': ('To change a picture into a bwp file(only black and white)', 'ptb <path of picture in real PC> <path of a bwp file>'),
             'rm': ('To remove a file or folder', 'rm <path>'),
             'rn': ('To rename a file or folder', 'rn <path> <new name>'),
             'rt': ('To change the PC change into new', 'rt'),
             'run': ('To run a code file', 'run <path of the code file>'),
             'st': ('To shut down a PC', 'st'),
             'table': ('To edit a table file and new a table file', 'table <path of a table file>', 'Help on table:\n  g:   Go to a spoint\n  i:   Insert\n  s:    Save\n  ESC:    close'),
             'vim': ('To write a file(txt,bwp,...)', 'vim <path of file>', 'Help on vim:\n  Ctrl+S:   Save\n  Ctrl+G:  Goto a spoint/Ln+Col(enter "f" to go to find_history)\n  Ctrl+F:   Find string\n  ESC:   Close'),
             }
help_doc = '#txt\n'
for key in help_dict.keys():
    help_doc += key+' '*(20-len(key)) + help_dict[key][0]+' '*(
        70-len(help_dict[key][0])-len(key))+help_dict[key][1] + '\n'
help_doc += '\nHelp on virtual PC:\ta)  The PC will run the file \'start_run\'(a code file on \ file) when the PC start.'


def ynbox(msg):
    if ['Yes', 'No'][choose_box(list=['Yes', 'No'], msg=msg, mode='letter')] == 'Yes':
        return True
    else:
        return False


def choose_box(list, msg='Choose:', mode='num'):            #......  Y/N
    """
    pick up a choise
    """
    temp = 1
    o_temp = 1
    a_dict = {}
    for n in range(len(list)):
        a_dict.update({n+1: list[n]})
    if mode == 'num':
        for n in a_dict.items():
            print('{}-->{}'.format(n[0], n[1]))
    elif mode == 'letter':
        for n in a_dict.items():
            print('{}'.format(n[1]))
    while 1:
        if mode == 'num':
            sys.stdout.write('\b \b' *
                             len('{}{}'.format(msg, o_temp))+'{}{}'.format(msg, temp))
            sys.stdout.flush()
        elif mode == 'letter':
            sys.stdout.write('\b \b'*len('{}{}'.format(msg, list[o_temp-1]))+'{}{}'.format(
                msg, list[temp-1]))
            sys.stdout.flush()
        char = m.getch()
        if char == b'\xe0':
            o_temp = temp
            char = m.getch()
            if char == b'H':
                if temp > len(list)-1:
                    temp = 1
                else:
                    temp += 1
            elif char == b'P':
                if temp <= 1:
                    temp = len(list)
                else:
                    temp -= 1
        elif char == b'\r':
            break
    return temp-1


try:
    url = urllib.request.Request(f'https://github.com/wzm-2007/liunx_windows-command-virtual-console/blob/main/CMD.py')
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    gra = re.findall('''<td id="LC\d*" class="blob-code blob-code-inner js-file-line">.*</td>''',html)
    last_gra = ''
    for j in gra:
        try:
            tab = re.search('>\s*<',re.search('<td id="LC\d*" class="blob-code blob-code-inner js-file-line">\s*<span class="pl-.*">',j).group()).group()[1:-1]
        except AttributeError:
            tab = ''
        j=re.sub('<td id="LC\d*" class="blob-code blob-code-inner js-file-line">\s*','',j)
        j=re.sub('</span>','',j)
        j=re.sub('<span class="pl-.*?">','',j)
        j = j.replace('\n','')
        j = j.replace('</td>','')
        j.replace('&#39;','"')
        last_gra += f'{tab}{j}\n'
except urllib.error.URLError:
    print('\nPlease Check Your Internet!!\n')
    print('\a')
else:
    print(gra)
    old_gra = open(__file__,'r',encoding='utf-8')
    if gra != old_gra.read():
        if ynbox(msg='We find a update!Are you sure to update?'):
            print('')
            old_gra = open(__file__,'w',encoding='utf-8')
            old_gra.write(gra)
            old_gra.close()
            os.system(f'python {CMD_NAME}')
            os.system('cls')
            exit(0)
        else:
            print('')


def path(p):  # 转化路径    /user/help_doc ------> ['user','help_doc']
    path_list = []
    p = p[:]
    try:
        while p:
            path_list.append(re.search(r'[^\s/]*', p).group())
            p = p[len('/'+re.search(r'[^\s/]*', p).group()):len(p)]
    except AttributeError:
        pass
    try:
        if path_list[0] == '':
            path_list.pop(0)
    except IndexError:
        return []
    return path_list


def re_path(p_li):  # 反路径  ['user','help_doc'] ----> 'user/help_doc'
    p = ''
    p_li = p_li[:]
    p_li.reverse()
    for n in range(len(p_li)):
        p += p_li.pop()+'/'
    return p


def gui_get_file(path_='/', type_=''):
    global gui_get_file_value, file
    file = file_load()
    spoint = 0
    folder_dict = {}
    if path_:
        if len(path_) > 1:
            if path_[0] == '/' and path_[1] == '/':
                path_ = path_[1:]
        else:
            if path_[0] == '/':
                path_ = path_[1:]
    for f in file_TF(path(path_)):
        f_type = get_type(file_TF(path(path_+f'/{f}')))
        if type_:
            if f_type == type_ or f_type == 'folder':
                folder_dict.update({f: f_type})
            else:
                continue
        else:
            folder_dict.update({f: f_type})
    if spoint <= len(folder_dict):
        while 1:
            os.system('cls')
            a = 0
            for key, value in folder_dict.items():
                a += 1
                print('-'*20)
                if a == spoint+1:
                    print(f'#{value}-------{key}#')
                else:
                    print(f'|{value}-------{key}|')
            min = 0 if spoint <= len(folder_dict) - \
                1 else spoint-len(folder_dict)-1
            max = len(folder_dict)-1 if spoint <= len(folder_dict) - \
                1 else len(folder_dict)-1+spoint-len(folder_dict)-1
            if len(folder_dict):
                print(f'{path_}/{list(folder_dict.keys())[spoint]}')
            char = m.getch()
            if char == b'\xe0':
                char = m.getch()
                if char == b'H':
                    spoint -= 1
                    if spoint < min:
                        spoint = len(folder_dict)-1
                elif char == b'P':
                    spoint += 1
                    if spoint > max:
                        spoint = 0
            elif char == b'\r':
                if len(folder_dict):
                    temp = path(path_).copy()
                    temp.append(list(folder_dict.keys())[spoint])
                    break
            elif char == b'\x1b':
                break
            elif char == b'n':
                break
            elif char == b'm':
                break
        if char == b'n':
            name = input('Name:')
            if name:
                fi_fol = choose_box(['folder', 'file'],
                                    msg='File or folder---', mode='letter')
                if fi_fol == 1:
                    print('')
                    type_file = input('Type:')
                else:
                    type_file = 'folder'
                if type_file:
                    if path_:
                        main(
                            ['new', path_+f'/{name}', ['folder', 'file'][fi_fol], type_file])
                    else:
                        main(
                            ['new', f'/{name}', ['folder', 'file'][fi_fol], type_file])
                    file_load()
                    gui_get_file(path_, type_)
                else:
                    file_load()
                    gui_get_file(path_, type_)
            else:
                file_load()
                gui_get_file(path_, type_)
        elif char == b'm':
            if ynbox(f'Remove {path_}:'):
                main(['rm', f'{path_}/{list(folder_dict.keys())[spoint]}'])
                file_load()
                gui_get_file(path_, type_)
            else:
                file_load()
                gui_get_file(path_, type_)
        elif char == b'\r':
            if get_type(file_TF(temp)) == 'folder':
                TF = len(
                    path(f'{path_}/{list(folder_dict.keys())[spoint]}'))
                gui_get_file(
                    f'{path_}/{list(folder_dict.keys())[spoint]}', type_)
            else:
                gui_get_file_value = f'{path_}/{list(folder_dict.keys())[spoint]}'
        elif char == b'\x1b':
            if len(folder_dict):
                temp_f_l = path(f'{path_}/{list(folder_dict.keys())[spoint]}')
                temp_f_l.pop()
                try:
                    temp_f_l.pop()
                except IndexError:
                    if ynbox('CLOSE:'):
                        gui_get_file_value = None
                    else:
                        gui_get_file(path_, type_)
                    print('')
                else:
                    if not temp_f_l:
                        temp_f_l = ['']
                    gui_get_file(re_path(temp_f_l), type_)
            else:
                gui_get_file(re_path(path(path_)[:-1]), type_)
    return gui_get_file_value


def gui_get_folder(path_='/'):
    global gui_get_folder_value, file
    file = file_load()
    spoint = 0
    folder_dict = {}
    if path_:
        if len(path_) > 1:
            if path_[0] == '/' and path_[1] == '/':
                path_ = path_[1:]
        else:
            if path_[0] == '/':
                path_ = path_[1:]
    for f in file_TF(path(path_)):
        f_type = get_type(file_TF(path(path_+f'/{f}')))
        if f_type == 'folder':
            folder_dict.update({f: f_type})
    if spoint <= len(folder_dict):
        while 1:
            os.system('cls')
            a = 0
            for key, value in folder_dict.items():
                a += 1
                print('-'*20)
                if a == spoint+1:
                    print(f'#{value}-------{key}#')
                else:
                    print(f'|{value}-------{key}|')
            min = 0 if spoint <= len(folder_dict) - \
                1 else spoint-len(folder_dict)-1
            max = len(folder_dict)-1 if spoint <= len(folder_dict) - \
                1 else len(folder_dict)-1+spoint-len(folder_dict)-1
            if len(folder_dict):
                print(f'{path_}/{list(folder_dict.keys())[spoint]}')
            char = m.getch()
            if char == b'\xe0':
                char = m.getch()
                if char == b'H':
                    spoint -= 1
                    if spoint < min:
                        spoint = len(folder_dict)-1
                elif char == b'P':
                    spoint += 1
                    if spoint > max:
                        spoint = 0
                elif char == b'M':
                    break
            elif char == b'\r':
                if len(folder_dict):
                    temp = path(path_).copy()
                    temp.append(list(folder_dict.keys())[spoint])
                    break
            elif char == b'\x1b':
                break
            elif char == b'n':
                break
            elif char == b'm':
                break
        if char == b'n':
            name = input('Name:')
            if name:
                if path_:
                    main(
                        ['new', path_+f'/{name}', 'folder', 'folder'])
                else:
                    main(
                        ['new', f'/{name}', 'folder', 'folder'])
                file_load()
                gui_get_folder(path_)
            else:
                file_load()
                gui_get_folder(path_)
        elif char == b'm':
            try:
                if ynbox(f'Remove {path_}/{list(folder_dict.keys())[spoint]}:'):
                    main(['rm', f'{path_}/{list(folder_dict.keys())[spoint]}'])
                    file_load()
                    gui_get_folder(path_)
                else:
                    file_load()
                    gui_get_folder(path_)
            except IndexError:
                file_load()
                gui_get_folder(path_)
        elif char == b'\r':
            gui_get_folder_value = f'{path_}/{list(folder_dict.keys())[spoint]}'
        elif char == b'\x1b':
            if len(folder_dict):
                temp_f_l = path(f'{path_}/{list(folder_dict.keys())[spoint]}')
                temp_f_l.pop()
                try:
                    temp_f_l.pop()
                except IndexError:
                    if ynbox('CLOSE:'):
                        gui_get_folder_value = None
                    else:
                        gui_get_folder(path_)
                    print('')
                else:
                    if not temp_f_l:
                        temp_f_l = ['']
                    gui_get_folder(re_path(temp_f_l))
            else:
                gui_get_folder(re_path(path(path_)[:-1]))
        elif char == b'M':
            gui_get_folder(
                f'{path_}/{list(folder_dict.keys())[spoint]}')
    return gui_get_folder_value


'''def run_code(code, values, line, funs, fun_values, b_fun):
    temp_values = {}
    give_patt = "^[a-z,_]*=\".*\"$|^[a-z,_]*='.*'$|^[a-z,_]*=\d*$"
    calculation_patt = '^[a-z,_]*=[a-z,_,1-9]*[+,-,/*,/][a-z,_,1-9]*'
    fun_patt = '^fun [a-z,_]*\(.*\){.*}*'
    if re.search('^[a-z_]*\(.*\)$', code):  # 调用函数
        left_s = re.search('\(', code).span()[0]
        right_s = re.search('\)', code).span()[0]
        name = code[:left_s]
        try:
            fun_codes = funs[name]
        except KeyError:
            print(f'line:{line}=>{code}\tUnknow function:{name}')
            return None
        vs = code[left_s+1:right_s].split(',')
        temp_values = values.copy()
        if not len(fun_values[name]) == len(vs):
            print(f'line:{line}=>{code}\tLose vaules')
            return None
        for n in range(len(vs)):
            if re.search('^[a-z_]*$', vs[n]):
                try:
                    vs[n] = values[vs[n]]
                except KeyError:
                    print(f'line:{line}=>{code}\tUnknow value:{vs[n]}')
                    return None
            else:
                vs[n] = eval(vs[n])
            if not (type(vs[n]) == type('a') or type(vs[n]) == type(1)):
                print(f'line:{line}=>{code}\tUnknow value:{vs[n]}')
                return None
        if name in b_fun:
            if name == b_fun[0]:  # print
                print(vs[0])
        temp_values.update(dict(zip(fun_values[name], vs)))
        l = 0
        for n in funs[name]:
            l += 1
            run_code(n, temp_values, l, funs, fun_values, b_fun)
    elif re.search(give_patt, code):  # 赋值代码
        equals = re.search('=', code).span()[0]
        name = code[:equals]
        vaule = eval(code[equals+1:])
        values.update({name: vaule})
    elif re.search(calculation_patt, code):  # 运算代码
        equals = re.search('=', code).span()[0]
        name = code[:equals]
        calculation = code[equals+1:]
        symbol = re.search('[+,-,/*,//]', calculation).span()[0]
        num1 = calculation[:symbol]
        num2 = calculation[symbol+1:]
        if re.search('^[a-z_]*$', num1):  # num1
            try:
                num1 = values[num1]
            except KeyError:
                print(f'line:{line}\tUnknow vaule:{num1}')
                return None
        elif re.search('^\d*$', num1):
            num1 = eval(num1)
        else:
            print(f'line:{line}\tUnknow vaule:{num1}')
            return None
        if re.search('^[a-z_]*$', num2):  # num2
            try:
                num2 = values[num2]
            except KeyError:
                print(f'line:{line}\tUnknow vaule:{num2}')
                return None
        elif re.search('^\d*$', num2):
            num2 = eval(num2)
        else:
            print(f'line:{line}\tUnknow vaule:{num2}')
            return None
        if not type(num1) == type(num2):
            print(f'line:{line}=>{code}\tError cal')
            return None
        symbol = re.search('[+,-,/*,//]', calculation).group()
        if symbol == '+':
            vaule = num1+num2
        elif symbol == '-':
            vaule = num1-num2
        elif symbol == '*':
            vaule = num1*num2
        elif symbol == '/':
            vaule = num1//num2
        values.update({name: vaule})'''


command_dict = {
    'vim': ['vim', [1], [0]],
    'list': ['list', [1, 0], [0]],
    'print': ['show', [1], [0]],
    'new': ['new', [3], [0]],
    'rm': ['remove', [1], [0]],
    'rn': ['rename', [2], [0]],
    'move': ['move', [2], [0, 1]],
    'copy': ['copy', [2], [0, 1]],
    'rt': ['re_start', [0], []],
    'bwp': ['bwp', [1], [0]],
    'ptb': ['png_to_bwp', [2], [1]],
    'run': ['run', [1], [0]],
    'help': ['help', [1, 0], []],
    'jump': ['jump', [1], [0]],
    'table': ['table', [1], [0]],
    'nick': ['nick', [2], []],
    'st': ['shut_down', [0], []],
    'app': ['app', [1, 2], []],
    'check': ['check',[0],[]]
}


class Comd():  # 代码类
    def __init__(self, workspace, command_dict, help_dict, nick_dict, app_list):
        self.help_dict = help_dict
        self.workspace = workspace
        self.command_dict = command_dict
        self.nick_dict = nick_dict
        self.app_list = app_list

    def vim(self, p):  # 编写文本
        p_li = path(p)
        file_load()
        doc = file
        last = file
        try:
            for n in range(len(path(p))):
                last = last[path(p)[n]]
        except KeyError:  # 路径出错
            self.new(p, 'file', 'txt')
            file_load()
            last = file
            try:
                for n in range(len(path(p))):
                    last = last[path(p)[n]]
                file_load()
            except KeyError:
                print('[Vim]:Error Path')
                return None
        except TypeError:
            print('[Vim]:Error Path')
            return None
        if not type(last) == type('s'):
            print('[Vim]:The path is not a file!')
            return None
        doc = file
        for n in range(len(path(p))):
            doc = doc[path(p)[n]]
        mode = re.search(r'^#.*', last).group()[1:]
        print(f'[Vim]:Remember that:it is a {mode} file')
        input('')
        # 通过msvcrt模块实现输入
        os.system('cls')
        spoint = len(doc)
        syb = '▌'
        line = 1
        find_h = {}
        while 1:
            os.system('cls')
            doc_c = (doc[:spoint]+syb+doc[spoint:]).split('\n')
            for n in range(len(doc_c)):
                if syb in doc_c[n]:
                    line = n+1
                    break
            max = 30
            if len(doc_c) < 30:
                max = len(doc_c)
            elif line <= 30:
                max = 30
            else:
                max = line
            min = 1 if line <= 30 else line-30
            len_ = len(str(max))
            num = '1'
            for n in range(min-1, max):
                num = '{}{}'.format(' '*(len_-len(str(n+1))), n+1)
                print(num+' '+doc_c[n])
            col = 1
            for n in doc_c[line-1]:
                col += 1
                if n == syb:
                    col -= 1
                    break
            print('Ln:{}  Col:{}  Spoint:{}\n--------------------------------------------------------------------------------------------------------------------------------'.format(line, col, spoint))
            char = m.getch()
            if not char == b'\xff':
                if char in list(key_dict.keys()):
                    doc = doc[:spoint]+key_dict[char]+doc[spoint:]
                    if spoint+1 > len(doc):
                        spoint = 0
                    else:
                        spoint += 1
                elif char == b'\r':
                    doc = doc[:spoint]+'\n'+doc[spoint:]
                    if spoint+1 > len(doc):
                        spoint = 0
                    else:
                        spoint += 1
                elif char == b'\x1b':
                    last = file
                    for n in range(len(path(p))):
                        last = last[path(p)[n]]
                    if not last == doc:
                        if ynbox('Close?:'):
                            print('\n')
                            if not ynbox('Close without saving?'):
                                if not re.search('^#.*', doc):
                                    doc = '#txt\n'+doc
                                file_set(doc, p_li)
                                break
                            else:
                                break
                    elif ynbox('Close?:'):
                        break
                elif char == b'\x08':
                    if not spoint == 0:
                        doc = doc[:spoint-1]+doc[spoint:]
                        if spoint-1 < 0:
                            spoint = len(doc)
                        else:
                            spoint -= 1
                    else:
                        if spoint-1 < 0:
                            spoint = len(doc)
                        else:
                            spoint -= 1
                elif char == b'\xe0':
                    sp = m.getch()
                    if sp == b'K':
                        if spoint-1 < 0:
                            spoint = len(doc)
                        else:
                            spoint -= 1
                    elif sp == b'M':
                        if spoint+1 > len(doc):
                            spoint = 0
                        else:
                            spoint += 1
                    elif sp == b'H':
                        spoint = 0
                        for n in doc_c[:line-2]:
                            spoint += 1
                            for i in n:
                                spoint += 1
                        if col > len(doc_c[line-2]):
                            spoint += len(doc_c[line-2])
                        else:
                            spoint += col - 1
                    elif sp == b'P':
                        spoint = 0
                        try:
                            for n in doc_c[:line]:
                                spoint += 1
                                for i in n:
                                    spoint += 1
                            spoint -= 1
                            if col > len(doc_c[line])+1:
                                spoint += len(doc_c[line])
                            else:
                                spoint += col - 1
                        except IndexError:
                            spoint = 0
                            if col > len(doc_c[0]):
                                spoint += len(doc_c[0])
                            else:
                                spoint += col - 1
                elif char == b'\x07':
                    line_c = 1
                    col_c = 1
                    temp = 0
                    sp = input('Goto:')
                    if find_h and sp == 'f':
                        find = choose_box(list(find_h.keys()))
                        print('\n')
                        spoint = find_h[list(find_h.keys())[find]][choose_box(
                            find_h[list(find_h.keys())[find]])]
                    else:
                        try:
                            sp = eval(sp)
                            sp = list(sp)
                        except SyntaxError:
                            pass
                        except TypeError:
                            if sp > 0 and sp < len(doc):
                                spoint = sp
                        except NameError:
                            pass
                        else:
                            if type(sp) == type([1, 2]):
                                if len(sp) < 2:
                                    sp.append(1)
                                try:
                                    sp[0] -= 1
                                    if len(sp) == 2 and sp[0] <= len(doc_c):
                                        try:
                                            line_c = doc_c[sp[0]]
                                        except IndexError:
                                            pass
                                        else:
                                            col_c = sp[1]
                                            for n in range(sp[0]):
                                                temp += len(doc_c[n])+1
                                            temp += col_c
                                            spoint = temp-1
                                except TypeError:
                                    pass
                elif char == b'\x06':
                    find = input('Find:')
                    if find:
                        doc_copy = doc
                        f_list = [0]
                        while 1:
                            if re.search('{}'.format(find), doc_copy):
                                f_list.append(re.search('{}'.format(
                                    find), doc_copy).span()[0]+f_list[-1]+len(find))
                                doc_copy = doc_copy[re.search(
                                    '{}'.format(find), doc_copy).span()[1]:]
                            else:
                                break
                        f_list.pop(0)
                        if f_list:
                            find_h.update({find: f_list})
                elif char == b'\x13':
                    if not re.search('^#.*', doc):
                        doc = '#txt\n'+doc
                    file_set(doc, p_li)
                    print('[Vim]:Save successful')
        os.system('cls')

    def list(self, p):  # 列出文件（夹）
        file_load()
        last = file
        try:
            for n in range(len(path(p))):
                last = last[path(p)[n]]
        except KeyError:  # 路径出错
            print('[List]:Erorr Path')
            return None
        if type(last) == type('s'):
            print('[List]:The path is a file!')
            return None
        print(f'Directory of {p}:')
        for key in last.keys():
            if type(last[key]) == type('s'):
                a = re.search(r'^#.*|^#.*\n', last[key]).span()[1]
                if re.search(r'^#.*\n', last[key]):
                    print(key+'                       ' +
                          last[key][:a]+' file')
                else:
                    print(key+'                       ' +
                          last[key]+' file')
            elif type(last[key]) == type({}):
                print(key+'                       #folder\n')
        if not last.keys():
            print('|', "There is nothing at all!!".center(20, '*'), '|')
        return None

    def show(self, p):  # 展示文件
        file_load()
        last = file
        try:
            for n in range(len(path(p))):
                last = last[path(p)[n]]
        except KeyError:  # 路径出错
            print('[Print]:Erorr Path')
            return None
        if not type(last) == type('s'):
            print('[Print]:The path is not a file!')
            return None
        print(last)
        return None

    def new(self, p, mode, type1):  # 新建文件（夹）
        if not (mode == 'file' or mode == 'folder'):
            print('[New]:Error mode')
            return None
        file_load()
        if type(p) == type([]):
            p = re_path(p)
        if type(p) == type('s'):
            p_li = path(p)
        try:
            new_f = p_li.pop()
        except IndexError:
            print('[New]:Erorr Path')
        else:
            if not p_li == []:
                last = file
                if p_li == []:
                    p_li = ['/']
                try:
                    for n in range(len(p_li)):
                        last = last[p_li[n]]
                except KeyError:  # 路径出错
                    print('[New]:Erorr Path')
                    return None
                if mode == 'file':
                    value = '#'+type1+'\n'
                elif mode == 'folder':
                    value = {}
                file_c = file
                for n in range(len(p_li)-1):  # 使用复制进行更改
                    file_c = file_c.copy()[p_li[n]]
                file_c[p_li[len(p_li)-1]].update({new_f: value})
                f = open('file.pkl', 'wb')
                pic.dump(file, f)
                f.close()
                file_load()
            else:
                if mode == 'file':
                    value = '#'+type1+'\n'
                elif mode == 'folder':
                    value = {}
                file.update({new_f: value})
            f = open('file.pkl', 'wb')
            pic.dump(file, f)
            f.close()
            file_load()
            print('[New]:new the file(folder) succesful!!')
            return None

    def remove(self, p):  # 删除文件（夹）
        file_load()
        last = file
        p_li = path(p)
        if p_li:
            fil = p_li.pop()
            file_c = file.copy()
            try:
                for n in range(len(p_li)):
                    last = last[p_li[n]]
            except KeyError:  # 路径出错
                print('[Rm]:Error path')
                return None
            if not p_li == []:
                for n in range(len(p_li)):  # 使用复制进行更改
                    file_c = file_c[p_li[n]]
                try:
                    re_name_use = list({fil: file_c.pop(fil)}.values())[0]
                except KeyError:
                    print('[Rm]:Error path')
                    return None
            else:
                if file_TF(p_li):
                    re_name_use = list({fil: file.pop(fil)}.values())[0]
                else:
                    print('[Rm]:Error path')
                    return None
            f = open('file.pkl', 'wb')
            pic.dump(file, f)
            f.close()
            file_load()
            print('[Rm]:remove the file(folder) succesful!!')
            return re_name_use
        else:
            print('[Rm]:Error path')

    def rename(self, p, re_name):  # 重命名
        file_load()
        last = file
        p_li = path(p)
        if p_li:
            old_name = p_li.pop()
            p_li.append(re_name)
            try:
                for n in range(len(p_li)-1):
                    last = last[p_li[n]]
            except KeyError:
                print('[Rn]:Erorr Path')
                return None
            try:
                if type(last[old_name]) == type('s'):
                    mode = 'file'
                    type1 = last[old_name][1:re.search(
                        r'^#.*\n', last[old_name]).span()[1]-1]
                elif type(last[old_name]) == type({'s': 1}):
                    mode = 'folder'
                    type1 = ''
            except KeyError:
                print('[Rn]:Erorr Path')
                return None
            value = self.remove(p)
            self.new(p_li, mode, type1)
            file_load()
            file_c = file
            p_li = path(p)[:-1]
            p_li.append(re_name)
            file_set(value, p_li)
            print('[Rn]:rename the file(folder) succesful!!')
            return None
        else:
            print('[Rn]:Erorr Path')

    def move(self, old, new):  # old=原路径,new=新路径
        o_p = path(old)
        n_p = path(new)
        file_load()
        last = file
        doc = file
        try:
            for n in range(len(o_p)-1):
                last = last[o_p[n]]
        except KeyError:
            print('[Move]:Erorr Old_Path')
            return None
        try:
            value = last[o_p[-1]]
        except:
            print('[Move]:Erorr Old_Path')
            return None
        try:
            for n in range(len(n_p)-1):
                doc = doc[n_p[n]]
        except KeyError:
            print('[Move]:Erorr New_Path')
            return None
        else:
            if type(doc) == type('s'):
                print('[Move]:Erorr New_Path')
                return None
        if type(value) == type('s'):
            mode = 'file'
        elif type(value) == type({'s': 1}):
            mode = 'folder'
        try:
            key = n_p.pop()
        except IndexError:
            print('[Move]:Error Path')
            return None
        self.remove(old)
        if mode == 'file':
            self.new(new, mode, re.search('^#.*\n', value).group()[1:-1])
        else:
            self.new(new, mode, 'folder')
        file_c = file
        for n in range(len(n_p)):  # 使用复制进行更改
            file_c = file.copy()[n_p[n]]
        file_c[key] = value
        print('[s]:move the file(folder) succesful!!')
        return None

    def copy(self, old, new):  # old=原路径,new=新路径
        o_p = path(old)
        n_p = path(new)
        file_load()
        last = file
        doc = file
        try:
            for n in range(len(o_p)-1):
                last = last[o_p[n]]
        except KeyError:
            print('[Copy]:Erorr Old_Path')
            return None
        try:
            value = last[o_p[-1]]
        except:
            print('[Copy]:Erorr Old_Path')
            return None
        try:
            for n in range(len(n_p)-1):
                doc = doc[n_p[n]]
        except KeyError:
            print('[Copy]:Erorr New_Path')
            return None
        else:
            if type(doc) == type('s'):
                print('[Copy]:Erorr New_Path')
                return None
        if type(value) == type('s'):
            mode = 'file'
        elif type(value) == type({'s': 1}):
            mode = 'folder'
        try:
            key = n_p.pop()
        except IndexError:
            print('[Copy]:Error Path')
            return None
        if mode == 'file':
            self.new(new, mode, re.search('^#.*\n', value).group()[1:-1])
        else:
            self.new(new, mode, 'folder')
        file_c = file
        for n in range(len(n_p)):  # 使用复制进行更改
            file_c = file.copy()[n_p[n]]
        file_c[key] = value
        print('[s]:copy the file(folder) succesful!!')
        return None

    def re_start(self):
        print('[s]:system restart')
        try:
            for n in range(3, 0, -1):
                print(n)
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        else:
            file = {'start_run': '#code\n//Hello, i am start_run file.I will run when the PC start!!',
                    'user': {'welcome': '#txt\nWelcome to CMD,by WZM!!', 'help_doc': help_doc}}
            f = open('file.pkl', 'wb')
            pic.dump(file, f)
            f.close()
            file_load()
            os.system('cls')
            os.system(f'python {CMD_NAME}')
            exit(0)

    def p_file(self):
        file_load()
        print('[s]:'+str(file))

    def bwp(self, p):  # 编译图片文件
        o_p = path(p)
        last = file
        try:
            for n in range(len(o_p)):
                last = last[o_p[n]]
        except KeyError:
            print('[Bwp]:Erorr Path')
            return None
        if not type(last) == type('s'):
            print('[Bwp]:The path is not a file!')
            return None
        if not re.search('^#bwp', last):
            print("[Bwp]:It's not a picture")
            return None
        if not ('1' in last or '0' in last) or not ('(' in last and ')' in last):
            print('[Bwp]:Erorr Picture')
            return None
        last = last[5:]
        last = eval(last)
        txt = ' '
        for n in last:
            for i in n:
                if i == '1':
                    txt += b
                elif i == '0':
                    txt += '  '
                else:
                    print('[Bwp]:Erorr Picture')
                    return None
                continue
            txt += '\n'
            continue
        print(txt)

    def png_to_bwp(self, real_p, p):  # real_p实际路径,p虚拟路径
        p_li = path(p)
        last = file
        try:
            for n in range(len(p_li)):
                last = last[path(p)[n]]
        except KeyError:  # 路径出错
            self.new(p, 'file', 'bwp')
            file_load()
            last = file
            try:
                for n in range(len(p_li)):
                    last = last[path(p)[n]]
                file_load()
            except KeyError:
                print('[Ptb]:Error Path')
                return None
        except TypeError:
            print('[Ptb]:Error Path')
            return None
        if not type(last) == type('s'):
            print('[Ptb]:The path is not a file!')
            return None
        try:
            img = Image.open(real_p)
        except FileNotFoundError:
            print('[Ptb]:Erorr Real path')
        except Image.ImageError:
            print("[Ptb]:it's not a picture")
        src_strlist = img.convert('RGB').load()
        x_max = img.size[0]
        y_max = img.size[1]
        doc = ''
        for y in range(0, y_max):
            doc += '('
            for x in range(0, x_max):
                str1 = src_strlist[x, y]
                if (str1[0]+str1[1]+str1[2]) >= 250:
                    doc += '"0"'
                else:
                    doc += '"1"'
            doc += '),'
        print('[Ptb]:'+doc)
        file_set('#bwp\n'+doc, p_li)

    def help(self, helper='all'):  # 帮助指令
        if helper == 'all':
            print(
                'Simple command-------------------------------------------------------------------------')
            for key in help_dict.keys():
                if not key in cmd.app_list:
                    print(key+' '*(20-len(key)) +
                          help_dict[key][0]+' '*(70-len(help_dict[key][0]))+help_dict[key][1])
            print(
                'App command-------------------------------------------------------------------------')
            for key in cmd.app_list:
                print(key+' '*(20-len(key)) +
                      help_dict[key][0]+' '*(70-len(help_dict[key][0]))+help_dict[key][1])
        else:
            try:
                key = helper
                print(key+' '*(20-len(key)) +
                      help_dict[key][0]+' '*(70-len(help_dict[key][0]))+help_dict[key][1])
                print(help_dict[key][2])
            except KeyError:
                print('[Help]:Unknow command')
                return None
            except IndexError:
                pass

    '''def run(self, p):
        """
        可执行代码
        """
        vaules = {}
        b_fun = ['print']
        """
        内置函数
        """
        fun_values = {'print': ['print_txt']}
        funs = {'print': 'print txt'}
        temp_values = {}
        give_patt = "^[a-z,_]*=\".*\"$|^[a-z,_]*='.*'$|^[a-z,_]*=\d*$"
        calculation_patt = '^[a-z,_]*=[a-z,_,1-9]*[+,-,/*,/][a-z,_,1-9]*'
        fun_patt = '^fun [a-z,_]*\(.*\){.*}*'
        p_li = path(p)
        code = file
        try:
            for n in range(len(p_li)):
                code = code[p_li[n]]
        except KeyError:
            print('Erorr Path')
            return None
        if not type(code) == type('s'):
            print('The path is not a file!')
            return None
        if not re.search('^#code', code):
            print('It\'s not a code file!')
            return None
        codes = code.split('\n')[1:]
        print(codes)
        line = 0
        for code in codes:
            line += 1
            if re.search('^[a-z_]*\(.*\)$', code):  # 调用函数
                left_s = re.search('\(', code).span()[0]
                right_s = re.search('\)', code).span()[0]
                name = code[:left_s]
                try:
                    fun_codes = funs[name]
                except KeyError:
                    print(f'line:{line}=>{code}\tUnknow function:{name}')
                    return None
                vs = code[left_s+1:right_s].split(',')
                temp_values = vaules.copy()
                if not len(fun_values[name]) == len(vs):
                    print(f'line:{line}=>{code}\tLose vaules')
                    return None
                for n in range(len(vs)):
                    if re.search('^[a-z_]*$', vs[n]):
                        try:
                            vs[n] = vaules[vs[n]]
                        except KeyError:
                            print(f'line:{line}=>{code}\tUnknow value:{vs[n]}')
                            return None
                    else:
                        try:
                            vs[n] = eval(vs[n])
                        except SyntaxError as r:
                            print(f'line:{line}=>{code}\t{r}')
                    if not (type(vs[n]) == type('a') or type(vs[n]) == type(1)):
                        print(f'line:{line}=>{code}\tUnknow value:{vs[n]}')
                        return None
                if name in b_fun:
                    if name == b_fun[0]:  # print
                        print(vs[0])
                else:
                    temp_values.update(dict(zip(fun_values[name], vs)))
                    l = 0
                    for n in funs[name]:
                        l += 1
                        run_code(n, temp_values, l, funs, fun_values, b_fun)

            elif re.search(give_patt, code):  # 赋值代码
                equals = re.search('=', code).span()[0]
                name = code[:equals]
                vaule = eval(code[equals+1:])
                vaules.update({name: vaule})
            elif re.search(calculation_patt, code):  # 运算代码
                equals = re.search('=', code).span()[0]
                name = code[:equals]
                calculation = code[equals+1:]
                symbol = re.search('[+,-,/*,//]', calculation).span()[0]
                num1 = calculation[:symbol]
                num2 = calculation[symbol+1:]
                if re.search('^[a-z_]*$', num1):  # num1
                    try:
                        num1 = vaules[num1]
                    except KeyError:
                        print(f'line:{line}=>{code}\tUnknow vaule:{num1}')
                        return None
                elif re.search('^\d*$', num1):
                    num1 = eval(num1)
                else:
                    print(f'line:{line}=>{code}\tUnknow vaule:{num1}')
                    return None
                if re.search('^[a-z_]*$', num2):  # num2
                    try:
                        num2 = vaules[num2]
                    except KeyError:
                        print(f'line:{line}=>{code}\tUnknow vaule:{num2}')
                        return None
                elif re.search('^\d*$', num2):
                    num2 = eval(num2)
                else:
                    print(f'line:{line}=>{code}\tUnknow vaule:{num2}')
                    return None
                symbol = re.search('[+,-,/*,//]', calculation).group()
                if not type(num1) == type(num2):
                    print(f'line:{line}=>{code}\tError cal')
                    return None
                if symbol == '+':
                    vaule = num1+num2
                elif symbol == '-':
                    vaule = num1-num2
                elif symbol == '*':
                    vaule = num1*num2
                elif symbol == '/':
                    vaule = num1//num2
                vaules.update({name: vaule})
            elif re.search(fun_patt, code):  # 定义函数代码
                code = code[4:]
                left_s = re.search('\(', code).span()[0]
                right_s = re.search('\)', code).span()[0]
                false_values = code[left_s+1:right_s].split(',')
                name = code[:left_s]
                fun_codes = code[right_s:][2:-1].split('}{')
                funs.update({name: fun_codes})
                fun_values.update({name: false_values})'''

    def run(self, p):
        """
        run code
        """
        p_li = path(p)
        code = file
        try:
            for n in range(len(p_li)):
                code = code[p_li[n]]
        except KeyError:
            print('[Run]:Erorr Path')
            return None
        if not type(code) == type('s'):
            print('[Run]:The path is not a file!')
            return None
        if not re.search('^#code', code):
            print('[Run]:It\'s not a code file!')
            return None
        codes = code.split('\n')[1:]
        line = 0
        temp_l = 0
        times = 0
        temp = 0
        try:
            for n in codes:
                line += 1
                if temp_l >= line:
                    continue
                if re.search('^do \d*$|^do -\d*$', n):
                    times = int(n.split(' ')[1])
                    temp_l = line-1
                    if 'loop' in codes[line-1:]:
                        for i in codes[line-1:]:
                            temp_l += 1
                            if i == 'loop':
                                break
                    else:
                        print('[Run]:Except loop-->line:{}'.format(line))
                    temp = line+1
                    if re.search('^do -\d*$', n):
                        while 1:
                            for j in codes[line:temp_l-1]:
                                temp += 1
                                if re.search('//.*$', j):
                                    j = re.sub('\S\s*//.*', '', j)
                                elif re.search('\s*$', j):
                                    j = re.sub('\s*$', '', j)
                                if not main(j.split(' ')):
                                    print(
                                        '[Run]:Error-->line:{}:{}'.format(temp, j))
                            temp = line+1
                    else:
                        for b in range(times):
                            for j in codes[line:temp_l-1]:
                                temp += 1
                                if re.search('//.*$', j):
                                    j = re.sub('\S\s*//.*', '', j)
                                elif re.search('\s*$', j):
                                    j = re.sub('\s*$', '', j)
                                if not main(j.split(' ')):
                                    print(
                                        '[Run]:Error-->line:{}:{}'.format(temp, j))
                            temp = line+1

                elif not (re.search('^//.*', n) or not n):
                    if re.search('//.*$', n):
                        n = re.sub('\s*//.*', '', n)
                    elif re.search('\s*$', n):
                        n = re.sub('\s*$', '', n)
                    if not main(n.split(' ')):
                        print('[Run]:Error-->line:{}:{}'.format(line, n))
        except KeyboardInterrupt:
            print('[Run]:KeyboardInterrupt-->line:{}:{}'.format(line, n))

    def jump(self, p):
        """
        jump form a folder to the other folder
        """
        p_li = path(p)
        last = file
        try:
            for n in range(len(p_li)):
                last = last[p_li[n]]
        except KeyError:
            print('[Jump]:Erorr Path')
            return None
        if not type(last) == type({1: 'a'}):
            print('[Jump]:The path is not folder')
        else:
            self.workspace = p_li

    def table(self, p):
        """
        edit a table file
        """
        p_li = path(p)
        last = file
        table_dict = {}
        x__max = 10
        x__min = 1
        y__max = 10
        y__min = 1
        spoint = [1, 1]
        try:
            for n in range(len(p_li)):
                last = last[p_li[n]]
        except KeyError:
            self.new(re_path(path(p)), 'file', 'table')
            file_load()
            last = file
            try:
                for n in range(len(p_li)):
                    last = last[path(p)[n]]
                file_load()
            except KeyError:
                print('[Table]:Error Path')
                return None
        if not re.search('^#table', last):
            print("[Table]:It's not a table file!")
            return None
        if not type(last) == type('s'):
            print('[Table]:The path is not a file!')
            return None
        last = last.split('\n')[1:]
        if last[0]:
            for n in last:
                sp = re.search('\)', n).span()[0]
                try:
                    table_dict.update({eval(n[:sp+1]): n[sp+1:]})
                except SyntaxError:
                    print('[Table]:Error table file(don\'t edit it)')
                    return None
            print(table_dict)
        x_max = 0
        for n in table_dict.keys():
            if n[0] >= x_max:
                x_max = n[0]
        y_max = 0
        for n in table_dict.keys():
            if n[0] >= y_max:
                y_max = n[0]
        while 1:
            x__min = 1 if spoint[0] <= 10 else spoint[0]-10
            x__max = 10 if spoint[0] <= 10 else 10+spoint[0]-10
            y__min = 1 if spoint[1] <= 10 else spoint[1]-10
            y__max = 10 if spoint[1] <= 10 else 10+spoint[1]-10
            os.system('cls')
            for y in range(y__min-1, y__max+1):
                print("-"*130)
                for x in range(x__min-1, x__max+1):
                    if y == y__min-1:
                        if x == x__min-1:
                            print(' '*10+'|'+'')
                        else:
                            a = ' '*((10-len(str(x)))//2)+str(x) + \
                                ' ' * ((10-len(str(x)))//2)
                            if len(a) < 10:
                                a += ' '
                            elif len(a) > 10:
                                a += '\b'
                            print(a+'|'+'')
                    else:
                        value = table_dict.get((x, y))
                        if not value:
                            value = ''
                        if x == x__min-1:
                            a = ' '*((10-len(str(y)))//2)+str(y) + \
                                ' ' * ((10-len(str(y)))//2)
                            if len(a) < 10:
                                a += ' '
                            elif len(a) > 10:
                                a += '\b'
                            print(a+'|'+'')
                        else:
                            a = ' '*((10-len(value))//2) + \
                                value+' '*((10-len(value))//2)
                            if len(a) < 10:
                                a += ' '
                            elif len(a) > 10:
                                a += '\b'
                            if x == spoint[0] and y == spoint[1]:
                                print('\b#'+a+'#'+'')
                            else:
                                print(a+'|'+'')
                print('\n')
            print(spoint)
            char = m.getch()
            if char == b'\xe0':
                sp = m.getch()
                if sp == b'K':
                    if spoint[0]-1 <= 0:
                        spoint[0] = 1
                    else:
                        spoint[0] -= 1
                if sp == b'M':
                    spoint[0] += 1
                if sp == b'H':
                    if spoint[1]-1 <= 0:
                        spoint[1] = 1
                    else:
                        spoint[1] -= 1
                if sp == b'P':
                    spoint[1] += 1
            elif char == b'g':
                try:
                    sp = eval(input('Goto:'))
                except SyntaxError:
                    pass
                except NameError:
                    pass
                else:
                    if type(sp) == type((1, 2)):
                        try:
                            if type(sp[0]) == type(1) and type(sp[1]) == type(1):
                                spoint[0] = sp[0]
                                spoint[1] = sp[1]
                        except IndexError:
                            pass
            elif char == b'\r':
                value = table_dict.get(tuple(spoint))
                if not value:
                    value = ''
                while 1:
                    sys.stdout.write('\r{}'.format(value))
                    sys.stdout.flush()
                    char = m.getch()
                    if char in list(key_dict.keys()):
                        value = value+key_dict[char]
                        sys.stdout.write('{}'.format(key_dict[char]))
                        sys.stdout.flush()
                    elif char == b'\x08':
                        value = value[:-1]
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                    elif char == b'\r':
                        break
                table_dict.update({tuple(spoint): value})
            elif char == b'\x1b':
                doc = '#table'
                for n in list(table_dict.items()):
                    doc += '\n{} {}'.format(n[0], n[1])
                last = file
                for n in range(len(path(p))):
                    last = last[path(p)[n]]
                if not last == doc:
                    if ynbox('Close?:'):
                        print('\n')
                        if not ynbox('Close without saving?'):
                            file_set(doc, p_li)
                            break
                        else:
                            break
                elif ynbox('Close?:'):
                    break
            elif char == b's':
                doc = '#table'
                for n in list(table_dict.items()):
                    doc += '\n{} {}'.format(n[0], n[1])
                print('[Table]:SAVING')
                file_set(doc, p_li)
                print('[Table]:Save successful')
        os.system('cls')

    def nick(self, command, nickname):
        try:
            value = command_dict[command]
            help_value = help_dict[command]
        except KeyError:
            print('[Nick]:Error command')
        else:
            if not nickname in command_dict.keys():
                if not command in self.nick_dict.values():
                    self.command_dict.update({nickname: value})
                    self.help_dict.update({nickname: help_value})
                    self.nick_dict.update({command: nickname})
                else:
                    print(f'[Nick]:"{command}" is a nick name!')
            else:
                print(f'[Nick]:"{nickname}" is a command name!')

    def shut_down(self):
        if choose_box(msg='Choose one: ', list=['shut down', 'restart']) == 0:
            print('\n')
            exit(0)
        else:
            print('\n')
            os.system('cls')
            os.system(f'python {CMD_NAME}')
            exit(0)

    def app(self, mode, app_name=''):
        if mode == 'list':
            for n in self.app_list:
                print(f'    {n}')
        elif mode == 'reload':
            from downloads import get_package
            self.help_dict.update(get_package.get_package()[1])
            self.command_dict.update(get_package.get_package()[0])
            self.app_list = get_package.get_package()[2]
        elif mode == 'search':
            for j in app_dict.keys():
                print(f'    {j}')
        elif app_name:
            if mode == 'uninstall':
                if app_name in self.app_list:
                    self.help_dict.pop(app_name)
                    self.command_dict.pop(app_name)
                    os.remove(f'downloads\\{app_name}.py')
                    from downloads import get_package
                    self.help_dict.update(get_package.get_package()[1])
                    self.command_dict.update(get_package.get_package()[0])
                    self.app_list = get_package.get_package()[2]
                    print(f'[App]:Successfully uninstall app name--{app_name}')
                else:
                    print(f'[App]:Unknow app name--{app_name}')
            elif mode == 'install':
                if app_dict:
                    if app_name in app_dict.keys():
                        app_name = app_dict[app_name]
                        try:
                            url = urllib.request.Request(f'https://ghostbin.com/paste/{app_name}', headers={
                                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'})
                            response = urllib.request.urlopen(url)
                        except ValueError:
                            print(f'[App]:No such a app is named--{app_name}')
                        except urllib.error.HTTPError:
                            print(f'[App]:No such a app is named--{app_name}')
                        else:
                            html = response.read().decode('utf-8')
                            f_n = re.search(
                                '<div class="container">\n<h4>.*</h4>', html).group()[28:-5]
                            app_code = html[re.search(
                                '<textarea class="form-control" id="paste" name="paste" disabled>.*', html).span()[0]+64:re.search('</textarea>', html).span()[0]].replace('&#39;', '"')
                            fi = open(f'downloads\\{f_n}', 'w')
                            fi.write(app_code)
                            fi.close()
                            main(['app', 'reload'])
                    else:
                        print(f'[App]:Unknow app name--{app_name}')
                else:
                    print('\nPlease Check Your Internet!!\n')
                    print('\a')
            else:
                print('[App]:Unknow mode')
        else:
            print('[App]:Lost app name.')
    
    def check(self):
        try:
            url = urllib.request.Request(f'https://github.com/wzm-2007/liunx_windows-command-virtual-console/blob/main/CMD.py', headers={
                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'})
            response = urllib.request.urlopen(url)
            html = response.read().decode('utf-8')
            gra = re.findall('''<td id="LC\d*" class="blob-code blob-code-inner js-file-line">.*</td>''',html)
            last_gra = ''
            for j in gra:
                try:
                    tab = re.search('>\s*<',re.search('<td id="LC\d*" class="blob-code blob-code-inner js-file-line">\s*<span class="pl-.*">',j).group()).group()[1:-1]
                except AttributeError:
                    tab = ''
                j=re.sub('<td id="LC\d*" class="blob-code blob-code-inner js-file-line">\s*','',j)
                j=re.sub('</span>','',j)
                j=re.sub('<span class="pl-.*?">','',j)
                j = j.replace('\n','')
                j = j.replace('</td>','')
                j.replace('&#39;','"')
                last_gra += f'{tab}{j}\n'
        except urllib.error.URLError:
            print('\nPlease Check Your Internet!!\n')
            print('\a')
        else:
            old_gra = open(__file__,'r',encoding='utf-8')
            if gra != old_gra.read():
                if ynbox(msg='We find a update!Are you sure to update?'):
                    print('')
                    old_gra = open(__file__,'w',encoding='utf-8')
                    old_gra.write(gra)
                    os.system(f'python {CMD_NAME}')
                    os.system('cls')
                    exit(0)
                else:
                    print('')


def file_TF(p_li):          #p_li ---> ['user','txt']
    last = file_load()
    if not p_li:
        p_li = []
    try:
        for n in p_li:
            last = last[n]
    except KeyError:
        return False
    else:
        return last


def get_type(doc):          #doc ---> string 
    if type(doc) == type('s'):
        if re.search('^#.*\n|^#.*', doc):
            f_type = re.search('^#.*\n|^#.*', doc).group()
            if '\n' in f_type:
                f_type = f_type[1:-1]
            else:
                f_type = f_type[1:]
            return f_type
        else:
            return False
    else:
        return 'folder'


def file_set(doc, p_li):
    global file
    file_c = file
    for n in range(len(p_li)-1):  # 使用复制进行更改
        file_c = file_c.copy()[p_li[n]]
    file_c[p_li[len(p_li)-1]] = doc
    f = open('file.pkl', 'wb')
    pic.dump(file, f)
    f.close()
    file_load()

def app_check():
    global app_dict
    try:
        url = urllib.request.Request(f'https://github.com/wzm-2007/liunx_windows-command-virtual-console/blob/main/downloads/app_dict.txt', headers={
                                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'})
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        app_dict = re.search('''<td id="LC1" class="blob-code blob-code-inner js-file-line">.*</td>''',html).group()[60:-5].replace('&#39;','"')
        app_dict = eval(app_dict)
    except urllib.error.URLError:
        if not app_dict:
            print('\nPlease Check Your Internet!!\n')
            print('\a')

def main(command, mode=0):                  #command ----> ['test'] / ['move','a','user/a']
    file_load()
    command_dict = cmd.command_dict.copy()
    workspace = cmd.workspace.copy()
    c_vs = command[1:]
    if command[0] in list(command_dict.keys()):
        if len(c_vs) in command_dict[command[0]][1]:
            for n in command_dict[command[0]][2]:
                try:
                    true_workspace = workspace.copy()
                    if not c_vs[n][0] == '/':
                        TF = 0
                        num = c_vs[n].count('.')-1
                        if num+1 and num <= len(true_workspace):
                            TF = 1
                            c_vs[n] = c_vs[n].replace(
                                '.'*(num+1), re_path(true_workspace[:len(true_workspace)-num].copy()))
                        if TF:
                            a = '/'+c_vs[n]
                        else:
                            a = '/'+re_path(workspace)+c_vs[n]
                        workspace = cmd.workspace.copy()
                        command_dict = cmd.command_dict.copy()
                        c_vs[n] = a
                except IndexError:
                    if len(c_vs) == 0:
                        c_vs.append('/'+re_path(workspace))
                        workspace = cmd.workspace.copy()
                        command_dict = cmd.command_dict.copy()
                    else:
                        if mode == 0:
                            print('Lose/More values!')
                        else:
                            print('Lose/More values:{}'.format(command))
                        return False
            c_vs = str(c_vs)[1:-1]
            try:
                exec(f'cmd.{command_dict[command[0]][0]}({c_vs})')
            except AttributeError:
                module = command_dict[command[0]][0]
                exec(f'from downloads import {module}')
                exec(
                    f'{command_dict[command[0]][0]}.{command_dict[command[0]][0]}({c_vs})')
        else:
            if mode == 0:
                print('Lose/More values!!')
            else:
                print('Lose/More values:{}'.format(command))
            return False
    else:
        if mode == 0:
            print('Unknow command!!')
        else:
            print('Unknow command:{}'.format(command))
        return False
    return True


def file_load():
    global file
    try:
        fi = open('file.pkl', 'rb')
        file = pic.load(fi)
    except EOFError:
        fi = open('file.pkl', 'wb')
        print('No such a virtual file')
        cmd.re_start()
    except FileNotFoundError:
        fi = open('file.pkl', 'wb')
        print('No such a virtual file')
        cmd.re_start()
    return file


cmd = Comd([], command_dict, help_dict, {}, [])
workspace = []


def fun_workspace():
    print(cmd.workspace)
    return workspace


if __name__ == '__main__':
    try:
        name_pass = pic.load(open('user_pass.pkl', 'rb'))
        while 1:
            name = ''
            pass_ = ''
            print('Log:\n   Username:')
            while 1:
                char = m.getch()
                if not char == b'\xff':
                    if char == b'\r':
                        print('   Password:')
                        while 1:
                            char = m.getch()
                            if not char == b'\xff':
                                if char == b'\r':
                                    break
                                elif char == b'\x08':
                                    pass_ = pass_[:-1]
                                else:
                                    try:
                                        pass_ += key_dict.get(char)
                                    except TypeError:
                                        pass
                        md = hashlib.md5()
                        md.update(pass_.encode('utf-8'))
                        pass_ = md.digest()
                        break
                    elif char == b'\x08':
                        name = name[:-1]
                    else:
                        try:
                            name += key_dict.get(char)
                        except TypeError:
                            pass
            if name_pass.get(name) == None:
                print('Unknow User')
                continue
            if not pass_ == name_pass[name]:
                print('Error Password')
                continue
            else:
                break
    except EOFError:
        np_file = open('user_pass.pkl', 'wb')
        name = ''
        pass_ = ''
        print('Reg:\n   Username:')
        while 1:
            char = m.getch()
            if not char == b'\xff':
                if char == b'\r':
                    print('Password:')
                    while 1:
                        char = m.getch()
                        if not char == b'\xff':
                            if char == b'\r':
                                break
                            elif char == b'\x08':
                                pass_ = pass_[:-1]
                            else:
                                try:
                                    pass_ += key_dict.get(char)
                                except TypeError:
                                    pass
                    md = hashlib.md5()
                    md.update(pass_.encode('utf-8'))
                    pass_ = md.digest()
                    break
                elif char == b'\x08':
                    name = name[:-1]
                else:
                    try:
                        name += key_dict.get(char)
                    except TypeError:
                        pass
        pic.dump({name: pass_}, np_file)
        np_file.close()
    except FileNotFoundError:
        np_file = open('user_pass.pkl', 'wb')
        name = ''
        pass_ = ''
        print('Reg:\n   Username:')
        while 1:
            char = m.getch()
            if not char == b'\xff':
                if char == b'\r':
                    print('   Password:')
                    while 1:
                        char = m.getch()
                        if not char == b'\xff':
                            if char == b'\r':
                                break
                            elif char == b'\x08':
                                pass_ = pass_[:-1]
                            else:
                                pass_ += key_dict.get(char)
                    md = hashlib.md5()
                    md.update(pass_.encode('utf-8'))
                    pass_ = md.digest()
                    break
                elif char == b'\x08':
                    name = name[:-1]
                else:
                    try:
                        name += key_dict.get(char)
                    except TypeError:
                        pass
        pic.dump({name: pass_}, np_file)
        np_file.close()
    file_load()
    help_dict.update(get_package.get_package()[1])
    command_dict.update(get_package.get_package()[0])
    cmd.app_list = get_package.get_package()[2]
    os.system('cls')
    fl = file
    try:
        for n in range(len(path('/start_run'))):
            fl = fl[path('/start_run')[n]]
    except KeyError:
        pass
    else:
        cmd.run('/start_run')
    while 1:
        command_dict = cmd.command_dict.copy()
        help_dict = cmd.help_dict.copy()
        workspace = cmd.workspace.copy()
        command = input('/'+re_path(workspace)+'>>>').split(' ')
        main(command)
