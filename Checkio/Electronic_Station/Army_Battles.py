class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5

class Knight(Warrior):

    def __init__(self):
        self.health = 50
        self.attack = 7

def fight(player1,player2):
    turn = 1
    while player1.health > 0 and player2.health > 0:
        if turn % 2 == 1:
            player2.health -= player1.attack
        else:
            player1.health -= player2.attack
        turn += 1
    player1.is_alive = player1.health>0
    player2.is_alive = player2.health>0
    return player1.is_alive

class Army:

    def __init__(self):
        self.list = []

    def add_units(self, unit_class, int):
        for i in range(int):
            unit_class_i = unit_class()
            self.list.append(unit_class_i)

class Battle:

    def fight(self, army1, army2):
        turn = 1
        n = 0
        m = 0
        while army1.list[-1].health>0 and army2.list[-1].health>0:
            if turn % 2 == 1:
                army2.list[m].health -= army1.list[n].attack
                if army2.list[m].health<=0:
                    m += 1
                    turn = 0
            else:
                army1.list[n].health -= army2.list[m].attack
                if army1.list[n].health<=0:
                    n += 1
                    turn = 0
            turn += 1
        return army1.list[-1].health>0
