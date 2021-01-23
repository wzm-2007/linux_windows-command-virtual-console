#!usr/bin/python3
from downloads import get_package
from PIL import Image
import importlib as il
import msvcrt as m
import os
import pickle as pic
import re
import sys
import time
import hashlib
import downloads
import urllib.request

key_dict = {b'q': 'q', b'w': 'w', b'e': 'e', b'r': 'r', b't': 't', b'y': 'y', b'g': 'g', b'j': 'j', b'u': 'u', b'i': 'i', b'o': 'o', b'p': 'p', b'[': '[', b']': ']', b'\\': '\\', b'a': 'a', b's': 's', b'd': 'd', b'f': 'f', b'h': 'h', b'k': 'k', b'l': 'l', b';': ';', b"'": "'", b'z': 'z', b'x': 'x', b'c': 'c', b'v': 'v', b'b': 'b', b'n': 'n', b'm': 'm', b',': ',', b'.': '.', b'/': '/',
            b'\t': '\t', b'`': '`', b'1': '1', b'2': '2', b'3': '3', b'4': '4', b'5': '5', b'6': '6', b'7': '7', b'8': '8', b'9': '9', b'0': '0', b'-': '-', b'=': '=', b'~': '~', b'!': '!', b'@': '@', b'#': '#', b'$': '$', b'%': '%', b'^': '^', b'&': '&', b'*': '*', b'(': '(', b')': ')', b'_': '_', b'+': '+', b'{': '{', b'}': '}', b'|': '|', b':': ':', b'"': '"', b'>': '>', b'?': '?', b'<': '<', b' ': ' ', b'Q': 'Q', b'W': 'W', b'E': 'E', b'R': 'R', b'T': 'T', b'Y': 'Y', b'U': 'U', b'I': 'I', b'O': 'O', b'P': 'P', b'A': 'A', b'S': 'S', b'D': 'D', b'F': 'F', b'G': 'G', b'H': 'H', b'J': 'J', b'K': 'K', b'L': 'L', b'Z': 'Z', b'X': 'X', b'C': 'C', b'V': 'V', b'B': 'B', b'N': 'N', b'M': 'M'}


com = ''
path = ''
doc = ''
b = '■'
path_list = []

