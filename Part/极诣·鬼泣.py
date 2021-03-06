from PublicReference.base import *
from math import *

class 极诣·鬼泣主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '太刀':
            return round(self.CD / self.恢复 * 1.0, 1)
        if 武器类型 == '短剑':
            return round(self.CD / self.恢复 * 1.05, 1)

class 极诣·鬼泣技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['鬼影步']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

class 极诣·鬼泣技能1(极诣·鬼泣主动技能):
    名称 = '鬼斩'
    备注 = '(蓄力&噬灵鬼斩)'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 51
    基础 = 810
    成长 = 113.12
    CD = 6.0
    TP成长 = 0.08
    TP上限 = 5

class 极诣·鬼泣技能2(被动技能):
    名称 = '刀魂之卡赞'
    是否主动 = 1
    所在等级 = 5
    等级上限 = 20
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.04 + 0.01 * self.等级, 5)

class 极诣·鬼泣技能3(被动技能):
    名称 = '侵蚀之普戾蒙'
    是否主动 = 1
    所在等级 = 15
    等级上限 = 11
    基础等级 = 2
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.01 * self.等级, 5)

class 极诣·鬼泣技能4(被动技能):
    名称 = '太刀精通'
    所在等级 = 15
    等级上限 = 40
    基础等级 = 30
    关联技能 = ['所有']
    data = [0, 13, 28, 41, 54, 68, 82, 96, 109, 123, 137, 150, 164, 177, 191, 205, 219, 233, 245, 259, 273, 287, 301, 314, 328, 341, 355, 369, 382, 396, 410, 424, 437, 450, 464, 478, 492, 506, 520, 532, 546, 560, 574, 588, 601, 615, 628, 642, 656, 669, 683, 697, 711, 724, 737, 751, 765, 779, 793, 806, 819, 833, 847, 861, 874, 888, 902, 915, 929, 942, 956]
    
    def 加成倍率(self, 武器类型):
        if 武器类型 == '太刀':
            return self.data[self.等级] / 1000 + 1
        else:
            self.关联技能 = ['无']
            return 1.0

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 极诣·鬼泣技能5(被动技能):
    名称 = '短剑精通'
    所在等级 = 15
    等级上限 = 40
    基础等级 = 30
    关联技能 = ['所有']

    data = [0, 12, 26, 39, 51, 64, 77, 90, 103, 116, 129, 141, 154, 167, 180, 193, 206, 219, 231, 244, 257, 270, 283, 296, 309, 321, 334, 347, 360, 373, 386, 399, 411, 424, 437, 450, 463, 476, 489, 501, 514, 527, 540, 553, 566, 579, 591, 604, 617, 630, 643, 656, 669, 681, 694, 707, 720, 733, 746, 759, 771, 784, 797, 810, 823, 836, 849, 861, 874, 887, 900]
    
    def 加成倍率(self, 武器类型):
        if 武器类型 == '短剑':
            return self.data[self.等级] / 1000 + 1
        else:
            self.关联技能 = ['无']
            return 1.0

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 极诣·鬼泣技能6(被动技能):
    名称 = '暗月降临'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['无']

    自定义描述 = 1
    def 技能描述(self, 武器类型):
        return '暗属性强化+' + str(self.属强加成())

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        if self.等级 <= 10:
            return round(self.等级 * 3)
        else:
            return round(30 + (self.等级-10) * 5)

class 极诣·鬼泣技能7(极诣·鬼泣主动技能):
    名称 = '月光斩'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1640.745455
    成长 = 185.2545455
    CD = 4.0
    TP成长 = 0.08
    TP上限 = 5

class 极诣·鬼泣技能8(极诣·鬼泣主动技能):
    名称 = '鬼影步'
    备注 = '(一轮)'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 20
    基础 = 361
    成长 = 0
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 3

class 极诣·鬼泣技能9(被动技能):
    名称 = '噬灵鬼斩'
    所在等级 = 25
    等级上限 = 5
    基础等级 = 1
    关联技能 = ['无']

    def 加成倍率(self):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.1 * self.等级, 5)

