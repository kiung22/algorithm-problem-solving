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
