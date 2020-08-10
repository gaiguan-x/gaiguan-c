from django.test import TestCase

# Create your tests here.
"""
城市接口json数据
http://zhouxunwang.cn/data/?id=104&key=Vb7F+tYwQtX+h5mL+4M3QG/IOwTgsJeZ/pxz7fk&ske=1
保存到数据库中去
这个文件不需要再运行了，因为数据库中已经有了城市的数据。
"""
import requests
import json
import sqlite3

# 连接数据库
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

url = "http://zhouxunwang.cn/data/?id=104&key=Vb7F+tYwQtX+h5mL+4M3QG/IOwTgsJeZ/pxz7fk&ske=1"
response = requests.get(url)
string = response.text
obj = json.loads(string)

# 提取result
results = obj['result']

for result in results:
    # 省份
    province = result['province']
    print(province)
    # 城市
    citys = result['city']
    for city in citys:
        # 城市
        city_name = city['city']
        print(city_name)
        districts = city['district']
        for district in districts:
            # 区域
            district_name = district['district']
            print(district_name)
            cursor.execute("""
            insert into form_city(`province`, `city`, `district`) values ('{}','{}','{}')
            """.format(province, city_name, district_name))
# 提取省份

cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
