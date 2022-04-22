
# name = [1, 2, 3, 4, 5]
#
# p = 10
# while p < 20 :
#     print("数字过小")
#     p += 2
#     print(p)

#
# count = 0
# while (count < 9 ):
#     print("count小于9", count)
#     count = count + 1
# print("count大于9")

# file = input("不妨猜一下我心里想的是哪个数字:")
# number = int(file)
# while number != shuzi:
#     file = input("哎呀猜错了，请重新输入吧！:")
#     number = int(file)
#     if number == shuzi:
#         print("猜对了")
#     else:
#         if number > shuzi:
#             print("嘿！ 偏大了！请重新输入！")
#         else:
#             print("嘿！ 偏小了！请重新输入！")
# import random #随机数
# shuzi = random.randint(0, 10)#0-10内的随机数
# print("请猜一下我心里想的是哪个数字吧")
# ture = input("是否开始：")
# if ture == "是":
#    print("那我们开始吧！")
#    guess = input("输入您将要猜测的数字：")
#    number = int(guess)
#    while (1):
#     guess = input("再次输入您将要猜测的数字：")
#     if number == shuzi:
#         print("恭喜！猜中了！")
#         print("游戏结束！！")
#     else:
#         if number < shuzi:
#             print("差一点了！有点偏小！！")
#         else:
#             print("差一点了！有点偏大！！")
# else:
#     print("好遗憾！")

import random
ran = random.randint(0,9)
temp  = input("请猜一下我心里想的是哪个数字：")
number = int(temp)
if temp == ran:
    print("猜对了！")
else:
    while number != ran:#条件成立
        print("猜错了，再来一次吧！")
        temp = input("请再猜一下我心里想的是哪个数字：")
        number = int(temp)
        if number == ran:
            print("你怎么猜的这么准！！")
        else:
            if number > ran:
                print("嘿！猜大了！")
            else:
                print("嘿！偏小了！")
    print("游戏结束！")