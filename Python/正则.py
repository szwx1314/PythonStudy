import re

# print(re.findall(r'I\b','I\'m a list'))

# print(re.findall('a','adsfds ysdfsa'))
#
# ret = re.sub('\d','asdasd','1zzzz2zzza32zzzz5',2)
# print(ret)

ret = re.search('(\d+)*(\d+)','5*3')
print(ret)



x,y =re.split('[*/]','0.5*3.9')
print(x,y)