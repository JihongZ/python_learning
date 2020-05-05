import random
# Write your code here
print("你好，读者")

readername = input("你的名字是? ")

print("你好, " + readername)

names = ["明", "红", "克", "阿强", "无心"]
places = ["水晶城", "龙城", "机械王国", "海龙殿", "伏虎山", "龙虎山"]
roles = ["骑士", "盗贼", "道士", "小和尚", "剑客"]
quests = ["寻找丢失宝藏的下落", "拯救心爱的人", "偷取国家宝藏", "刺杀无道的昏君"]

randomname = random.choice(names)
randomplace = random.choice(places)
randomrole = random.choice(roles)
randomquest = random.choice(quests)

# first paragraph
story_p1 = "很久很久以前，有一个" + randomrole + "名叫 " + randomname + "道人 。他的故乡在" + randomplace + "。有一天他被上天赋予了一个使命 -- " + randomquest +"。从此他踏上了冒险的旅程。\n"

places2 = ["黑风寨", "销魂窟", "三杯倒", "恶人谷"]
villiagestyles = ["凶恶", "懒散", "彪悍", "油滑"]
events = ["一位英姿飒爽的女侠客从旁边路过", 
"一位癞头和尚从路边向他招呼", 
"一位不知从哪冒出来的穷道士意味深长的喊了一身\"道友且慢\""]

randomplace2 = random.choice(places2)
randomvilliagestyle = random.choice(villiagestyles)
randomevent = random.choice(events)

# second paragraph
story_p2 = "于是，他先来到了一个叫" + randomplace2 + "的地方。" + "这个地方民风非常的" + randomvilliagestyle + "。他一来到这就感觉和自己的个性非常不和。于是他想赶紧在客栈住一晚第二天就赶紧上路,突然走在路上的他看见" + randomevent + "。"

story = story_p1 + story_p2
print(story)
