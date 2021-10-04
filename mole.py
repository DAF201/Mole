times = 0
#this is the first mole!
times = times+1
this = __file__


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


change()