help_dict = {'vim': ('To write a file(txt,bwp,...)', '*(path of file)', 'Help on vim:\n  Ctrl+S:   Save(enter "f" to go to find_history)\n  Ctrl+F:   Find string\n  ESC:   Close'),
             'list': ('To list all of file or folder under folder', '*(path of folder)'),
             'print': ('To show the content of the file', '*(path of file)'),
             'new': ('To new a file or folder', '*(path of file/folder,mode=fileor folder,type of the file(the type of folder is " "))'),
             'rm': ('To remove a file or folder', '*(path of file or folder)'),
             'rn': ('To rename a file or folder', '*(path of file or folder)'),
             'move': ('To move a file or folder to the other place', '*(path of file or folder,new path(You can change the name of the file))'),
             'ptb': ('To change a picture into a bwp file(only black and white)', '*(path of picture in the real PC)'),
             'bwp': ('To read a bwp file', '*(path of the bwp file)'),
             'rt': ('To change the PC change into new', '*(NO)'),
             'st': ('To shut down a PC', '*(NO)'),
             'run': ('To run a code file', '*(path of the code file)'),
             'jump': ('To jump from a folder to the other folder', '*(path)'),
             'table': ('To edit a table file and new a table file', '*(path)', 'Help on table:\n  g:   Go to a spoint\n  i:   Insert\n  s:    Save\n  ESC:    close'),
             'nick': ('To give a nickname to a command', '*(command,nickname)'),
             'app': ('App command.', '*(mode=uninstall/reload/list,app_name(except list,reload))')
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


def choose_box(list, msg='Choose:', mode='num'):
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


def path(p):  # 转化路径
    path_list = []
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


def re_path(p_li):  # 反路径
    p = ''
    p_li.reverse()
    for n in range(len(p_li)):
        p += p_li.pop()+'/'
    return p


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
print('')
workspace = []


command_dict = {
    'vim': ['vim', [1], [0]],
    'list': ['list', [1, 0], [0]],
    'print': ['show', [1], [0]],
    'new': ['new', [3], [0]],
    'rm': ['remove', [1], [0]],
    'rn': ['rename', [2], [0]],
    'move': ['move', [2], [0], [1]],
    'rt': ['re_start', [0], []],
    'bwp': ['bwp', [1], [0]],
    'ptb': ['png_to_bwp', [2], [1]],
    'run': ['run', [1], [0]],
    'help': ['help', [1, 0], []],
    'jump': ['jump', [1], [0]],
    'table': ['table', [1], [0]],
    'nick': ['nick', [2], []],
    'st': ['shut_down', [0], []],
    'app': ['app', [1, 2], []]
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
        syb = '|'
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
            print('Erorr Path')
            return None
        if type(last) == type('s'):
            print('The path is a file!')
            return None
        print(f'Directory of {p}:')
        for key in last.keys():
            if type(last[key]) == type('s'):
                a = re.search(r'^#.*|^#.*\n', last[key]).span()[1]
                if re.search(r'^#.*\n', last[key]):
                    print(key, end='                       ' +
                          last[key][:a]+' file\n')
                else:
                    print(key, end='                       ' +
                          last[key]+' file\n')
            elif type(last[key]) == type({}):
                print(key, end='                       #folder\n')
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
            print('Erorr Path')
            return None
        if not type(last) == type('s'):
            print('The path is not a file!')
            return None
        print(last)
        return None

    def new(self, p, mode, type1):  # 新建文件（夹）
        if not (mode == 'file' or mode == 'folder'):
            print('Error mode')
            return None
        file_load()
        if type(p) == type([]):
            p = re_path(p)
        if type(p) == type('s'):
            p_li = path(p)
        try:
            new_f = p_li.pop()
        except IndexError:
            print('Erorr Path')
        else:
            if not p_li == []:
                last = file
                if p_li == []:
                    p_li = ['/']
                try:
                    for n in range(len(p_li)):
                        last = last[p_li[n]]
                except KeyError:  # 路径出错
                    print('Erorr Path')
                    return None
                if mode == 'file':
                    value = '#'+type1+'\n'
                elif mode == 'folder':
                    value = {}
                file_set({new_f: value}, p_li)
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
            print('[s]:new the file(folder) succesful!!')
            return None

    def remove(self, p):  # 删除文件（夹）
        file_load()
        last = file
        p_li = path(p)
        fil = p_li.pop()
        file_c = file.copy()
        try:
            for n in range(len(p_li)):
                last = last[p_li[n]]
        except KeyError:  # 路径出错
            print('Error path')
            return None
        if not p_li == []:
            for n in range(len(p_li)):  # 使用复制进行更改
                file_c = file_c[p_li[n]]
            try:
                re_name_use = list({fil: file_c.pop(fil)}.values())[0]
            except KeyError:
                print('Error path')
        else:
            re_name_use = list({fil: file.pop(fil)}.values())[0]
        f = open('file.pkl', 'wb')
        pic.dump(file, f)
        f.close()
        file_load()
        print('[s]:remove the file(folder) succesful!!')
        return re_name_use

    def rename(self, p, re_name):  # 重命名
        file_load()
        last = file
        p_li = path(p)
        old_name = p_li.pop()
        p_li.append(re_name)
        try:
            for n in range(len(p_li)-1):
                last = last[p_li[n]]
        except KeyError:
            print('Erorr Path')
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
            print('Erorr Path')
            return None
        value = self.remove(p)
        self.new(p_li, mode, type1)
        file_load()
        file_c = file
        p_li = path(p)[:-1]
        p_li.append(re_name)
        file_set(value, p_li)
        print('[s]:rename the file(folder) succesful!!')
        return None

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
            print('Erorr Old_Path')
            return None
        try:
            value = last[o_p[-1]]
        except:
            print('Erorr Old_Path')
            return None
        try:
            for n in range(len(n_p)-1):
                doc = doc[n_p[n]]
        except KeyError:
            print('Erorr New_Path')
            return None
        else:
            if type(doc) == type('s'):
                print('Erorr New_Path')
                return None
        if type(value) == type('s'):
            mode = 'file'
        elif type(value) == type({'s': 1}):
            mode = 'folder'
        try:
            key = n_p.pop()
        except IndexError:
            print('Error Path')
            return None
        self.remove(old)
        self.new(new, mode, re.search('^#.*\n', value).group()[1:-1])
        file_c = file
        for n in range(len(n_p)):  # 使用复制进行更改
            file_c = file.copy()[n_p[n]]
        file_c[key] = value
        print('[s]:move the file(folder) succesful!!')
        return None

    def re_start(self):
        print('[s]:system restart')
        file_load()
        file = {
            'user': {'welcome': '#txt\nWelcome to CMD,by WZM!!', 'help_doc': help_doc}}
        f = open('file.pkl', 'wb')
        pic.dump(file, f)
        f.close()
        file_load()
        for n in range(3, 0, -1):
            print(n)
            time.sleep(1)
        exit()

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
            print('Erorr Path')
            return None
        if not type(last) == type('s'):
            print('The path is not a file!')
            return None
        if not re.search('^#bwp', last):
            print("[Erorr]:It's not a picture")
            return None
        if not ('1' in last or '0' in last) or not ('(' in last and ')' in last):
            print('Erorr Picture')
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
                    print('Erorr Picture')
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
                print('Error Path')
                return None
        except TypeError:
            print('Error Path')
            return None
        if not type(last) == type('s'):
            print('The path is not a file!')
            return None
        try:
            img = Image.open(real_p)
        except FileNotFoundError:
            print('Erorr Real path')
        except Image.ImageError:
            print("it's not a picture")
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
        print('[s]:'+doc)
        file_set('#bwp\n'+doc, p_li)

    def help(self, helper='all'):  # 帮助指令
        if helper == 'all':
            for key in help_dict.keys():
                print(key+' '*(20-len(key)) +
                      help_dict[key][0]+' '*(70-len(help_dict[key][0])-len(key))+help_dict[key][1])
        else:
            try:
                key = helper
                print(key+' '*(20-len(key)) +
                      help_dict[key][0]+' '*(70-len(help_dict[key][0])-len(key))+help_dict[key][1])
                print(help_dict[key][2])
            except KeyError:
                print('Unknow command')
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
            print('Erorr Path')
            return None
        if not type(code) == type('s'):
            print('The path is not a file!')
            return None
        if not re.search('^#code', code):
            print('It\'s not a code file!')
            return None
        codes = code.split('\n')[1:]
        line = 1
        for n in codes:
            line += 1
            if not main(n.split(' ')):
                print('line:{}'.format(line))

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
            print('Erorr Path')
            return None
        if not type(last) == type({1: 'a'}):
            print('The path is not folder')
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
                            print(' '*10+'|', end='')
                        else:
                            a = ' '*((10-len(str(x)))//2)+str(x) + \
                                ' ' * ((10-len(str(x)))//2)
                            if len(a) < 10:
                                a += ' '
                            elif len(a) > 10:
                                a += '\b'
                            print(a+'|', end='')
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
                            print(a+'|', end='')
                        else:
                            a = ' '*((10-len(value))//2) + \
                                value+' '*((10-len(value))//2)
                            if len(a) < 10:
                                a += ' '
                            elif len(a) > 10:
                                a += '\b'
                            if x == spoint[0] and y == spoint[1]:
                                print('\b#'+a+'#', end='')
                            else:
                                print(a+'|', end='')
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
            if not command in self.nick_dict.values():
                self.command_dict.update({nickname: value})
                self.help_dict.update({nickname: help_value})
                self.nick_dict.update({command: nickname})
            else:
                print(f'[Nick]:"{command}" is a nick name!')

    def shut_down(self):
        exit(0)

    def app(self, mode, app_name=''):
        if mode == 'list':
            for n in self.app_list:
                print(n)
        elif mode == 'reload':
            from downloads import get_package
            self.help_dict.update(get_package.get_package()[1])
            self.command_dict.update(get_package.get_package()[0])
            self.app_list = get_package.get_package()[2]
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
                try:
                    url = urllib.request.Request(f'https://ghostbin.com/paste/{app_name}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'})
                    response = urllib.request.urlopen(url)
                except ValueError:
                    print(f'[App]:No such a app named--{app_name}')
                except urllib.error.HTTPError:
                    print(f'[App]:No such a app named--{app_name}')
                else:
                    html = response.read().decode('utf-8')
                    print(html)
                    f_n = re.search('<h4>.*</h4>', html).group()[4:-5]
                    app_code = re.search(
                        '<textarea class="form-control" id="paste" name="paste" disabled="">.*</textarea>', html).group()[66:-12]
                    print(f_n, app_code)
            else:
                print('[App]:Unknow mode')
        else:
            print('[App]:Lost app name.')


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


cmd = Comd([], command_dict, help_dict, {}, [])


def main(command, mode=0):
    command_dict = cmd.command_dict.copy()
    workspace = cmd.workspace.copy()
    c_vs = command[1:]
    if command[0] in list(command_dict.keys()):
        if len(c_vs) in command_dict[command[0]][1]:
            for n in command_dict[command[0]][2]:
                try:
                    if not c_vs[n][0] == '/':
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
        return None
    except FileNotFoundError:
        fi = open('file.pkl', 'wb')
        print('No such a virtual file')
        cmd.re_start()
    return file


file_load()

help_dict.update(get_package.get_package()[1])
command_dict.update(get_package.get_package()[0])
cmd.app_list = get_package.get_package()[2]

fl = file
try:
    for n in range(len(path('/start_run'))):
        fl = fl[path('/start_run')[n]]
except KeyError:
    pass
else:
    if type(fl) == type('s'):
        if re.search('^#code.*', fl):
            codes = fl.split('\n')[1:]
            for n in codes:
                if not main(n.split(' '), 1):
                    continue

while 1:
    command_dict = cmd.command_dict.copy()
    help_dict = cmd.help_dict.copy()
    workspace = cmd.workspace.copy()
    command = input('/'+re_path(workspace)+'>>>').split(' ')
    main(command)
