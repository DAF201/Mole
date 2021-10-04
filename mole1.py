times = 1
PATH=''
#this is the first mole!
times = times+1
this = __file__

import subprocess
import os
import sys
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
        pass
    finally:
        print('this is the %s mole!'%(times-1))
    subprocess.Popen("python mole"+str(times)+".py")
    if times==1:
        sys.exit(0)
    else:
        os.remove(PATH)
        
change()
