times = 0
PATH=''
#this is the first mole!
#this thing is build on bug, the first few time runs will comes with warning for sure



#10/05/2021 update:
"""
This mole work for vscode terminal with command python mole(running mode not debug mode)
However, it will cause the stack overflow when it comes to cmd and PowerShell
"""
times = times+1
this = __file__

import subprocess
import os
def change():
    try:
        with open(__file__, 'r')as this_file:
            this = this_file.readlines()[2:]
        temp = ''
        for x in this:
            temp = temp+x
        this = temp
        with open("mole"+str(times)+".py", 'w')as file:
            file.write('times=%s\nPATH=r"%s"\n%s' % (times, __file__, this))
    except:
        change()
    finally:
        print('this is the %s mole!'%(times-1))
    try:
        subprocess.Popen("python mole"+str(times)+".py")
        os.remove(PATH)
    except:
        subprocess.Popen("python mole"+str(times)+".py")
        os.remove(PATH)
change()
