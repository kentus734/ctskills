class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount

scorpion = Hero("Scorpion", 100)
subzero = Hero("Sub-Zero", 100)

scorpion.take_damage(10)

print(scorpion.hp)     
print(subzero.hp)      

