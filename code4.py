"""def test():
    print('This is test')
test()"""


"""def calc(a, b=1):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
calc(8)
calc(3, 8)
calc(6, 5)
calc(1, 4)

def concat(*args):

    print(args[0] + args[1] + args[2])

concat("sdfs", "dsfdrs", "fgsftd")

def clas(elev, nota, obiect):
    return f"Elevul: {elev} are nota:  {nota} la disciplina:  {obiect}"
final = clas(elev= "Ion", nota= 8, obiect= "Matematica")
print(final)"""

"""for i in range(1,10):
    if i == 4 and i == 6:
        continue #break
    print(i)"""


"""for i in range(1,10):
    if i == 4:
        pass
    else:
        print("lalala")
    print(i)"""

"""Hp = 75
Damage = 25
Armor = 50

def attack(hp, damage, armor):
    hp_after_damage = hp
    armor_after_damage = armor
    if hp_after_damage - damage > 0:
        if armor > 0:
            armor_after_damage = armor - damage
        if armor <=0:
            if hp_after_damage > 0:
                hp_after_damage = hp - damage + armor
    else:
        print("Dead")
    return hp_after_damage, armor_after_damage

def heal(hp):
    hp_after_heal = hp + 10
    
    return hp_after_heal

for i in range(1,10):
    Hp, Armor = attack(Hp,Damage,Armor)
    print("HP =", Hp, "Armor =" ,Armor)
    if Hp <= 0:
        print("Dead")
        break
    Hp =heal(Hp)
    print("HP =", Hp, "Armor =", Armor)"""

#miss
"""for i in range(1, 100):

    if i %3 == 0:
        print("miss")"""

