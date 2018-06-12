# Author:YSY

import os,sys

print(os.getcwd())
a=1

print(sys.platform)



import json

date = {'name': 'ysy', 'sex': '男'}
date["addr"] = 'binzhou'
p_str = json.dumps(date)
print(p_str)


date1 = [1,2,3,4,6,4,3,2,5,6]

p_str2 = json.dumps(date1)
print(p_str2)