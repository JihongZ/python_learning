import random

print("------这是一个文字游戏2--------")

temp = input("请你猜一个我心中的数字：")
guess = int(temp)
secret = random.randint(1, 10)

# first guess
if guess == secret:
        print("你猜中啦！正确答案是" + str(secret) + "!!!!")
        print("猜中了也没有奖励啦~~")
else:
    if guess > secret:
        print("大了")
    else:
        print("小了")

error_num = 1

while guess != secret and error_num < 3:
    error_num += 1
    temp = input("猜错了，请重新输入：")
    guess = int(temp) #改变成整形integer
    if guess == secret:
        print("你猜中啦！正确答案是" + str(secret) + "!!!!")
        print("猜中了也没有奖励啦~~")
    else:
        if guess > secret:
            print("大了")
        else:
            print("小了")
print("你一共猜了" +  str(error_num) + "次")
