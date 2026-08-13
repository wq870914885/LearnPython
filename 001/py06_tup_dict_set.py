# 元组
# tup = (1,2,3,4,5)
# print(tup)
# print(type(tup))

# 元组和列表的区别
# 元组只支持查询，不支持增删改
# li = [1,2,3]
# li[1] = 'a'
# print(li)
# tup = (1,2,3)
# print(tup[2])   # 3
# tup[2] = 'a'
# print(tup)  # TypeError: 'tuple' object does not support item assignment
            # 不支持修改
# print(tup.index(1))

# 应用场景
# 函数的参数和返回值
# 格式化输出后面的小括号（）本质上就是一个元组

# 字典 dict
# dic = {'name':'wq','age':'18'}
# print(dic)
# print(type(dic))

# 字典常见操作
# 查看元素
# dic = {'name': 'wq', 'age': 18}
# print(dic['name'])
# print(dic['age'])
# print(dic.get('name'))
# print(dic.get('w','不存在'))   # 如果没有键名，返回自己设置的默认值‘不存在’

# 修改元素
# dic = {'name': 'wq', 'age': 18}
# dic['age'] = 20
# print(dic)

# 添加元素
# dic = {'name': 'wq', 'age': 18}
# 键名存在就修改，不存在就新增
# dic ['tel'] = '123123'
# print(dic)
# dic = {'name': 'wq', 'age': 18}

# 删除元素
# del 删除整个字典
# dic = {'name': 'wq', 'age': 18}
# del dic
# print(dic)  # NameError: name 'dic' is not defined. Did you mean: 'dir'?
            # 字典已被删除
# del 删除指定键值对，键名不存在会报错
# dic = {'name': 'wq', 'age': 18}
# del dic['age']
# print(dic)

# clear 清空整个字典里面的东西，但保留字典
# dic = {'name': 'wq', 'age': 18}
# dic.clear()
# print(dic)  # {}

# pop 删除指定键值对，键不存在就会报错
# dic = {'name': 'wq', 'age': 18}
# dic.pop('name')  # {'age': 18}
# dic.pop()   #报错，没有指定键名
# dic.popitem()   # 删除最后一个
# print(dic)

# len 求长度
# dic = {'name': 'wq', 'age': 18}
# print(len(dic)) # 2

# # keys(): 返回字典里面包含的所有键名
# dic = {'name': 'wq', 'age': 18}
# print(dic.keys())   # dict_keys(['name', 'age'])
# for i in dic.keys() :
#     print(i)
# # values(): 返回字典里面包含的所有值
# print(dic.values()) # dict_values(['wq', 18])
# for i in dic.values() :
#     print(i)
# # items(): 返回字典里面包含的所有键值对
# print(dic.items())
# for i in dic.items() :
#     print(i)

# 字典的应用场景
# 使用键值对存储描述一个物体的相关信息

# 集合 set
# s1 = {1,2,3}
# print(s1)
# print(type(s1))
# 集合具有无序性
# s1 = {'a','b','c','d'} # 每次运行结果都不一样
# print(s1)   # 每次运行结果都不一样

# 集合无需的实现方式涉及哈希表

# 无序性

# 唯一性
# s1 = {1,2,3,2,3,4,5,6,5}
# print(s1)   # {1, 2, 3, 4, 5, 6}

# 集合的常见操作
# 添加
# add 添加的是一个整体
# s1 = {1,2,3,2,3,4,5,6,5}
# print(s1)
# s1.add(90)
# print(s1)

# update 把传入的元素拆分，一个个放进集合中
# s1 = {1,2,3}
# s1.update('567')    # update里面放可迭代的，：字符串、列表、元组
# print(s1)

# 删除
# remove 选择删除的元素，如果集合中有就删除，没有就报错
# s1 = {1,2,3,4}
# s1.remove(3)
# print(s1)

# pop
# s1 = {'a','b','c','d'}
# s1.pop()    # 随机排序后删除第一个
# print(s1)

