
import os
import time

import Character
import Weapon

#計測開始
start_time = time.perf_counter()

filename = "artifact.csv"

class Artifact:
    #id、部位、聖遺物名、メイン、攻撃力、攻撃力%、防御、防御%、HP、HP%、元素熟知、チャージ効率、会心率、会心ダメージ
    def __init__(self,id,part,name,mainOP,atk_con,atk_per,def_con,def_per,hp_con,hp_per,em,charge,c_rate,c_damage):
        self.id = id 
        self.part = part # 0 =flower 1 = feather 2 = sand 3 = cup 4 = crown
        self.name = name
        self.mainOP = mainOP #string
        self.atk_con = atk_con
        self.atk_per = atk_per
        self.def_con = def_con
        self.def_per = def_per
        self.hp_con = hp_con
        self.hp_per = hp_per
        self.em = em
        self.charge = charge
        self.c_rate = c_rate
        self.c_damage = c_damage

        self.damage = 0

        self.set_mainOP()

    def set_mainOP(self):
        if self.mainOP == "atk_con":
            self.atk_con += 311

        elif self.mainOP == "hp_con":
            self.hp_con += 4780

        elif self.mainOP == 'em':
            self.em += 187

        elif self.mainOP == "atk_per":
            self.atk_per += 46.6

        elif self.mainOP == "def_per":
            self.def_per += 58.3

        elif self.mainOP == "charge":
            self.charge += 51.8

        elif self.mainOP == "c_rate":
            self.c_rate += 31.1

        elif self.mainOP == "c_damage":
            self.c_damage += 62.2

        elif self.mainOP == "physics":
            self.damage += 58.3

        elif self.mainOP == "damage":
            self.damage += 46.6


#聖遺物を種別に入れておく
class Bag:
    def __init__(self):
        self.flower = []
        self.feather = []
        self.sand = []
        self.cup = []
        self.crown = []

class Equip:
    def __init__(self):
        self.flower = None
        self.feather = None
        self.sand = None
        self.cup = None
        self.crown = None
    
    #聖遺物を入れ替える
    def set_artifact(self,fl,fe,sa,cu,cr):
        self.flower = fl
        self.feather = fe
        self.sand = sa
        self.cup = cu
        self.crown = cr


max_value = 0 #最大価値
now_equip = Equip() #最大の組み合わせ

readf = open(os.path.dirname(os.path.abspath(__file__))+ "/" + filename, 'r',encoding="utf-8")

datalist = readf.readlines()
count = 0

bag = Bag()

for data in datalist:
    if(count < 1):

        count += 1
    else:
        fixdata = data.strip().split(",")
        if fixdata[1] == '0': 
            bag.flower.append(Artifact(fixdata[0],fixdata[1],fixdata[2],fixdata[3],float(fixdata[4]),float(fixdata[5]),float(fixdata[6]),float(fixdata[7]),float(fixdata[8]),float(fixdata[9]),float(fixdata[10]),float(fixdata[11]),float(fixdata[12]),float(fixdata[13])))
        elif fixdata[1] =='1':
            bag.feather.append(Artifact(fixdata[0],fixdata[1],fixdata[2],fixdata[3],float(fixdata[4]),float(fixdata[5]),float(fixdata[6]),float(fixdata[7]),float(fixdata[8]),float(fixdata[9]),float(fixdata[10]),float(fixdata[11]),float(fixdata[12]),float(fixdata[13])))
        elif fixdata[1] =='2':
            bag.sand.append(Artifact(fixdata[0],fixdata[1],fixdata[2],fixdata[3],float(fixdata[4]),float(fixdata[5]),float(fixdata[6]),float(fixdata[7]),float(fixdata[8]),float(fixdata[9]),float(fixdata[10]),float(fixdata[11]),float(fixdata[12]),float(fixdata[13])))
        elif fixdata[1] =='3':
            bag.cup.append(Artifact(fixdata[0],fixdata[1],fixdata[2],fixdata[3],float(fixdata[4]),float(fixdata[5]),float(fixdata[6]),float(fixdata[7]),float(fixdata[8]),float(fixdata[9]),float(fixdata[10]),float(fixdata[11]),float(fixdata[12]),float(fixdata[13])))
        elif fixdata[1] =='4':
            bag.crown.append(Artifact(fixdata[0],fixdata[1],fixdata[2],fixdata[3],float(fixdata[4]),float(fixdata[5]),float(fixdata[6]),float(fixdata[7]),float(fixdata[8]),float(fixdata[9]),float(fixdata[10]),float(fixdata[11]),float(fixdata[12]),float(fixdata[13])))

char = Character.Ganyu() 
amos = Weapon.Amos_bow()
amos.option() #武器効果を有効にする

#全探索
for fl in bag.flower:
    print("a")
    for fe in bag.feather:
        for sa in bag.sand:
            for cu in bag.cup:
                for cr in bag.crown:
                    if max_value < char.calc_damage(amos,fl,fe,sa,cu,cr):
                        max_value = char.calc_damage(amos,fl,fe,sa,cu,cr)
                        now_equip.set_artifact(fl,fe,sa,cu,cr)
                        print("更新されました")
                    
print("一番良い組み合わせ\n")
print(now_equip.flower.id + now_equip.feather.id + now_equip.sand.id + now_equip.cup.id + now_equip.crown.id)

#計測終了
end_time = time.perf_counter()

print("経過時間:" + str(end_time-start_time))