
#Character,Enemy
def calcNormalDamage(ch):
    normalAtkDamagelist = []

    ch.updatestatus()
    
    base_atk = ch.status["atk_con"]
    display_atk = base_atk + base_atk*ch.status["atk_per"]*0.01 + ch.flower.atk_con + ch.feather.atk_con + ch.sand.atk_con + ch.cup.atk_con + ch.crown.atk_con

    def_fix = 0.495
    element_resist = 0.9

    for nowTalentMultiplier in ch.normal_atk:
        normalAtkDamagelist.append(display_atk*ch.skill_atk[0]*0.01*(1 + ch.status["c_rate"]*0.01*ch.status["c_damage"]*0.01)*(1 + ch.status["damage"]*0.01)*def_fix*element_resist) 

    #print(display_atk*ch.skill_atk[0]*0.01*(1 + ch.status["c_rate"]*0.01*ch.status["c_damage"]*0.01)*(1 + ch.status["damage"]*0.01)*def_fix*element_resist)
    return normalAtkDamagelist

    
    #会心率100%のとき
    #print(display_atk*ch.skill_atk[0]*0.01*(1 + 1*ch.status["c_damage"]*0.01)*(1 + ch.status["damage"]*0.01)*def_fix*element_resist)