class 极诣·鬼泣技能10(极诣·鬼泣主动技能):
    名称 = '鬼影鞭'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 26
    基础 = 2649.05556
    成长 = 502.9444444
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5

class 极诣·鬼泣技能11(极诣·鬼泣主动技能):
    名称 = '冰霜之萨亚'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 39
    基础 = 433.0666667
    成长 = 48.93333333
    CD = 15.0
    TP上限 = 5
    演出时间 = 5

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级)) * ceil(10 / (1 - 0.07 * self.TP等级)) * self.倍率)

class 极诣·鬼泣技能12(极诣·鬼泣主动技能):
    名称 = '死亡墓碑'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6500.045455
    成长 = 735.9545455
    CD = 18
    TP成长 = 0.10
    TP上限 = 5

class 极诣·鬼泣技能13(极诣·鬼泣主动技能):
    名称 = '瘟疫之罗刹'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 37
    基础 = 6142.0
    成长 = 694.0
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 5

    def 装备护石(self):
        self.倍率 *= (0.5*1.1)+(0.5*1.1*1.08)


class 极诣·鬼泣技能14(极诣·鬼泣主动技能):
    名称 = '鬼斩：狂怒'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 6962.7
    成长 = 786.3
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.5

    def 装备护石(self):
        self.倍率 *= 1.26
        self.演出时间 = 1.2

class 极诣·鬼泣技能15(极诣·鬼泣主动技能):
    名称 = '鬼影闪'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 5724.725
    成长 = 646.275
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


class 极诣·鬼泣技能16(极诣·鬼泣主动技能):
    名称 = '冥炎之卡洛'
    备注 = '(一轮)'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 32
    基础 = 187.7567568 * 3
    成长 = 21.24324324 * 3
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5

class 极诣·鬼泣技能17(极诣·鬼泣主动技能):
    名称 = '冥炎之卡洛(灼烧)'
    备注 = '(1秒3次)'
    所在等级 = 45
    等级上限 = 1
    基础等级 = 1
    基础 = 114.972973 * 3
    成长 = 13.02702703 * 3
    CD = 1.0
    TP成长 = 0.10

class 极诣·鬼泣技能18(极诣·鬼泣主动技能):
    名称 = '冥炎剑'
    所在等级 = 45
    等级上限 = 1
    基础等级 = 1
    基础 = 11522.4359
    成长 = 1301.282051
    CD = 45.0
    TP成长 = 0.10

    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.20

class 极诣·鬼泣技能19(被动技能):
    名称 = '恐惧光环'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

class 极诣·鬼泣技能20(极诣·鬼泣主动技能):
    名称 = '第七鬼神：邪神怖拉修'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 24990.46
    成长 = 7544.68
    CD = 140.0

class 极诣·鬼泣技能21(极诣·鬼泣主动技能):
    名称 = '鬼斩：炼狱'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 11149.95455
    成长 = 1259.045455
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.20762

class 极诣·鬼泣技能22(极诣·鬼泣主动技能):
    名称 = '冥祭之沼'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 14727.94118
    成长 = 1663.058824
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.20

class 极诣·鬼泣技能23(被动技能):
    名称 = '御鬼之极'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.20 + 0.02 * self.等级, 5)

class 极诣·鬼泣技能24(极诣·鬼泣主动技能):
    名称 = '幽魂之布雷德'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 32144.25
    成长 = 3630.75
    攻击次数 = 1
    基础2 = 24755.45
    成长2 = 2795.55
    攻击次数2 = 0
    CD = 40.0

class 极诣·鬼泣技能25(极诣·鬼泣主动技能):
    名称 = '幽魂降临：式'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 32089.94118
    成长 = 3623.058824
    CD = 45.0

class 极诣·鬼泣技能26(极诣·鬼泣主动技能):
    名称 = '王者号令：吉格降临'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 50664
    成长 = 15299
    CD = 180.0

class 极诣·鬼泣技能27(被动技能):
    名称 = '鬼神冠冕'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 极诣·鬼泣技能28(极诣·鬼泣主动技能):
    名称 = '鬼神剑·黄泉摆渡'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 68159.6
    成长 = 7695.4
    CD = 60.0

