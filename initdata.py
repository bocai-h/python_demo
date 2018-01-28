# coding=utf-8
# 记录
bob = { 'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev' }
sue = { 'name': 'Sue Jones', 'age': 45, 'pay': 4000, 'job': 'hdw' }
tom = { 'name': 'Tom', 'age': 50, 'pay': 0, 'job': None }

# 数据库

db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__': #作为脚本运行时
    for key in db:
        print(key + '=>')
        print(db[key])