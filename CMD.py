#!usr/bin/python3
from PIL import Image
import msvcrt as m
import os
import pickle as pic
import re
import sys
import time
import hashlib

key_dict = {b'q': 'q', b'w': 'w', b'e': 'e', b'r': 'r', b't': 't', b'y': 'y', b'g': 'g', b'j': 'j', b'u': 'u', b'i': 'i', b'o': 'o', b'p': 'p', b'[': '[', b']': ']', b'\\': '\\', b'a': 'a', b's': 's', b'd': 'd', b'f': 'f', b'h': 'h', b'k': 'k', b'l': 'l', b';': ';', b"'": "'", b'z': 'z', b'x': 'x', b'c': 'c', b'v': 'v', b'b': 'b', b'n': 'n', b'm': 'm', b',': ',', b'.': '.', b'/': '/',
            b'\t': '\t', b'`': '`', b'1': '1', b'2': '2', b'3': '3', b'4': '4', b'5': '5', b'6': '6', b'7': '7', b'8': '8', b'9': '9', b'0': '0', b'-': '-', b'=': '=', b'~': '~', b'!': '!', b'@': '@', b'#': '#', b'$': '$', b'%': '%', b'^': '^', b'&': '&', b'*': '*', b'(': '(', b')': ')', b'_': '_', b'+': '+', b'{': '{', b'}': '}', b'|': '|', b':': ':', b'"': '"', b'>': '>', b'?': '?', b'<': '<', b' ': ' ', b'Q': 'Q', b'W': 'W', b'E': 'E', b'R': 'R', b'T': 'T', b'Y': 'Y', b'U': 'U', b'I': 'I', b'O': 'O', b'P': 'P', b'A': 'A', b'S': 'S', b'D': 'D', b'F': 'F', b'G': 'G', b'H': 'H', b'J': 'J', b'K': 'K', b'L': 'L', b'Z': 'Z', b'X': 'X', b'C': 'C', b'V': 'V', b'B': 'B', b'N': 'N', b'M': 'M'}


com = ''
path = ''
doc = ''
b = '■'
path_list = []


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


def run_code(code, values, line, funs, fun_values, b_fun):
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
        values.update({name: vaule})
try:
    name_pass = pic.load(open('user_pass.pkl', 'rb'))
    while 1:
        name = ''
        pass_ = ''
        print('Username:')
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
    print('Reg:\nUsername:')
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
    print('Reg:\nUsername:')
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
                            pass_ += key_dict.get(char)
                md = hashlib.md5()
                md.update(pass_.encode('utf-8'))
                pass_ = md.digest()
                break
            elif char == b'\x08':
                name = name[:-1]
            else:
                name += key_dict.get(char)
    pic.dump({name: pass_}, np_file)
    np_file.close()
workspace=[]
def main():
    workspace=cmd.workspace.copy()
    command = input('/'+re_path(workspace)+'>>>').split(' ')
    workspace=cmd.workspace.copy()
    c_vs = command[1:]
    if command[0] in list(command_dict.keys()):
        if len(c_vs) == command_dict[command[0]][1]:
            for n in command_dict[command[0]][2]:
                try:
                    if not c_vs[n][0] == '/':
                        a='/'+re_path(workspace)+c_vs[n]
                        c_vs[n] = a
                except IndexError:
                    print('Lose/More values!!')
                    return None
            c_vs = str(c_vs)[1:-1]
            exec(f'cmd.{command_dict[command[0]][0]}({c_vs})')
        else:
            print('Lose/More values!!')
            return None
    else:
        print('Unknow command!!')
        return None

command_dict = {
    'vim': ['vim', 1, [0]],
    'list': ['list', 1, [0]],
    'show': ['show', 1, [0]],
    'new': ['new', 3, [0]],
    'remove': ['remove', 1, [0]],
    'rename': ['rename', 2, [0]],
    'move': ['move', 2, [0, 1]],
    'restart': ['re_start', 0, []],
    'bwp': ['bwp', 1, [0]],
    'png_to_bwp': ['png_to_bwp', 1, []],
    'run': ['run', 1, [0]],
    'help': ['help', 1, []],
    'jump': ['jump', 1, [0]]
}

