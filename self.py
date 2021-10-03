
times=0
times=times+1
this=__file__
if times==1:
    with open(__file__,'r')as this_file:
        this=this_file.readlines()[2:]
else:
    with open(__file__,'r')as this_file:
        this=this_file.readlines()[1:]
temp=''
for x in this:
    temp=temp+x
this=temp
with open(__file__,'w')as file:
    file.write('times=%s\n%s'%(times,this))
