
import os
import time

import Character
import Weapon
import Artifact
import CalcDamage

#計測開始
start_time = time.perf_counter()

filename = "artifact.csv"

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
            bag.flower.append(Artifact.Artifact(fixdata[0],fixdata[1],fixdata[2],fixdata[3],float(fixdata[4]),float(fixdata[5]),float(fixdata[6]),float(fixdata[7]),float(fixdata[8]),float(fixdata[9]),float(fixdata[10]),float(fixdata[11]),float(fixdata[12]),float(fixdata[13])))
        elif fixdata[1] =='1':
            bag.feather.append(Artifact.Artifact(fixdata[0],fixdata[1],fixdata[2],fixdata[3],float(fixdata[4]),float(fixdata[5]),float(fixdata[6]),float(fixdata[7]),float(fixdata[8]),float(fixdata[9]),float(fixdata[10]),float(fixdata[11]),float(fixdata[12]),float(fixdata[13])))
        elif fixdata[1] =='2':
            bag.sand.append(Artifact.Artifact(fixdata[0],fixdata[1],fixdata[2],fixdata[3],float(fixdata[4]),float(fixdata[5]),float(fixdata[6]),float(fixdata[7]),float(fixdata[8]),float(fixdata[9]),float(fixdata[10]),float(fixdata[11]),float(fixdata[12]),float(fixdata[13])))
        elif fixdata[1] =='3':
            bag.cup.append(Artifact.Artifact(fixdata[0],fixdata[1],fixdata[2],fixdata[3],float(fixdata[4]),float(fixdata[5]),float(fixdata[6]),float(fixdata[7]),float(fixdata[8]),float(fixdata[9]),float(fixdata[10]),float(fixdata[11]),float(fixdata[12]),float(fixdata[13])))
        elif fixdata[1] =='4':
            bag.crown.append(Artifact.Artifact(fixdata[0],fixdata[1],fixdata[2],fixdata[3],float(fixdata[4]),float(fixdata[5]),float(fixdata[6]),float(fixdata[7]),float(fixdata[8]),float(fixdata[9]),float(fixdata[10]),float(fixdata[11]),float(fixdata[12]),float(fixdata[13])))

char = Character.Ganyu() 
amos = Weapon.Amos_bow()
amos.option() #武器効果を有効にする

char.setWeapon(amos) #武器をセット

#全探索
for fl in bag.flower:
    print("a")
    for fe in bag.feather:
        for sa in bag.sand:
            for cu in bag.cup:
                for cr in bag.crown:
                    char.setArtifact(fl)
                    char.setArtifact(fe)
                    char.setArtifact(sa)
                    char.setArtifact(cu)
                    char.setArtifact(cr)
                    if max_value < CalcDamage.calcNormalDamage(char)[0]:
                        max_value = CalcDamage.calcNormalDamage(char)[0]
                        now_equip.set_artifact(fl,fe,sa,cu,cr)
                        print("更新されました")
                    
print("一番良い組み合わせ\n")
print(now_equip.flower.id + now_equip.feather.id + now_equip.sand.id + now_equip.cup.id + now_equip.crown.id)
print(max_value)
#計測終了
end_time = time.perf_counter()

print("経過時間:" + str(end_time-start_time))