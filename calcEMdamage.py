

def calcElementalReactionDamage(lv,EMcon,reaction):
    '''
        superconduct,(超伝導)
        swirl,(拡散)
        electrocharged,(感電)
        shattered,(氷砕き)
        overloaded,(過負荷)
        のいずれかがreactionに入る
    '''
    #固有値テーブル
    uniqueDamage = {"superconduct":{80:538,
                                         90:723},

                        "swirl":{80:646,
                                90:868},

                        "electrocharged":{80:1292,
                                          90:1736},

                        "shattered":{80:1616,
                                     90:2170},

                        "overloaded":{80:2154,
                                     90:2893},
                    }

    #元素反応ダメージ＝固有値*(1 + 元素熟知の元素反応ダメージボーナス + その他の元素反応ダメージボーナス) *元素耐性補正
    #元素熟知の反応ダメージボーナス = 16*元素熟知/(元素熟知 + 2000)

    reactionDamageBonus = 16*EMcon/(EMcon + 2000)
    nowUniqueDamage = uniqueDamage[reaction][lv]

    otherreactionDamageBonus = 0
    resistance = 0.9

    reactionDamage = nowUniqueDamage*(1 + reactionDamageBonus + otherreactionDamageBonus)*resistance

    return reactionDamage

#print(calcElementalReactionDamage(90,80,"overloaded")) ゲーム内では4206ダメージ

#ゲーム内ではレベル90,EMconが80のときの超電導発動で1051ダメージだった