# discard 选择要删除的元素，有就会删除，没有则不会有改变
# s1 = {1,2,3,4}
# print(s1)
# s1.discard(5)
# print(s1)
# s1.discard(3)
# print(s1)

# 交集和并集
# 交集 &
# 共有的部分
# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# s3 = {5,6,7,8}
# print(s1 & s2)  # {3, 4}
# print(s1 & s3)  # set() 返回空集合

# 并集 |
# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# print(s1 | s2)  # {1, 2, 3, 4, 5, 6}


# ============================================================
# 专项练习：元组 / 字典 / 集合 由易到难
# 总题量：10 道 —— 简单 4 道、一般 4 道、困难 2 道
# 对应本章：元组只读、字典增删改查与遍历、集合去重与交并集
# ============================================================

# ---------- 简单（4 道）----------

# 1. 创建一个元组 point = (10, 20, 30)
#    - 打印整个元组和类型 type(point)
#    - 打印下标为 1 的元素
#    - 用 index 查出 30 的下标
#    - （选做）尝试执行 point[0] = 99，观察报错信息，用注释写一句结论
# point = (10, 20, 30)
# print(point)
# print(type(point))
# print(point[1])
# print(point.index(30))

# 2. 有字典 student = {'name': '小明', 'age': 18, 'score': 90}
#    - 用 [] 打印 name
#    - 用 get 打印 age
#    - 用 get 查询不存在的键 'tel'，默认值设为「暂无」
#    - 把 score 改成 95，再新增键 'city' 值为 '上海'，最后 print 整个字典
# student = {'name': '小明', 'age': 18, 'score': 90}
# print(student['name'])
# print(student.get('age'))
# print(student.get('tel','暂无'))
# student['score'] = 95
# student['city'] = '上海'
# print(student)

# 3. 有字典 info = {'a': 1, 'b': 2, 'c': 3}
#    - 用 keys() 遍历打印所有键
#    - 用 values() 遍历打印所有值
#    - 用 items() 遍历，打印「键:值」格式（如 a:1）
# info = {'a': 1, 'b': 2, 'c': 3}
# print(info.keys())
# for i in info.keys():
#     print(i)
# print(info.values())
# for i in info.values():
#     print(i)
# print(info.items())
# for i in info.items():
#     print(i)

# 4. 有列表 nums = [1, 2, 2, 3, 3, 3, 4]
#    - 转成集合，观察去重效果并打印
#    - 再用 add 添加 5，用 update 添加 'ab'（观察拆分效果）
#    - 打印最终集合（注意：集合无序，每次打印顺序可能不同）
# nums = [1, 2, 2, 3, 3, 3, 4]
# s1 = set(nums)
# print(s1)
# s1.add(5)
# s1.update('ab')
# print(s1)

# ---------- 一般（4 道）----------

# 5. 有字典 user = {'name': 'Tom', 'age': 20, 'city': '北京'}
#    - 用 pop 删除 'age'，并打印被删掉的值
#    - 用 del 删除 'city'
#    - 用 popitem 删除一对键值，并打印被删内容
#    - 用 clear 清空字典，打印结果
#    - 每步后都 print 一次 user，观察变化
# user = {'name': 'Tom', 'age': 20, 'city': '北京'}
# name = user['age']
# user.pop('age')
# print(name)
# del user['city']
# user.popitem()
# print(user)
# user.clear()
# print(user)

# 6. 简易通讯录（只用字典，不用列表嵌套）：
#    contacts = {'张三': '13800001111', '李四': '13900002222'}
#    接收用户输入姓名：
#    - 若姓名 in contacts：打印对应电话
#    - 若不在：提示「无此人」，再让用户输入电话，添加进字典并打印「添加成功」和整个字典
# contacts = {'张三': '13800001111', '李四': '13900002222'}
# contacts.keys()
# res = input('请输入姓名：')
# for i in contacts.keys():
#     if res == i:
#         print(f'姓名{i}已存在,电话：{contacts[i]}')
#         break
#     else:
#         print('无此人，请输入电话：')
#         tel = input()
#         contacts[res] = tel
#         print('添加成功')
#         print(contacts)
#         break

