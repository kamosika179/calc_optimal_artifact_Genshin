#キャラクターのステータスを入れる

class Character:
    def __init__(self,hp_con,def_con,atk_con,atk_per=0,def_per=0,hp_per=0,em=0,charge=0,c_rate=0,c_damage=0):
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

#甘雨
class Ganyu(Character):
    def __init__(self):
        super().__init__(hp_con=9797,def_con=630,atk_con=335) #レベル90
        self.c_damage = 38.4 #突破ステータス,90
        self.normal_atk = [62.7,70.4,89.9,89.9,95.4,113.9] #通常倍率,10
        self.charge_atk = [86.7,223,230,392] #重撃倍率,10
        self.skill_atk = 238 #スキル倍率,10
        self.burst_atk = 126 #爆発倍率,10

        self.is_c_rate_talent = 1#天賦を有効にする
        self.is_damage_talent = 1#天賦を有効にする

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