class Comd():  # 代码类
    def __init__(self,workspace):
        self.workspace=workspace
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
                print('Error Path')
                return None
        except TypeError:
            print('Error Path')
            return None
        if not type(last) == type('s'):
            print('The path is not a file!')
            return None
        doc = file
        for n in range(len(path(p))):
            doc = doc[path(p)[n]]
        mode = re.search(r'^#.*', last).group()[1:]
        print(f'Remember that:it is a {mode} file')
        input('')
        # 通过msvcrt模块实现输入
        os.system('cls')
        spoint = len(doc)
        syb = '|'
        while 1:
            os.system('cls')
            print(doc[:spoint]+syb+doc[spoint:])
            print(spoint)
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
                    os.system('cls')
                    mode = input(':')
                    if mode == 'q':
                        doc = last
                        break
                    elif mode == 'wq':
                        break
                elif char == b'\x08':
                    doc = doc[:spoint-1]+doc[spoint:]
                    if spoint-1 <= 0:
                        spoint = len(doc)
                    else:
                        spoint -= 1
                elif char == b'\xe0':
                    sp = m.getch()
                    if sp == b'K':
                        if spoint-1 <= 0:
                            spoint = len(doc)
                        else:
                            spoint -= 1
                    if sp == b'M':
                        if spoint+1 > len(doc):
                            spoint = 0
                        else:
                            spoint += 1

        if mode == 'wq':
            file_c = file
            for n in range(len(p_li)-1):  # 使用复制进行更改
                file_c = file_c.copy()[p_li[n]]
            file_c[p_li[len(p_li)-1]] = doc
            os.system('cls')
            print('SAVING')
            f = open('file.pkl', 'wb')
            pic.dump(file, f)
            f.close()
            print('Save successful')

        else:
            os.system('cls')
            print('Only Quit')
            doc = None

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
        for key in last.keys():
            if type(last[key]) == type('s'):
                a = re.search(r'^#.*\n', last[key]).span()[1]
                print(key, end='                       ' +
                      last[key][:a-1]+' file\n')
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
                file_c = file.copy()
                if mode == 'file':
                    value = '#'+type1+'\n'
                elif mode == 'folder':
                    value = {}
                try:
                    for n in range(len(path(p))-1):  # 使用复制进行更改
                        file_c = file_c[p_li[n]]
                except KeyError:
                    file_c = file.copy()
                file_c.update({new_f: value})
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
        print(p_li)
        for n in range(len(p_li)-1):  # 使用复制进行更改
            file_c = file_c.copy()[p_li[n]]
        print(file_c)
        file_c[p_li[-1]] = value
        f = open('file.pkl', 'wb')
        pic.dump(file, f)
        f.close()
        file_load()
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
        print(last)
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
        self.remove(old)
        key = n_p.pop()
        self.new(new, mode, last[o_p[-1]][:-1])
        file_c = file
        for n in range(len(n_p)):  # 使用复制进行更改
            file_c = file.copy()[n_p[n]]
        file_c[key] = value
        print('[s]:move the file(folder) succesful!!')
        return None

    def re_start(self):
        print('[s]:system restart')
        file_load()
        file = {'user': {'welcome': '#txt\nWelcome to CMD,by WZM!!'}}
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

    def png_to_bwp(self, real_p):  # real_p实际路径,p虚拟路径
        try:
            img = Image.open(real_p)
        except FileNotFoundError:
            print('Erorr Real path')
        except Image.ImageError:
            print("it's not a picture")
        src_strlist = img.convert('RGB').load()
        print(src_strlist)
        x_max = img.size[0]
        y_max = img.size[1]
        print(x_max, y_max)
        doc = ''
        for y in range(0, y_max):
            doc += '('
            for x in range(0, x_max):
                str1 = src_strlist[x, y]
                if str1[1] > 200 and str1[2] > 200 and str1[0] > 200:
                    doc += '"0"'
                else:
                    doc += '"1"'
            doc += '),'
        print('[s]:'+doc)

    def help(self, helper):  # 帮助指令
        help = {'vim': ('To write a file(txt,bwp,...)', '*(path of file)'),
                'list': ('To list all of file or folder under folder', '*(path of folder)'),
                'show': ('To show the content of the file', '*(path of file)'),
                'new': ('To new a file or folder', '*(path of file/folder,mode=fileor folder,type of th file(the type of folder is " "))'),
                'remove': ('To remove a file or folder', '*(path of file or folder)'),
                'rename': ('To rename a file or folder', '*(path of file or folder)'),
                'move': ('To move a file or folder to the other place', '*(path of file or folder,new path(You can change the name of the file))'),
                'png_to_bwp': ('To change a picture into a bwp file(only black and white)', '*(path of picture in the real PC)'),
                'bwp': ('To read a bwp file', '*(path of the bwp file)'),
                're_start': ('To make the PC change into new', '*(NO)'),
                'run': ('To run a code file', '*(path of the code file)'),
                'jump': ('jump form a folder to the other folder', '*(path)')
                }
        if helper == 'all':
            for key in help.keys():
                print(key+' '*(20-len(key)) +
                      help[key][0]+' '*(70-len(help[key][0])-len(key))+help[key][1])
        else:
            try:
                key = helper
                print(key+' '*(20-len(key)) +
                      help[key][0]+' '*(70-len(help[key][0])-len(key))+help[key][1])
            except KeyError:
                print('Unknow command')
                return None

    def run(self, p):
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
                fun_values.update({name: false_values})

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
cmd = Comd([])
def file_load():
    global file
    try:
        fi=open('file.pkl', 'rb')
        file = pic.load(fi)
    except EOFError:
        return None
    except FileNotFoundError:
        fi = open('file.pkl', 'wb')
        print('No such a virtual file')
        cmd.re_start()
    return file
file_load()
while 1:
    main()
