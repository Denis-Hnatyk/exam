import random as rn

class CasinoPlayer:
    global_increment = 0

    def __init__(self, name):
        CasinoPlayer.global_increment += 1
        self.local_increment = CasinoPlayer.global_increment
        self.name = name
        self.win = 0
        self.bet = int(input(f"Гравець {self.name}, введіть суму, яку ви хочете поставити: "))
        self.number = rn.randint(1, 3)
        if self.number == 1:
            self.win = self.bet * 5
        elif self.number == 2:
            self.win = self.bet * 3
        else:
            self.win = 0

player1 = CasinoPlayer("Denis")
player2 = CasinoPlayer("Viktor")
player3 = CasinoPlayer("Yura")


print(f"Глобальний інкремент для player1: {player1.global_increment}, локальний інкремент: {player1.local_increment}. Ваш виграш становить {player1.win}\n")
print(f"Глобальний інкремент для player2: {player2.global_increment}, локальний інкремент: {player2.local_increment}. Ваш виграш становить {player2.win}\n")
print(f"Глобальний інкремент для player3: {player3.global_increment}, локальний інкремент: {player3.local_increment}. Ваш виграш становить {player3.win}\n")
