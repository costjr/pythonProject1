"""a = [1,2,3]

for i in range(0,100000000000000):
    try:
        print(a[i])
    except:
        print("here we have a bug")
        break
print("The Final of the Code")"""


"""class Mypet():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('clasa a fost initializata')
        print(f"object {self.name} a fost creat")

    def feed(self):
        print(self.name + " suiiii")
pol = Mypet('Pol', 12)
lop = Mypet('Lop',1 )
pol.feed()
lop.feed()"""

#console game
fighters =[]
heal_power = 10

class caracters():
    def __init__(self,name,power,hp,armor):
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
class game(caracters):
    def heal(self):
        global heal_power
        self.hp += heal_power
        print(f"{self.name} have {self.hp} ")

    def attack(self, damage):
        if self.hp - damage >0:
            self.hp -= damage
            print(f"{self.name} have {self.hp}")
            return True
        else:
            print(f"{self.name} is dead")
            return False

nr = 0
while 1:
    try:
        nr = int(input("Number of players"))
        break
    except:
        print("Invalid Data")
        continue


for i in range(0, nr):
    name = input("name:")
    power = int(input("power:"))
    hp = int(input("hp:"))
    armor = int(input("armor:"))
    fighters.append(game(name,power,hp,armor))

alive = True
player1 = fighters[0]
player2 = fighters[1]

cur_player = player1
next_player = player2


while alive:
        print("chose what you want to do")
        print("Press 1 to attack other players")
        print("Press 2 to heal your self")
        print("Press 3 to continue/skip")
        move = int(input("Move:"))
        if move == 1:
            alive = next_player.attack(cur_player.power)
        elif move == 2:
            cur_player.heal()
        else:
             pass

        if cur_player == player1:
            cur_player = player2
            next_player = player1
        else:
            next_player = player2
            cur_player = player1
