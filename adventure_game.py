import random
import time


def introduction():
    print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    time.sleep(2)
    print(f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.")
    time.sleep(2)
    print("In front of you is a house.")
    time.sleep(2)
    print("To your right is a dark cave.")
    time.sleep(2)
    print(f"In your hand you hold your trusty (but not very effective) {weapon}.")
    time.sleep(2)


def field():
    print("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print("Enter 2 to peer into the cave.")
    time.sleep(2)
    print("What would you like to do?")
    choice = ''
    while choice not in ['1','2']:
        choice = input("(Please enter 1 or 2.)\n")
    if choice == '1':
        house()
    elif choice == '2':
        cave()


def house():
    print("You approach the door of the house.")
    time.sleep(2)
    print(f"You are about to knock when the door opens and out steps a {enemy}.")
    time.sleep(2)
    print(f"Eep! This is the {enemy}'s house!")
    time.sleep(2)
    fight(weapon)


def cave():
    global cave_visited
    global weapon
    print("You peer cautiously into the cave.", 2)
    if cave_visited:
        print("You've been here before, and gotten all the good stuff. It's just an empty cave now.", 2)
    elif cave_visited is False:
        print("It turns out to be only a very small cave.")
        time.sleep(2)
        print("Your eye catches a glint of metal behind a rock.")
        time.sleep(2)
        print("You have found the magical Sword of Ogoroth!")
        time.sleep(2)
        print(f"You discard your silly old {weapon} and take the sword with you.")
        time.sleep(2)
        weapon = "sword"
    cave_visited = True
    print("You return to the field")
    time.sleep(2)
    field()


def fight(weapon):
    player_health = random.randint(1, 2)
    enemy_health = random.randint(1, 2)
    print(f"The {enemy} attacks you!")
    time.sleep(2)
    if weapon == "dagger":
        print(f"You feel a bit under-prepared for this, what with only having a tiny {weapon}.")
        time.sleep(2)
    choice = input("Would you like to (1) fight or (2) run away?")
    if choice == '1':
        if weapon == "dagger":
            print(f"You do your best...")
            time.sleep(2)
            print(f"but your {weapon} is no match for the {enemy}.")
            time.sleep(2)
            print(f"You have been defeated!""")
            time.sleep(2)
        elif weapon == "sword":
            print(f"As the {enemy} moves to attack, you unsheath your new sword.")
            time.sleep(2)
            print(f"The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
            time.sleep(4)
            print(f"But the {enemy} takes one look at your shiny new toy and runs away!")
            time.sleep(4)
            print(f"You have rid the town of the {enemy}. You are victorious!")
            time.sleep(3)
    elif choice == '2':
        print("You run back into the field. Luckily, you don't seem to have been followed.")
        time.sleep(2)
        field()
    while player_health > 0 and enemy_health > 0:
        print(f"Your health: {player_health} | Enemy's health: {enemy_health}")
        time.sleep(2)
        player_attack = random.randint(1, 3)
        enemy_attack = random.randint(1, 3)
        enemy_health -= player_attack
        player_health -= enemy_attack
        print(f"You hit the enemy for {player_attack} damage.")
        time.sleep(2)
        print(f"The enemy hits you for {enemy_attack} damage.")    
    if player_health > 0:
        print("Congratulations! You have won the game!")
        time.sleep(2)
    else:
        print("Sorry, you have lost the game. Better luck next time!")
        time.sleep(2)

def play_again():
    print("GAME OVER")
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'n':
            print("Thank you for playing! Goodbye!")
            time.sleep(2)
            return 'exit'
        elif choice == 'y':
            print("Nice! Restarting game ")
            time.sleep(2)
            weapon = 'dagger'
            return 'start'
        

game_state = 'start'
while game_state == 'start':
    enemies = [ 'wicked fairie', 'troll', 'pirate', 'gorgon', 'dragon']
    enemy = random.choice(enemies)
    weapon = 'dagger'
    cave_visited = False

    introduction()
    field()
    
    game_state = play_again()