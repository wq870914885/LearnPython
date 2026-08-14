# 函数是组织好的、可重复使用的、用来实现特定功能的代码片段
# 定义函数
# def 函数名（参数列表）：
#     函数体
#     ......
#     return 返回值
# 调用函数
# 函数名（参数）

# 定义函数
# def out_line():
#     print('------------------------')
# 调用函数
# out_line()

# 计算圆的面积
# def circle_area(r):
#     area = 3.14 * r * r
#     return area
# 调用函数
# c_area = circle_area(5)
# print(c_area)

# 多个返回值,封装到元组中
# def circle_area_len(r):
#     '''
#     函数的功能
#     :param r: 函数的参数的含义
#     :return:  函数的返回值代表什么
#     '''
#     return round(3.14 * r * r,1),round(2 * 3.14 * r,1) # round保留小数位
# al = circle_area_len(10)
# print(al)
#
# area, len = circle_area_len(10) # 解包元组
# print(area, len)

# 函数的调用，栈结构 LIFO 后进先出
# def fuction_a():
#     print('fuction_a ... befor')
#     function_b()
#     print('fuction_a ... after')
# def function_b():
#     print('function_b ... befor')
#     function_c()
#     print('function_b ... after')
# def function_c():
#     print('function_c')
#
# fuction_a()

# 1.定义一个函数:根据传入的底和高计算三角形面积的函数(3三角形面积=底*高/2)。
# def tri_area(base , height):
#     area = base * height / 2
#     return area
#
# result = tri_area(5, 5)
# print(f'三角形的高为面积为：{result}')

# 2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)。
# def str_vow(s):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     num = 0
#     for i in s :
#         for j in vowels :
#             if i == j :
#                 num = num + 1
#     return num
# str = input('请输入字符串')
# print(f'元音字母的个数为{str_vow(str)}')

# 3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)并返回。
# def score(list):
#     list.sort()
#     min = list[0]
#     list.reverse()
#     max = list[0]
#     sum = 0
#     for i in list:
#         sum = sum + i
#     ave = round(sum / len(list),1)
#     return max, min, ave
#
# list = [45,56,74,87,32,99,90,100,57,95,86,84,86,95,65,75,79]
# result = score(list)
# print(result)
#
# scores = [45, 56, 74, 87, 32]
#
# max(scores)   # 最大值 → 87
# min(scores)   # 最小值 → 32
# sum(scores)   # 求和   → 294
# len(scores)   # 个数   → 5（你应该已经用过）

# 1.定义一个函数,根据传入的分数,计算对应的分数等级并返回。
# 分数>=90:A
# 分数>=75:B
# 分数>=60:C
# 分数<60:D
# def score_lev(score):
#     if score >= 90:
#         s_lev = 'A'
#     elif score >= 75:
#         s_lev = 'B'
#     elif score >= 60:
#         s_lev = 'C'
#     else:
#         s_lev = 'D'
#     return s_lev
#
# score = round(float(input('请输入分数：')),1)
# res = score_lev(score)
# print(f'分数等级为：{res}')

# 2.定义一个函数,用于判断一个字符串是否是回文串,返回bool值。
# 把字符串反转,如果和原字符串相同,就是回文串。(如:"1evel","radar","黄山落叶松叶落山黄")
def main(str1):
    str2 = str1.reverse()
    if str2 == str1 :
        return True
    else:
        return False
str1 = input('输入字符串，判断是否是回文串：')
print(type(str1))
print(main(str1))
# 3.定义一个函数:完成时间转换功能,将传入的秒转换为小时、分钟、秒。
# 4.定义一个函数:根据传入的三角形三个边的边长,判定三角形的类型(等边、等腰、普通,或者不能构成三角形)。