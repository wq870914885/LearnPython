# li = [1,2,3,4,'a','a','b','b','c','c']
# print(li)
# print(li,type(li))
# print(li[2])
# print(li[0:3])
# for i in li:
#     print(i)    #列表可遍历
#

#列表常见操作
 #新增,添加元素
 #append() extend() insert()
# li = ['one','two','three']
# li.append('four')   #['one', 'two', 'three', 'four']
# li.extend('four')   #分散添加     ['one', 'two', 'three', 'f', 'o', 'u', 'r']
# li.insert(3,'four')     #指定位置插入元素     ['one', 'two', 'three', 'four']
# li.insert(0,'four')     #指定位置如果有元素,原有元素就会往后移    ['four', 'one', 'two', 'three']
# print(li)

#修改元素
#通过下标就可以进行修改
# li = [1,2,3]
# print(li[1])
# li[1] = 'a'
# print(li)

#查询
#in     判断指定元素是否存在列表中,存在返回true,不存在返回false
#not in     与in相反
# li = ['a','b','c','d']
# print('b'in li)     #True
# print('1'in li)     #False

#用户输入昵称,重复则不能使用
# name_list = ['Bob','Peter','Jhon']
# name = input('请输入昵称')
# if name in name_list:
#     print(f'{name}昵称已经存在!')
# else:
#     print('昵称可以使用!')
#     name_list.append(name)
# print(name_list)

#index  返回数据所在位置的下标,不存在则报错
#count  统计指定数据在当前列表出现的次数

#删除
#del
# li = ['a','b','c','d']
# del li  #删除列表
# del li[2]   #根据下标删除     ['a', 'b', 'd']
# print(li)

#pop    删除指定下标的数据,默认删除最后一个元素
# li = ['a','b','c','d']
# li.pop()    #['a', 'b', 'c']
# li.pop(2)   #['a', 'b', 'd']
# print(li)

#remove     根据元素的值进行删除
# li = ['a','b','c','d']
# li.remove('a')      #['b', 'c', 'd']
#默认删除最开是出现的指定元素
# print(li)

#排序
# sort 将列表按特定顺序从新排列,默认从小到大
# li = [1,4,2,5,3,6]
# li.sort()   #按照从小到大顺序排序     [1, 2, 3, 4, 5, 6]
# print(li)

#reverse 倒序,将列表倒置
# li = [1,4,2,5,3,6]
# li.reverse()    #[6, 3, 5, 2, 4, 1]
# print(li)

# 列表推导式
# 1 表达式 for 变量 in 列表
# li = [1,2,3,4,5,6]
# [print(i) for i in li]      #1 2 3 4 5 6
# [print(i * 5) for i in li]      #5 10 15 20 25 30

# li = []
# for i in range(1,6):
#     # print(i)
#     li.append(i)
# print(li)

# li = []
# [li.append(i) for i in range(1,6)]  #[1, 2, 3, 4, 5]
# print(li)

# 2 [表达式 for 变量 in 列表 if 条件]
# 把奇数放进列表里
# li = []
# [li.append(i) for i in range(1,6) if i % 2 != 0]    #[1, 3, 5]
# print(li)

#列表嵌套
#一个列表里面又有一个列表
# li = [1,2,3,[4,5,6]]
# print(li[3])    #   [4, 5, 6]
# print(li[3][0])    #    4


# ============================================================
# 专项练习：列表（list）由易到难
# 总题量：10 道 —— 简单 4 道、一般 4 道、困难 2 道
# 对应本章：增删改查、遍历、排序、推导式、列表嵌套
# ============================================================

# ---------- 简单（4 道）----------

# 1. 创建一个列表 fruits = ['apple', 'banana', 'orange']
#    - 打印整个列表
#    - 打印下标为 1 的元素
#    - 用切片打印前两个元素
#    - 用 for 遍历打印每个水果

# fruits = ['apple', 'banana', 'orange']
# print(fruits)
# print(fruits[1])
# print(fruits[0:2])
# for fruit in fruits:
#     print(fruit)


# 2. 有列表 nums = [10, 20, 30]
#    - 用 append 在末尾加 40
#    - 用 insert 在下标 0 插入 5
#    - 把下标 2 的元素改成 99
#    - 每步操作后都 print 一次，观察变化

# nums = [10, 20, 30]
# nums.append(40)
# print(nums)
# nums.insert(0,5)
# print(nums)
# del nums[2]
# nums.insert(2,99)
# print(nums)

# 3. 有列表 names = ['Tom', 'Jerry', 'Spike']
#    接收用户输入一个名字：
#    - 若 in 列表中：打印“已存在”
#    - 若不在：append 进去，并打印“添加成功”和新列表

