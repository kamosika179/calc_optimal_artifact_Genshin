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
