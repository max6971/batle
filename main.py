from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass



class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"


class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"


class Fighter:
    def __init__(self):
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def fight(self):
        if self.weapon:
            return f"Боец {self.weapon.attack()}"
        else:
            return "Боец без оружия"



class Monster:
    def __init__(self, health=100):
        self.health = health

    def is_defeated(self):
        return self.health <= 0


def battle(fighter, monster):
    print(fighter.fight())
    if fighter.weapon:
        monster.health -= 50

    if monster.is_defeated():
        print("Монстр побежден!")
    else:
        print("Монстр все еще в бою.")



fighter = Fighter()
monster = Monster(health=50)

# Боец выбирает меч
fighter.change_weapon(Sword())
battle(fighter, monster)

# Боец выбирает лук
fighter.change_weapon(Bow())
battle(fighter, Monster(health=50))