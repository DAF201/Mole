import os
import random
directories = [row[0] for row in os.walk(os.path.expanduser('~/subdir'))]
directories = []
for i, row in enumerate(os.walk(os.path.expanduser('~'))):
    if i > 64:
        break
    directories += [row[0]]
print(random.choice(directories))
