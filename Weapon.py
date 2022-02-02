


class Weapon:
    def __init__(self,atk_con=0,atk_per=0,damage=0,c_rate=0,c_damage=0):
        self.atk_con = atk_con
        self.atk_per = atk_per
        self.damage = damage
        self.c_rate = c_rate
        self.c_damage = c_damage

#アモスの弓
class Amos_bow(Weapon):
    def __init__(self):
        super().__init__(atk_con=608,atk_per=49.6)
    
    #武器効果
    def option(self,count=5):
        self.damage += 12 + 8*count
