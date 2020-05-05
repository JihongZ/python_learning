print("------这是一个文字游戏--------")
temp = input("请你猜一个我心中的数字：")
guess = int(temp) #改变成整形integer
if guess == 8:
    print("Jihong:\t我猜中啦！你心里想的是8!!")
    print("Jihong:\t猜中了也没有奖励啦~~")
else:
    if guess > 8:
        print("大了")
    else:
        print("小了")
print("不玩啦！学习代码去了!")