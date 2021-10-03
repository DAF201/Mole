import random
name = str(random.random())
this_file=__file__
with open(name+'.py', 'w')as file1:
    with open(__file__,'r')as file2:
        file1.write(file2.read())
