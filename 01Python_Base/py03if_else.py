# #20260812
#
# age = 18
# name = 'wq'
# print(f'name:{name}, age:{age}')
#
# a = 1
# a = a +1
# print(a)
# a+=1
# print(a)
#
# Python 练习题：if 判断、比较运算符与逻辑运算符
# 难度划分：简单｜一般｜困难
# 知识点：if/elif/else、比较运算符 > < >= <= == !=、逻辑运算符 and or not
# 一、简单（基础识别、单条件判断）
# 编写程序，输入一个整数，如果数字大于 10，打印大于10，否则打印小于等于10。
# a=int(input())
# if a>10:
#     print("a大于10")
# else:
#     print('a小于等于10')
#
# 输入两个数字 a、b，使用 if 判断，输出两个数中较大的数字。
# a=int(input('a='))
# b=int(input('b='))
# if a>b:
#     print(a)
# else:
#     print(b)

# 接收用户输入年龄，如果年龄 >=18，输出成年，否则输出未成年。

# a=int(input())
# if a>=18:
#     print('成年')
# else:
#     print('未成年')

# 判断变量score = 85，如果 score 等于 100，打印满分，否则打印不是满分。
# score =85
# if score ==100:
#     print('满分')
# else:
#     print('不是满分')

# 二、一般（多条件、逻辑运算符 and/or、elif 分支）
# 输入考试分数（0~100），按规则评级：
# ≥90：优秀；≥80：良好；≥60：及格；其余：不及格。
# a=int(input())
# if a >= 90:          # 注意：要用 >=90，写成 >90 时 90 分会错成「良好」
#     print('优秀')
# elif a >= 80:
#     print('良好')
# elif a >= 60:
#     print('及格')
# else:
#     print('不及格')

# 输入年龄，判断是否可以学车：年龄≥18 并且 年龄≤70，输出可以学车，否则输出不可以学车。
# a=int(input())
# if a>=18 and a<=70:
#     print('可以学车')
# else:
#     print("不可以学车")

# 接收用户名和密码，用户名等于admin 或者 密码等于123456，就打印允许临时登录，否则打印登录失败。
# name=input('name:')
# pwd=input('password:')
# if name == 'admin' or pwd == '123456':
#     print('可以登录')
# else:
#     print('登录失败')

# 给定数字 num，满足：大于 0 并且 不能等于 5，打印符合条件，否则打印不符合条件。
# num=int(input('num='))
# if num>0 and num !=5:
#     print('num=%d,符合条件' %num)
# else:
#     print('不符合条件')

# 三、困难（多层判断、not、复杂逻辑组合、边界条件思考）
# 输入三个整数 a、b、c，使用 if 判断输出三个数里的最大值（不允许直接使用 max 函数）。
# 你原来用 > 时，若出现相等（如 5 5 3）可能误选到 c。改成 >= 更稳。
# a = int(input('a='))
# b = int(input('b='))
# c = int(input('c='))
# if a >= b and a >= c:
#     print(a)
# elif b >= a and b >= c:
#     print(b)
# else:
#     print(c)

# 会员购票规则：
# 票价原价 100 元。
# 条件 A：年龄小于 12 岁 或者 大于 65 岁 → 半价
# 条件 B：拥有会员标识（is_vip=True），并且 不满足条件 A → 8 折
# 其余情况原价
# 编写程序，输入年龄、传入 is_vip 变量，计算最终票价。
# 思路：先判断 A，再判断 B，最后才是原价；题目要的是「最终票价」，不只是打印半价/8折。
# age = int(input('age='))
# vip = input('是会员吗？输入 yes 或 no：')
# is_vip = (vip == 'yes')   # 输入 yes 则为 True，否则 False
# price = 100
# if age < 12 or age > 65:       # 条件 A：半价
#     price = 50
# elif is_vip:                  # 条件 B：不满足 A，且是会员 → 8 折
#     price = 80
# else:
#     price = 100
# print('最终票价：', price)

# 编写程序判断闰年：
# 闰年规则：能被 4 整除但不能被 100 整除，或者 能被 400 整除。输入年份，输出是否为闰年。
# % 是取余：year % 4 == 0 表示能被 4 整除
# year = int(input('请输入年份：'))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('是闰年')
# else:
#     print('不是闰年')

# 模拟门禁系统：
# 开门条件：
# （刷卡有效 card_ok=True 并且 人脸验证通过 face_ok=True）
# 或者
# 管理员密钥 admin_key=True
# 使用 if + and/or 组合逻辑，输出能否开门。
# 第三节课先用固定 True/False 练习逻辑；以后再改成 input 也行。
# card_ok = True
# face_ok = True
# admin_key = False
# if (card_ok and face_ok) or admin_key:
#     print('可以开门')
# else:
#     print('不能开门')
