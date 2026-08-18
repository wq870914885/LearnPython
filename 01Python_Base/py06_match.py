# if
# day = input('请输入星期几（1-7：）')
# if day == '1':
#     print('周一：工作会议日')
# elif day == '2':
#     print('周二：学习培训日')
# elif day == '3':
#     print('周三：项目开发日')
# elif day == '4':
#     print('周四：代码审查日')
# elif day == '5':
#     print('周五：总结规划日')
# elif day == '6'or day == '7':
#     print('周末：休息放松')
# else:
#     print('输入错误')

# match
# day = input('请输入星期几（1-7：）')
# match day:
#     case '1':
#         print('周一：工作会议日')
#     case '2':
#         print('周二：学习培训日')
#     case '3':
#         print('周三：项目开发日')
#     case '4':
#         print('周四：代码审查日')
#     case '5':
#         print('周五：总结规划日')
#     case '6'|'7':
#         print('周末：休息放松')
#     case _ :  # 匹配其他所有条件
#         print('输入错误')

# 简易计算器
# num1 = int(input('请输入第一个数：'))
# num2 = int(input('请输入第二个数：'))
# sym = input('请输入运算符（+、-、*、/）:')
# res = 0
# match sym :
#     case '+' :
#         res =num1+num2
#         print(res)
#     case '-' :
#         res =num1-num2
#         print(res)
#     case '*' :
#         res =num1*num2
#         print(res)
#     case '/' :
#         res =num1/num2
#         print(res)
#     case _:
#         print('运算符输入错误！')

# num1 = float(input('请输入第一个数：'))
# num2 = float(input('请输入第二个数：'))
# sym = input('请输入运算符（+、-、*、/）:')
# match sym :
#     case '+' :
#         print(f'{num1} + {num2} = {num1+num2}')
#     case '-' :
#         print(f'{num1} - {num2} = {num1-num2}')
#     case '*' :
#         print(f'{num1} * {num2} = {num1*num2}')
#     case '/' if num2 != 0:
#         print(f'{num1} / {num2} = {num1/num2}')
#     case _:
#         print('操作不支持！')
#

# 需求：根据输入的用户名密码执行登录操作：
# 正确的用户名和密码为admin/666888，zhangsan/123456，taoge/888666
# 输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
# 输入的用户名和面不能为空
# 登录成功：输出‘登录成功，进入B站首页’
# 登录失败：输出‘用户名或密码错误，请重新输入’
dict = {'admin':'666888','zhangsan':'123456','taoge':'888666'}
while True:
    name = input('请输入姓名：')
    pwd = input('请输入密码：')
    if name == '' or pwd == '':
        print('用户名和密码不能为空！')
        continue
    for key,value in dict.items():
        if name == key and pwd == value:
            print('登录成功，进入B站首页')
            res = True
            break
        else:
            print('用户名或密码错误，请重新输入！')
            res = False
            break
    if res == True:
        break
    else:
        continue