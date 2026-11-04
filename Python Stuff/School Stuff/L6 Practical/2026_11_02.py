import math
import random

class Creature:
    def __init__(self, name, creature_type, health, attack_power):
        self.name = str(name)
        self.type = str(creature_type)
        self.health = int(health)
        self.attack_power = int(attack_power)
        pass

def create_player():
    name = input("Enter the player's name: ")
    while True:
        creature_type = input("Enter either 'Fire', 'Water', 'Grass', or 'Electric': ").lower()
        if creature_type in ['fire', 'water', 'grass', 'electric']:
            break
        print("Invalid input. Please try again.")
    health = random.randint(100, 140)
    attack_power = random.randint(10, 30)
    return Creature(name, creature_type, health, attack_power)

Player = create_player()

Computer = Creature(random.choice(["Blaze", "Storm", "Boulder", "Shadow", "Spark"]), random.choice(['fire', 'water', 'grass', 'electric']), random.randint(100,140), random.randint(10, 30))

def attack(Whos_turn_is_it):
    if Whos_turn_is_it == "Player":
        damage = Player.attack_power
        Computer.health -= damage
        print(f"{Player.name} attacks {Computer.name} for {damage} damage!")
    else:
        damage = Computer.attack_power
        Player.health -= damage
        print(f"{Computer.name} attacks {Player.name} for {damage} damage!")

def heal(Whos_turn_is_it):
    if Whos_turn_is_it == "Player":
        heal_amount = random.randint(10, 25)
        Player.health += heal_amount
        if Player.health > 140:
            Player.health = 140
        print(f"{Player.name} heals for {heal_amount} health!")
    else:
        heal_amount = random.randint(10, 25)
        Computer.health += heal_amount
        if Computer.health > 140:
            Computer.health = 140
        print(f"{Computer.name} heals for {heal_amount} health!")

def is_alive():
    if Player.health <= 0:
        return False
    elif Computer.health <= 0:
        return False
    else:
        return True

def get_health():
    print(f"{Player.name}'s health: {Player.health}")

def __str__():
    return f"{Player.name} ({Player.type}) - Health: {Player.health}/140, Attack: {Player.attack_power}"

def main():
    create_player()
    print(f"Your creature:\n\nName: {Player.name}\nType: {Player.type}\nHealth: {Player.health}/140\nAttack: {Player.attack_power}\n")
    while Player.is_alive() and Computer.is_alive():
        print("--------------------------------------------------")
        while True:
            Player_action = input("Choose an action: 'attack' or 'heal': ").lower()
            if Player_action in ["attack", "heal"]:
                break
            print("Invalid input. Please try again.")
        if Player_action == "attack":
            attack("Player")
        else:
            heal("Player")
        Computer_action = random.choice(["attack", "heal"])
        if Computer_action == "attack":
            attack("Computer")
        else:
            heal("Computer")
    if Player.health <= 0:
        print(f"{Player.name} has been defeated! {Computer.name} wins!")
    else:
        print(f"{Computer.name} has been defeated! {Player.name} wins!")

main()