class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount

arthur = Hero("Scorpion", 100)
morgana = Hero("Sub-Zero", 100)

arthur.take_damage(10)

print(arthur.hp)     
print(morgana.hp)      

