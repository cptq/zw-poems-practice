''' 诗词新学 Poems
    Derek Lim
    call by: python3 poems_practice.py k m
    where k = poem number and m = number of characters omitted
'''
import sys
import random
import os

poems = ['']*30

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

poems[14] = ''''''

poems[15] = '''  七步诗
煮豆燃豆萁，
豆在釜中泣。
本是同根生，
相煎何太急？
'''

poems[16] = '''  枫桥夜泊
月落乌啼霜满天，江枫渔火对愁眠。
姑苏城外寒山寺，夜半钟声到客船。
'''

poems[17] = '''  卜算子
我住长江头，君住长江尾。
日日思君不见君，共饮长江水。
此水几时休？此恨何时已？
只愿君心似我心，定不负相思意。
'''

poems[18] = ''' 游子吟
慈母手中线，游子身上衣。
临行密密缝，意恐迟迟归。
谁言寸草心，报得三春晖。
'''

poems[19] = '''  偶然
我是天空里的一片云，
偶尔投影在你的波心
你不必讶异，
更无须欢喜
在转瞬间消灭了踪影。
你我相逢在黑夜的海上，
你有你的，我有我的方向；
你记得也好，
最好你忘掉，
在这交会时互放的光亮！
'''

poems[20] = '''  愁奴儿
少年不识愁滋味，
爱上层楼,爱上层楼，
为赋新词强说愁。
而今识尽愁滋味，
欲说还休,欲说还休，
却道天凉好个秋。
'''

poems[21] = ''''''

poems[22] = ''''''

poems[23] = ''''''

poems[24] = '''  声声慢
寻寻，觅觅，冷冷，清清，
凄凄，惨惨，戚戚。
乍暖还寒时候，最难将息。
三杯两盏淡酒，怎敌他、晚来风急？
雁过也，正伤心，却是旧时相识。
满地黄花堆积。憔悴损，
如今有谁堪摘？
守着窗儿，独自怎生得黑？
梧桐更兼细雨，到黄昏、点点滴滴。
这次第，怎一个愁字了得!
'''

poems[25] = '''  水调歌头
明月几时有？把酒问青天。
不知天上宫阙，今夕是何年？
我欲乘风归去，又恐琼楼玉宇，
高处不胜寒。
起舞弄清影，何似在人间？
转朱阁，低绮户，照无眠。
不应有恨，何事长向别时圆？
人有悲欢离合，月有阴晴圆缺，
此事古难全。
但愿人长久，千里共婵娟。
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

    assert k > 0 and k < len(poems), \
        f"poem number must be between 1 and {len(poems)-1}"

    p = poems[k]
    assert p, "poem not yet supported"

    orig_p = p
    count = 0
    while to_omit > 0 and count < 3000:
        r = random.randint(0,len(p)-1)
        triv_set = {'.', ',', ';', ':', ' ',
                 '\n', '*', '，', '.', '。', '？', '；', '！'}
        if p[r] not in triv_set:
            p = p[:r] + '*' + p[r+1:]
            to_omit -= 1
        count += 1
    print(p)
    input("Enter to reveal\n")
    print(orig_p)


