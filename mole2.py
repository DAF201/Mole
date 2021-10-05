times = 0
PATH = ''
# this is the first mole!
"""
This work on both for sure
"""
import subprocess
import os
times = times+1
this = __file__


def self_copy():
    with open(__file__, 'r')as this_file:
        this = this_file.readlines()[2:]
    temp = ''
    for x in this:
        temp = temp+x
    this = temp
    with open("mole"+str(times)+".py", 'w')as file:
        file.write('times=%s\nPATH=r"%s"\n%s' % (times, __file__, this))


def call_up():
    print('this is the %s mole!' % (times-1))
    subprocess.Popen("python mole"+str(times)+".py")


def change():
    try:
        self_copy()
    except:
        self_copy()
    finally:
        call_up()
    try:
        os.remove(PATH)
    except:
        os.remove(PATH)


change()
