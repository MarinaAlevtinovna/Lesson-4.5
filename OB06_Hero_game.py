import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            if random.choice([True, False]):
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            self._print_health()

            if not self.player.is_alive():
                print(f"{self.player.name} проиграл! {self.computer.name} победил!")
                break
            elif not self.computer.is_alive():
                print(f"{self.computer.name} проиграл! {self.player.name} победил!")
                break

    def _print_health(self):
        print(f"Здоровье {self.player.name}: {self.player.health}")
        print(f"Здоровье {self.computer.name}: {self.computer.health}")

player_hero = Hero("Витязь")
computer_hero = Hero("Компьютер")
game = Game(player=player_hero, computer=computer_hero)
game.start()