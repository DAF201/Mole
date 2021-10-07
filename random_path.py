import os
import random
dictionary=[]
for x,y in enumerate(os.walk(os.path.expanduser('C:\\'))):
    dictionary.append(y)
print(random.choice(dictionary)[0])
