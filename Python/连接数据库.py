# Author:YSY

import pymysql

# 创建连接
conn = pymysql.connect(host ='192.168.3.59',user ='root',passwd = 'root',db ='SystemMaintenance',charset="utf8")
# 创建游标
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行sql，返回结果为受影响的行数
rt = cur.execute('SELECT * FROM USERS;')

print(cur.fetchone())

# 提交，否则无法保存创建或修改的数据
conn.commit()

# 关闭游标
cur.close()

# 关闭连接
conn.close()

print(rt)