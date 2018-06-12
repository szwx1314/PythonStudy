# Author:YSY

f = open("消愁", 'r', encoding="utf-8")





#
# f.write("毛不易的《消愁》\n")
# f.write("毛不易的《消愁》")

print(f.readline())

for line in f.readlines():

    print(line.strip())