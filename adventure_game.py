import random
import time


def print_delay(message, delay_time):
    print(message)
    time.sleep(delay_time)


def start_adventure():
    print_delay(
        "You find yourself standing in an open field, filled with grass and "
        "yellow wildflowers.", 2)
    print_delay(
        f"Rumor has it that a {enemy} is somewhere around here, and has been "
        "terrifying the nearby village.", 2)
    print_delay("In front of you is a house.", 2)
    print_delay("To your right is a dark cave.", 2)
    print_delay(
        f"In your hand you hold your trusty (but not very effective) {tool}.", 
        2)


def field():
    print_delay("Enter 1 to knock on the door of the house.", 2)
    print_delay("Enter 2 to peer into the cave.", 2)
    print_delay("What would you like to do?", 2)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
    if choice == '1':
        house()
    elif choice == '2':
        cave()


def house():
    print_delay("You approach the door of the house.", 2)
    print_delay(
        f"You are about to knock when the door opens and out steps a {enemy}.", 
        2)
    print_delay(f"Eep! This is the {enemy}'s house!", 2)
    fight(tool)


def cave():
    global cave_explored
    global tool
    print_delay("You peer cautiously into the cave.", 2)
    if cave_explored:
        print_delay(
            "You've been here before, and gotten all the good stuff. It's just "
            "an empty cave now.", 2)
    elif not cave_explored:
        print_delay("It turns out to be only a very small cave.", 2)
        print_delay("Your eye catches a glint of metal behind a rock.", 2)
        print_delay("You have found the magical Sword of Ogoroth!", 2)
        print_delay(
            f"You discard your silly old {tool} and take the sword with you.", 
            2)
        tool = "sword"
    cave_explored = True
    print_delay("You return to the field", 2)
    field()


def fight(tool):
    player_health = random.randint(1, 2)
    enemy_health = random.randint(1, 2)
    print_delay(f"The {enemy} attacks you!", 2)
    if tool == "dagger":
        print_delay(
            f"You feel a bit under-prepared for this, what with only having a "
            "tiny {tool}.", 2)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("Would you like to (1) fight or (2) run away?")
    if choice == '1':
        if tool == "dagger":
            print_delay("You do your best...", 2)
            print_delay(
                f"but your {tool} is no match for the {enemy}.", 2)
            print_delay("You have been defeated!", 2)
        elif tool == "sword":
            print_delay(
                f"As the {enemy} moves to attack, you unsheath your new sword.",
                2)
            print_delay(
                "The Sword of Ogoroth shines brightly in your hand as you brace "
                "yourself for the attack.", 4)
            print_delay(
                f"But the {enemy} takes one look at your shiny new toy and runs "
                "away!", 4)
            print_delay(
                f"You have rid the town of the {enemy}. You are victorious!", 3)
    elif choice == '2':
        print_delay(
            "You run back into the field. Luckily, you don't seem to have been "
            "followed.", 2)
        field()
    while player_health > 0 and enemy_health > 0:
        print_delay(
            f"Your health: {player_health} | Enemy's health: {enemy_health}", 2)
        player_attack = random.randint(1, 3)
        enemy_attack = random.randint(1, 3)
        enemy_health -= player_attack
        player_health -= enemy_attack
        print_delay(f"You hit the enemy for {player_attack} damage.", 2)
        print_delay(f"The enemy hits you for {enemy_attack} damage.", 2)
    if player_health > 0:
        print_delay("Congratulations! You have won the game!", 2)
    else:
        print_delay("Sorry, you have lost the game. Better luck next time!", 2)


def play_game():
    while True:
        enemies = ['wicked fairie', 'ogre', 'buccaneer', 'gorgon', 'dragon']
        global enemy
        enemy = random.choice(enemies)
        global tool
        tool = 'dagger'
        global cave_explored
        cave_explored = False

        start_adventure()
        field()

        if not play_again():
            break


def play_again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
    if choice == 'n':
        print_delay("Thank you for playing! Goodbye!", 2)
        return False
    elif choice == 'y':
        print_delay("Nice! Restarting game ", 2)
        return True


play_game()
