import os
from os import path

import time

print('Operational System: ', os.name)
print('Item exists: ', path.exists('textfile.txt'))
print('Item path: ', path.realpath('textfile.txt'))

last_modification = time.ctime(path.getmtime('textfile.txt'))

print("Modification Time:", last_modification)