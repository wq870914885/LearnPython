# # # # # # # i = 1
# # # # # # # while i <= 10:
# # # # # # #     print(i)
# # # # # # #     # i += 1
# # # # # # #     i += 1
# # # # # # #
# # # # # #
# # # # # # sum = 0
# # # # # # i = 1
# # # # # # while i <= 100:
# # # # # #     sum = sum + i
# # # # # #     i += 1
# # # # # # print(sum)
# # # # # #
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)
# # # # # Python 练习题：while 循环与循环嵌套
# # # # # 总题量：10 道，划分：简单 4 道、一般 4 道、困难 2 道
# # # # # 知识点：while循环、循环条件、break、continue、while 循环嵌套
# # # # # 简单（4 道）
# # # # # 使用 while 循环，依次打印 1～10 的所有整数。
# # # # i = 1
# # # # while i <= 10:
# # # #     print(i)
# # # #     i += 1
# # #
# # # # # 使用 while 循环，倒序打印 10～1 的数字。
# # # i = 10
# # # while i >= 1:
# # #     print(i)
# # #     i = i - 1
# #
# # # # # 利用 while 循环计算 1+2+3+…+100 的总和。
# # # sum = 0
# # # i = 1
# # # while i <= 100:
# # #     sum = sum+i
# # #     i = i+1
# # # print(sum)
# #
# # # # # 不断接收用户输入，只要输入内容不是quit就持续输入，输入quit结束循环。
# answer = 'quit'
# while True:
#     a = input()
#     if a == answer:
#         break
#
# # # # # 一般（4 道）
# # # # # 使用 while 循环输出 1～50 之间所有偶数。
# # i = 1
# # while i <= 50:
# #     if i % 2 == 0:
# #         print(i)
# #     i = i + 1
# #
# # # # # 猜数字简易程序：预设数字answer=22，while 循环持续接收用户输入，猜对使用 break 跳出循环并提示 “猜对了”。
# # answer = 22
# # while True :
# #     a = int(input("Enter a number: "))
# #     if a ==answer:
# #         break
# # print('猜对了')

# # # # # 使用单层 while 循环，输出 1～20 中，不能被 3 整除的数字（使用 continue 实现）。
# i = 1
# while i <= 20:
#     if i % 3 != 0:
#         print(i)
#     i += 1
# # # # # while 嵌套基础：使用 while 循环嵌套，打印如下矩形（5 行，每行输出 4 个*）
# # # # # plaintext
# # # # # ****
# # # # # ****
# # # # # ****
# # # # # ****
# # # # # ****
# # # # # 困难（2 道）
# # # # # while 嵌套：打印九九乘法表（正序），要求只用 while 循环实现，不使用 for。
# # # # # 编写程序：找出 1～100 以内所有质数，只用 while 循环嵌套实现。