class 极诣·鬼泣技能29(极诣·鬼泣主动技能):
    名称 = '黄泉之门：万鬼渡灵'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 210478.5
    成长 = 63546.5
    CD = 290.0

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

极诣·鬼泣技能列表 = []
i = 0
while i >= 0:
    try:
        exec('极诣·鬼泣技能列表.append(极诣·鬼泣技能'+str(i)+'())')
        i += 1
    except:
        i = -1

极诣·鬼泣技能序号 = dict()
for i in range(len(极诣·鬼泣技能列表)):
    极诣·鬼泣技能序号[极诣·鬼泣技能列表[i].名称] = i

极诣·鬼泣一觉序号 = 0
极诣·鬼泣二觉序号 = 0
极诣·鬼泣三觉序号 = 0
for i in 极诣·鬼泣技能列表:
    if i.所在等级 == 50:
        极诣·鬼泣一觉序号 = 极诣·鬼泣技能序号[i.名称]
    if i.所在等级 == 85:
        极诣·鬼泣二觉序号 = 极诣·鬼泣技能序号[i.名称]
    if i.所在等级 == 100:
        极诣·鬼泣三觉序号 = 极诣·鬼泣技能序号[i.名称]

极诣·鬼泣护石选项 = ['无']
for i in 极诣·鬼泣技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣·鬼泣护石选项.append(i.名称)

极诣·鬼泣符文选项 = ['无']
for i in 极诣·鬼泣技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        极诣·鬼泣符文选项.append(i.名称)

class 极诣·鬼泣角色属性(角色属性):

    实际名称 = '极诣·鬼泣'
    角色 = '鬼剑士(男)'
    职业 = '鬼泣'

    武器选项 = ['太刀','短剑']
    
    伤害类型选择 = ['魔法百分比']
    
    伤害类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.69
   
    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(极诣·鬼泣技能列表)
        self.技能序号= deepcopy(极诣·鬼泣技能序号)
    
    def 被动倍率计算(self):
        super().被动倍率计算()
        self.暗属性强化 += self.技能栏[self.技能序号['暗月降临']].属强加成()

        self.技能栏[self.技能序号['冥炎之卡洛(灼烧)']].等级 = self.技能栏[self.技能序号['冥炎之卡洛']].等级
        self.技能栏[self.技能序号['冥炎之卡洛(灼烧)']].TP等级 = self.技能栏[self.技能序号['冥炎之卡洛']].TP等级
        self.技能栏[self.技能序号['冥炎剑']].等级 = self.技能栏[self.技能序号['冥炎之卡洛']].等级
        self.技能栏[self.技能序号['冥炎剑']].TP等级 = self.技能栏[self.技能序号['冥炎之卡洛']].TP等级

        x = 1 + self.技能栏[self.技能序号['鬼斩']].TP等级 * self.技能栏[self.技能序号['鬼斩']].TP成长 
        x /= self.技能栏[self.技能序号['噬灵鬼斩']].加成倍率()
        self.技能栏[self.技能序号['鬼斩']].基础 += 787 / x
        self.技能栏[self.技能序号['鬼斩']].成长 += 110.07 / x

class 极诣·鬼泣(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣·鬼泣角色属性()
        self.角色属性A = 极诣·鬼泣角色属性()
        self.角色属性B = 极诣·鬼泣角色属性()
        self.一觉序号 = 极诣·鬼泣一觉序号
        self.二觉序号 = 极诣·鬼泣二觉序号
        self.三觉序号 = 极诣·鬼泣三觉序号
        self.护石选项 = deepcopy(极诣·鬼泣护石选项)
        self.符文选项 = deepcopy(极诣·鬼泣符文选项)

    def 界面(self):
        super().界面()
        self.布雷德开关=QCheckBox('刀阵：直接解放',self.main_frame2)
        self.布雷德开关.setChecked(False)
        self.布雷德开关.resize(120,20)
        self.布雷德开关.move(325,450)
        self.布雷德开关.setStyleSheet(复选框样式)

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        if self.布雷德开关.isChecked():
            属性.技能栏[属性.技能序号['幽魂之布雷德']].攻击次数 = 0
            属性.技能栏[属性.技能序号['幽魂之布雷德']].攻击次数2 = 1