# names = ['Tom', 'Jerry', 'Spike']
# while True:
#     res = input('请输入名字:')
#     if res in names:
#         print('已存在')
#     else:
#         names.append(res)
#         break
# print('success')
# print(names)

# 4. 有列表 li = ['a', 'b', 'c', 'd', 'b']
#    - 用 index 查出第一次出现 'b' 的下标
#    - 用 count 统计 'b' 出现几次
#    - 用 remove 删除一个 'b'，再 print 列表

# li = ['a', 'b', 'c', 'd', 'b']
# print(li.index('b'))
# print(li.count('b'))
# li.remove('b')
# print(li)

# ---------- 一般（4 道）----------

# 5. 有列表 scores = [88, 92, 75, 60, 95]
#    - 用 pop() 删掉最后一个，并打印被删掉的值
#    - 用 del 删除下标 1 的元素
#    - 用 sort 从小到大排序并打印
#    - 再用 reverse 倒置并打印
# scores = [88, 92, 75, 60, 95]
# scores.pop()
# print(scores)
# del scores[1]
# print(scores)
# scores.sort()
# print(scores)
# scores.reverse()
# print(scores)

# 6. 不断让用户输入商品名加入购物车列表 cart（初始为空列表）：
#    - 输入 'q' 时 break 结束
#    - 若商品已在 cart 中（用 in），提示“已添加过”，不要重复 append
#    - 结束循环后打印购物车
# cart = []
# while True:
#     res = input('请输入商品名:')
#     if res == 'q':
#         break
#     if res in cart:
#        print('已添加过')
#     else:
#         cart.append(res)
# print(cart)

# 7. 用列表推导式完成：
#    - 生成 1～10 的列表
#    - 生成 1～10 中所有偶数的列表
#    - 生成 1～10 每个数乘以 3 的列表
#    （可先用普通 for + append 写一遍，再用推导式写一遍）
# li = []
# [li.append(i) for i in range(0,11)]
# print(li)
# li = []
# [li.append(i) for i in range(0,11) if i%2==0]
# print(li)
# li = []
# [li.append(i*3) for i in range(0,11)]
# print(li)

# 8. 有嵌套列表 classroom = [['张三', '李四'], ['王五', '赵六'], ['钱七']]
#    - 打印第二个小组（下标 1）
#    - 打印第二个小组里的第一个人
#    - 用嵌套 for 遍历，打印每一个名字
# classroom = [['张三', '李四'], ['王五', '赵六'], ['钱七']]
# print(classroom[1])
# print(classroom[1][0])
# for i in classroom:
#     for j in i :
#         print(j)

# ---------- 困难（2 道）----------

# 9. 班级成绩：scores = [55, 72, 88, 91, 60, 45, 78]
#    要求：
#    - 用列表推导式得到“及格名单”（>=60）和“不及格名单”（<60）
#    - 对及格名单 sort 排序
#    - 打印：及格人数、不及格人数、及格最高分、及格最低分
#      （最高/最低可用排序后取下标，或 max/min）
# scores = [55, 72, 88, 91, 60, 45, 78]
# res_good = []
# res_bad = []
# [res_good.append(i) for i in scores if i >= 60]
# print(res_good)
# [res_bad.append(i) for i in scores if i < 60]
# print(res_bad)
# res_good.sort()
# print(res_good)
# print(f'及格人数:{len(res_good)}')
# print(f'不及格人数:{len(res_bad)}')
# res_good.reverse()
# print(f'及格最高分:{res_good[0]}')
# res_good.sort()
# print(f'及格最低分:{res_good[0]}')

# 10. 简易通讯录（列表嵌套）：
#     contacts = [['张三', '13800001111'], ['李四', '13900002222']]
#     菜单循环（while True）：
#     1 → 添加联系人（姓名、电话），若姓名已存在则提示不可重复
#     2 → 按姓名查询，打印电话；找不到提示“无此人”
#     3 → 按姓名删除（可用循环找下标再 pop，或按你学过的方式）
#     4 → 打印全部联系人
#     0 → break 退出
contacts = [['张三', '13800001111'], ['李四', '13900002222']]
while True :
    name = input('姓名:')
    if name == 'q' :
        print('已退出录入系统')
        break
    tel = input('电话:')
    exists =False
    for i in contacts :
        j = i[0]
        if name == j:
           print('名字重复,添加失败')
           exists = True
           break
    if not exists :
           contacts.append([name,tel])
    print(contacts)

res_name = input('输入名字查询电话:')
for i in contacts :
    j = i[0]
    exists = False
    if res_name == j :
        print(f'电话:{i[1]}')
        exists = True
        break
if exists == False :
    print('不存在此人')

#删除
name = input('输入需要删除的姓名：')
for i in contacts :
    j = i[0]
    print(f'{i}')
    if name == j :
        print('存在一样的')
        contacts.remove(i)
        print('删除成功！')
        break
print(contacts)