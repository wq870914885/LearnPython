#        i = 1
#        while i <= 10:
#            print(i)
#             i += 1
#            i += 1
      
     
#       sum = 0
#       i = 1
#       while i <= 100:
#           sum = sum + i
#           i += 1
#       print(sum)
     
#  sum = 0
#  for i in range(1,101):
#      sum = sum + i
#  print(sum)
#      Python 练习题：while 循环与循环嵌套
#      总题量：10 道，划分：简单 4 道、一般 4 道、困难 2 道
#      知识点：while循环、循环条件、break、continue、while 循环嵌套
#      简单（4 道）
#      使用 while 循环，依次打印 1～10 的所有整数。
#     i = 1
#     while i <= 10:
#         print(i)
#         i += 1
  
#      使用 while 循环，倒序打印 10～1 的数字。
#    i = 10
#    while i >= 1:
#        print(i)
#        i = i - 1
 
#      利用 while 循环计算 1+2+3+…+100 的总和。
#    sum = 0
#    i = 1
#    while i <= 100:
#        sum = sum+i
#        i = i+1
#    print(sum)
 
#      不断接收用户输入，只要输入内容不是quit就持续输入，输入quit结束循环。
#  answer = 'quit'
#  while True:
#      a = input()
#      if a == answer:
#          break

#      一般（4 道）
#      使用 while 循环输出 1～50 之间所有偶数。
#   i = 1
#   while i <= 50:
#       if i % 2 == 0:
#           print(i)
#       i = i + 1
 
#      猜数字简易程序：预设数字answer=22，while 循环持续接收用户输入，猜对使用 break 跳出循环并提示 “猜对了”。
#   answer = 22
#   while True :
#       a = int(input("Enter a number: "))
#       if a ==answer:
#           break
#   print('猜对了')

#      使用单层 while 循环，输出 1～20 中，不能被 3 整除的数字（使用 continue 实现）。
#  i = 1
#  while i <= 20:
#      if i % 3 != 0:
#          print(i)
#      i += 1

#      while 嵌套基础：使用 while 循环嵌套，打印如下矩形（5 行，每行输出 4 个*）
#      plaintext
#      ****
#      ****
#      ****
#      ****
#      ****
# i = 5
# while i>= 1:
#     print('****')
#     i = i - 1

#      困难（2 道）
#      while 嵌套：打印九九乘法表（正序），要求只用 while 循环实现，不使用 for。
# n = 1
# m = 1
# while n < 10:
#     m = n
#     while m < 10:
#         sum = n * m
#         print(f'{n} x {m} = {sum}',end='\t')
#         m += 1
#     n  += 1
#     print('')

#      编写程序：找出 1～100 以内所有质数，只用 while 循环嵌套实现。


# ============================================================
# 专项练习：break 与 continue（由易到难）
# 总题量：8 道 —— 简单 3 道、一般 3 道、困难 2 道
# 目标：分清 break（结束本层循环）和 continue（跳过本轮剩余代码）
# ============================================================

# ---------- 简单（3 道）----------

# 1. 使用 while 打印 1～10，当打印到 7 时用 break 结束循环。
#    预期输出：1 2 3 4 5 6 7
# i = 1
# while i <= 10:
#     print(i)
#     if i == 7:
#         break
#     i += 1


# 2. 使用 while 打印 1～10，遇到 5 时用 continue 跳过，不打印 5。
#    注意：i 要先加再判断，避免死循环。
#    预期输出：1 2 3 4 6 7 8 9 10
# i = 0
# while i <= 9:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

# 3. 预设密码 password = "1234"，用 while True 不断让用户输入，
#    输入正确则 break 并打印“登录成功”。
# psw = '1234'
# while True :
#     res = input('password:')
#     if res == psw:
#         break
# print('success!')

# ---------- 一般（3 道）----------

# 4. 用 while 累加 1+2+3+…，当总和第一次超过 100 时 break，
#    并打印：最终总和、最后加进去的那个数。
# i = 1
# s = 0
# while True:
#     s = s + i
#     i += 1
#     if s >= 100:
#         break
# print(f'总和：{s}，最后加进的数：{i}')

# 5. 打印 1～30 中的数字，但跳过所有能被 3 或 5 整除的数（用 continue）。
#    预期：不出现 3、5、6、9、10、12、15……
# i = 0
# while i <= 29:
#     i += 1
#     if (i % 3 ==0) or (i % 5 == 0):
#         continue
#     print(i)

# 6. 不断接收用户输入的整数：
#    - 输入 0：break 结束，并打印之前所有正数的总和
#    - 输入负数：用 continue 跳过，不计入总和
#    - 输入正数：累加到总和
# sum = 0
# while True:
#     i = int(input('请输入整数'))
#     if i < 0 :
#         continue
#     if i == 0 :
#         break
#     sum = sum + i
#     print(sum)
# print(f'sum = {sum}')

# ---------- 困难（2 道）----------

# 7. while 嵌套：外层 i=1～5，内层 j=1～5，打印 i 和 j。
#    当 i * j > 10 时，用 break 结束【内层】循环（外层继续）。
#    观察输出，体会：break 只跳出最内层。
# i = 1
# j = 1
# while i <= 5:
#  while j <= 5:
#      if i * j > 10:
#          break
#      print(f'i={i}',end=',')
#      print(f'j={j}')
#
#      j = j + 1
#  i = i + 1
#  j = 1


# 8. 猜数字升级版：
#    预设 answer = 7，最多猜 5 次。
#    - 猜对：打印“猜对了”，break
#    - 猜错：提示“错了，还有 x 次机会”，继续
#    - 5 次都错：循环正常结束后打印“机会用完了”
#    （可选）输入不是数字时用 continue 跳过本次，不消耗次数
i = 5
while True :
    res = input('answer:')
    if res == '7' :
        print('猜对了')
        break
    i = i - 1
    if i <= 0 :
        print('没有机会了')
        break
    print(f'猜错了,还有{i}次机会!')


