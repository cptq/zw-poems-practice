''' 诗词新学 Poems
    Derek Lim
    call by: python3 poems_practice.py k m
    where k = poem number and m = number of characters omitted
'''
import sys
import random
import os

poems = ['']*20

poems[1] = '''  梦与诗
醉过才知酒浓
爱过才知情重
你不能做我的诗
正如我不能做你的梦
'''

poems[2] = ''' 花非花 
花非花，雾非雾，
夜半来，天明去。
来如春梦几多时？
去似朝云无觅处。
'''

poems[3] = '''  天净沙
枯藤老树昏鸦，
小桥流水平沙，
古道西风瘦马，夕阳西下，
断肠人在天涯。
'''

poems[4] = '''  采葛
彼采葛兮，一日不见，如三月兮。
彼采萧兮，一日不见，如三秋兮。
彼采艾兮，一日不见，如三岁兮。
'''

poems[5] = '''江南可采莲
江南可采莲，
莲叶何田田，
鱼戏莲叶间。
鱼戏莲叶东，
鱼戏莲叶西。
鱼戏莲叶南，
鱼戏莲叶北。
'''

poems[6] = '''  调笑令
胡马，胡马，远放燕支山下。
跑沙跑雪独嘶，东望西望路迷。
迷路，迷路，边草无穷日暮。
'''

poems[7] = '''  渔歌子
西塞山前白鹭飞，桃花流水鳜鱼肥。
青箬笠，绿蓑衣，斜风细雨不须归'''

poems[8] = '''  长命女
春日宴,绿酒一杯歌一遍,再拜陈三愿:
一愿郎君千岁;
二愿妾身长健;
三愿如同梁上燕,
岁岁长相见.
'''

poems[9] = '''  早发白帝城
朝辞白帝彩云间，千里江陵一日还。
两岸猿声啼不住，轻舟已过万重山'''

poems[10] = '''  虞美人
春花秋月何时了，
往事知多少.
小楼昨夜又东风，
故国不堪回首月明中！
雕栏玉砌应犹在，
只是朱颜改。
问君能有几多愁？
恰似一江春水向东流。'''

poems[11] = '''书画琴棋诗酒花
书画琴棋诗酒花,
当年件件不离他;
而今七事都更变,
柴米油盐酱醋茶.
'''

poems[12] = '''  新嫁娘
三日入厨下
洗手作羹汤
未谙姑食性
先遣小姑尝
'''

poems[13] = '''  我侬词
你侬我侬,忒煞情多;
情多处,热如火;
把一块泥,捻一个你,塑一个我,
将咱两个一齐打破,用水调和;
再捻一个你,再塑一个我.
我泥中有你,你泥中有我;
我与你生同一个衾,死同一个椁.
'''


if __name__ == '__main__':
    os.system('clear')
    if len(sys.argv) > 1:
        k = int(sys.argv[1])
    else:
        k = random.randint(7,13)
    if len(sys.argv) > 2:
        to_omit = int(sys.argv[2])
    else:
        to_omit = 10
    p = poems[k]
    orig_p = p
    count = 0
    while to_omit > 0 and count < 3000:
        r = random.randint(0,len(p)-1)
        triv_set = {'.', ',', ';', ':', ' ',
                 '\n', '*', '，', '.', '。'}
        if p[r] not in triv_set:
            p = p[:r] + '*' + p[r+1:]
            to_omit -= 1
        count += 1
    print(p)
    input("Enter to reveal\n")
    print(orig_p)


