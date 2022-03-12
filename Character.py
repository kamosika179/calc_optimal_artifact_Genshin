import CalcDamage 
import Weapon
import Artifact

#キャラクターのステータスを入れる
class Character:
    def __init__(self,hp_con,def_con,atk_con,atk_per=0,def_per=0,hp_per=0,em=0,charge=0,c_rate=0,c_damage=0,damage=0):
        #ステータス
        self.status = {
            "hp_con":0,
            "def_con":0,
            "atk_con":0,
            "atk_per":0,
            "def_per":0,
            "hp_per":0,
            "em":0,
            "charge":0,
            "c_rate":0,
            "c_damage":0,
            "damage":0
        }
        self.hp_con = hp_con
        self.def_con = def_con
        self.atk_con = atk_con
        self.atk_per = atk_per
        self.def_per = def_per
        self.hp_per = hp_per
        self.em = em
        self.charge = charge
        self.c_rate = c_rate
        self.c_damage = c_damage

        self.damage = damage

        #聖遺物
        self.flower = None
        self.feather = None
        self.sand = None
        self.cup = None
        self.crown = None
        #武器
        self.weapon = None

    #武器を装備する
    def setWeapon(self,weapon):
        self.weapon = weapon

    #聖遺物を装備する
    def setArtifact(self,artifact):
        if artifact.part == 0:
            self.flower = artifact
        elif artifact.part == 1:
            self.feather = artifact
        elif artifact.part == 2:
            self.sand = artifact
        elif artifact.part == 3:
            self.cup = artifact
        elif artifact.part == 4:
            self.crown = artifact

    #ステータスに反映させる
    def updatestatus(self):
        self.status["hp_con"] = self.hp_con + self.flower.hp_con + self.feather.hp_con + self.sand.hp_con + self.cup.hp_con + self.crown.hp_con
        self.status["def_con"] = self.def_con + self.flower.def_con + self.feather.def_con + self.sand.def_con + self.cup.def_con + self.crown.def_con
        self.status["atk_con"] = self.atk_con + self.weapon.atk_con
        self.status["atk_per"] = self.atk_per + self.flower.atk_per + self.feather.atk_per + self.sand.atk_per + self.cup.atk_per + self.crown.atk_per + self.weapon.atk_per
        self.status["def_per"] = self.def_per + self.flower.def_per + self.feather.def_per + self.sand.def_per + self.cup.def_per + self.crown.def_per
        self.status["hp_per"] = self.hp_per + self.flower.hp_per + self.feather.hp_per + self.sand.hp_per + self.cup.hp_per + self.crown.hp_per
        self.status["em"] = self.em+ self.flower.em + self.feather.em+ self.sand.em + self.cup.em + self.crown.em
        self.status["charge"] = self.charge + self.flower.charge + self.feather.charge + self.sand.charge + self.cup.charge + self.crown.charge
        self.status["c_rate"] = self.c_rate+ self.flower.c_rate + self.feather.c_rate + self.sand.c_rate + self.cup.c_rate + self.crown.c_rate + self.weapon.c_rate + 5
        self.status["c_damage"] = self.c_damage + self.flower.c_damage + self.feather.c_damage + self.sand.c_damage + self.cup.c_damage+ self.crown.c_damage + self.weapon.c_damage + 50
        self.status["damage"] = self.damage + self.flower.damage + self.feather.damage + self.sand.damage + self.cup.damage + self.crown.damage + self.weapon.damage


#甘雨
class Ganyu(Character):
    def __init__(self):
        super().__init__(hp_con=9797,def_con=630,atk_con=335) #レベル90
        self.c_damage = 38.4 #突破ステータス,90
        self.normal_atk = [62.7,70.4,89.9,89.9,95.4,113.9] #通常倍率,10
        self.charge_atk = [86.7,223,230,392] #重撃倍率,10
        self.skill_atk = [238] #スキル倍率,10
        self.burst_atk = [126] #爆発倍率,10

        self.is_c_rate_talent = 1#天賦を有効にする
        self.is_damage_talent = 1#天賦を有効にする

'''

    #ひとまずヒルチャールlv90で考えます。今回は最適な聖遺物を探したいので、敵，元素耐性は影響しない？
    def calc_damage(self,weapon,flower,feather,sand,cup,crown):
        atk_con_sum = flower.atk_con + feather.atk_con + sand.atk_con + cup.atk_con + crown.atk_con
        atk_per_sum = weapon.atk_per + flower.atk_per + feather.atk_per + sand.atk_per + cup.atk_per + crown.atk_per
        def_con_sum = flower.def_con + feather.def_con + sand.def_con + cup.def_con + crown.def_con
        #def_per_sum = weapon.def_per + flower.def_per + feather.def_per + sand.def_per + cup.def_per + crown.def_per
        def_hp_con = flower.hp_con + feather.hp_con + sand.hp_con + cup.hp_con + crown.hp_con
        #hp_per_sum = weapon.hp_per + flower.hp_per + feather.hp_per + sand.hp_per + cup.hp_per + crown.hp_per
        #em_sum = weapon.em + flower.em + feather.em + sand.em + cup.em + crown.em
        #charge_sum = weapon.charge + flower.charge + feather.charge + sand.charge + cup.charge + crown.charge
        c_rate_sum = weapon.c_rate + flower.c_rate + feather.c_rate + sand.c_rate + cup.c_rate + crown.c_rate + 5 + self.is_c_rate_talent*20 
        c_damage_sum = weapon.c_damage + flower.c_damage + feather.c_damage + sand.c_damage + cup.c_damage + crown.c_damage + 50 +self.c_damage
        damage_sum = weapon.damage + flower.damage + feather.damage + sand.damage + cup.damage + crown.damage + self.is_damage_talent*20

        base_atk = self.atk_con + weapon.atk_con #基礎攻撃力
        display_atk = base_atk + base_atk*atk_per_sum*0.01 + atk_con_sum#表示攻撃力
        
        def_fix = 0.495#防御補正,wikiより0.495を使うよ
        element_resist = 0.9 #とりあえず0.9とする

        #単純に聖遺物を探すだけなので,一段目の天賦倍率を利用する
        print(display_atk*self.charge_atk[3]*0.01*(1 + c_rate_sum*0.01*c_damage_sum*0.01)*(1 + damage_sum*0.01)*def_fix*element_resist)
        return display_atk*self.charge_atk[3]*0.01*(1 + c_rate_sum*0.01*c_damage_sum*0.01)*(1 + damage_sum*0.01)*def_fix*element_resist

'''

#テスト用
ganyu = Ganyu()
amos = Weapon.Amos_bow()

fl = Artifact.Artifact(1,0,"troupe","hp_con",14,0,0,0,4780,4.7,0,0,10.5,25.6)
fea = Artifact.Artifact(3,1,"troupe","atk_con",0,21.6,0,0,478,0,0,0,3.9,14)
sand= Artifact.Artifact(5,2,"troupe","atk_per",0,0,0,0,448,0,0,11.7,3.1,21)
cup = Artifact.Artifact(7,3,"heart","damage",35,0,0,5.1,0,0,0,0,14,11.7)
cro = Artifact.Artifact(9,4,"troupe","c_damage",0,10.5,0,0,448,0,63,0,5.8,0)

ganyu.setWeapon(amos)
ganyu.setArtifact(fl)
ganyu.setArtifact(fea)
ganyu.setArtifact(sand)
ganyu.setArtifact(cup)
ganyu.setArtifact(cro)

CalcDamage.calcDamage(ganyu)

print(ganyu.status)