# 7. 有两个集合：
#    math = {'小明', '小红', '小刚', '小丽'}
#    english = {'小红', '小刚', '小华', '小强'}
#    - 打印两门课都选的人（交集 &）
#    - 打印至少选了一门的人（并集 |）
#    - 用 remove 从 math 中删除「小明」（存在才删）
#    - 用 discard 尝试从 english 中删除「不存在的人」，确认不报错
#    - 打印操作后的两个集合
# math = {'小明', '小红', '小刚', '小丽'}
# english = {'小红', '小刚', '小华', '小强'}
# print(math & english)
# print(math | english)
# math.remove('小明')
# english.discard('小明')
# print(math)
# print(english)

# 8. 接收用户输入一串字符（如 hello），完成：
#    - 用集合统计「有哪些不重复字符」，并打印
#    - 用字典统计「每个字符出现次数」：键为字符，值为次数
#      提示：遍历字符串，若字符不在字典中则设为 1，若在则 +1
#    - 最后打印这个字典
# res= input('请输入一串字符：')
# print(res)
# print(type(res))
# tes = set()
# print(tes)
# tes.update(res)
# print(tes)
#
# dic1 = {}
# for i in res:
#     if i in dic1 :
#         dic1[i] += 1
#     else:
#         dic1[i] = 1
# print(dic1)

# ---------- 困难（2 道）----------

# 9. 成绩管理（字典嵌套）：
#    class_scores = {
#        '张三': {'语文': 85, '数学': 92, '英语': 78},
#        '李四': {'语文': 70, '数学': 88, '英语': 95},
#        '王五': {'语文': 90, '数学': 76, '英语': 80},
#    }
#    要求：
#    - 打印「李四」的数学成绩
#    - 给「张三」新增科目 '物理': 88
#    - 遍历所有学生，打印：姓名、三科（或更多）总分、平均分
#      （可用 values() 取分数再求和）
#    - 找出平均分最高的学生姓名并打印
class_scores = {
       '张三': {'语文': 85, '数学': 92, '英语': 78},
       '李四': {'语文': 70, '数学': 88, '英语': 95},
       '王五': {'语文': 90, '数学': 76, '英语': 80},
}
print(class_scores['李四']['数学'])
class_scores['张三']['物理'] = 88
dict_new = {}
for students in class_scores.items() :
    # print(students)
    # print(type(students))
    nums = 0
    ave = 0
    name = students[0]
    # print(name)
    value = students[1]
    # print(value)
    for score in value.values() :
        # print(score)
        nums = nums + score
    ave = nums / len(value)
    print(f'姓名：{name}',end='\t')
    print(f'总分：{nums}',end='\t')
    print(f'平均分：{ave}')
    dict_new[name] = ave
# print(dict_new)
max_name =''
max_score = 0
for name, score in dict_new.items() :
    if score > max_score :
        max_name = name
        max_score = score
print(f'最高分数为{max_name}，平均分{max_score}')
# 10. 点餐系统（综合：字典 + 集合 + 元组）：
#     menu = {
#         '红烧肉': 38,
#         '西红柿蛋汤': 18,
#         '米饭': 2,
#         '可乐': 5,
#     }
#     菜单循环（while True）：
#     1 → 查看菜单：遍历 menu.items() 打印「菜名 价格元」
#     2 → 点菜：输入菜名
#         - 不在菜单：提示「没有这道菜」
#         - 在菜单：加入订单列表 order，每条订单用元组保存 (菜名, 价格)
#     3 → 查看订单：打印 order；用集合打印「去重后的已点菜名」
#     4 → 结账：计算总价并打印，然后 clear 订单相关数据（或直接 break）
#     0 → break 退出
#     提示：order 初始为 []；集合可用 set() 从订单里收集菜名

