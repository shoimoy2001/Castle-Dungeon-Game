from os import system
from random import randint

gametitle = "Castle Dungeons - An interactive story game"
system("mode 110, 30")  # wide height
system("title " + gametitle)


def cls():
    # main function
    system('cls')


character_name = None
character_race = None
character_class = None
character_strength = None
character_magic = None
character_dexterity = None
character_life = None


# to this point cls will clean the screen
cls()
print("Castle Dungeons - An interactive story game")


def Intro():
    print("")
    print("In this Adventure, you are the Hero.")
    print("Your choices, skills, and a bit of luck will influence the outcome of the game")
    print("")
    print("An Evil sorcerer is holding your fellow adventurers prisoners.")
    print("Will you succeed in freeing your friends from the castle dungeons, or perish trying?")
    print("")
    input("Press Enter to start...")


def create_character():
    cls()
    global character_name, character_race, character_class
    character_name = input("""
        Let's Begin by creating your character.
        What is your Character name?
                           
        > """)

    while character_race is None:
        race_choice = input("""
            Choose your character race from the list by entering the relevant number:
            1 - Elf
            2 - Dwarf
            > """)
        if race_choice == "1":
            character_race = "Elf"
        elif race_choice == "2":
            character_race = "Dwarf"
        else:
            print("Not a valid choice, try again")
    cls()
    while character_class is None:
        class_choice = input("""
            Choose your character class from the list below by entering the relevant number:
            1 - Warrior
            2 - Wizard
            > """)
        if class_choice == "1":
            character_class = "Warrior"
        elif class_choice == "2":
            character_class = "Wizard"
        else:
            print("Not a valid choice, try again!")


def create_character_skill_sheet():
    cls()
    global character_strength, character_dexterity, character_life, character_magic
    print("""
    Now let's determine your character's skills, which you will use throughout the game.
    In this game, your character has four skills:
    
    - Strength, which you will use in combat or any strength test
    - Dexterity, which you will use in any ability test
    - Magic, which you will use whenever you need to cast a spell or use/inspect a magical item or place
    - Life, which determines your life energy, points will be lost when hurt, 
      and whenever Life reaches 0, your character dies.

    
    Depending on your race and class, you will have a certain point-base already calculated by the game.
    You will shortly be able to increase your skills by rolling a 6-face die.

    Here is your base Character Skills Sheet:
    """)
    character_strength = 5
    character_magic = 0
    character_dexterity = 3
    character_life = 10

    if character_race == "Elf":
        character_strength += 3
        character_magic += 6
        character_dexterity += 4
        character_life += 2
    elif character_race == "Dwarf":
        character_strength += 5
        character_life += 4

    if character_class == "Warrior":
        character_strength += 3
        character_life += 3
    elif character_class == "Wizard":
        character_magic += 4
    print("""
    Name: """ + character_name +
          """
    Race: """ + character_race +
          """
    Class: """ + character_class +
          """
    Strength:  """ + str(character_strength) +
          """
    Dexterity:  """ + str(character_dexterity) +
          """
    Magic: """ + str(character_magic) +
          """
    Life: """ + str(character_life) + """

    """)
    input("Press Enter to apply your skills modifiers")


def modify_skill():
    cls()
    global character_strength, character_dexterity, character_life
    print("To modify your skills, roll a six face die for each of your skills, and the game will add your score to the relevant skill")
    input("Press Enter to roll for strength")
    roll = randint(1, 6)
    print("You Rolled: " + str(roll))
    character_strength += roll
    input("Press Enter to roll for Dexterity")
    roll = randint(1, 6)
    print("You Rolled: " + str(roll))
    character_dexterity += roll
    input("Press Enter to roll for Life")
    roll = randint(1, 6)
    print("You Rolled: " + str(roll))
    character_life += roll
    input("Press Enter to continue......")
    cls()
    print("""
    Congratulations! You have completed your character creation!
    Your final character sheet is:
          
    Name: """ + character_name +
          """
    Race: """ + character_race +
          """
    Class: """ + character_class +
          """
    Strength:  """ + str(character_strength) +
          """
    Dexterity:  """ + str(character_dexterity) +
          """
    Magic: """ + str(character_magic) +
          """
    Life: """ + str(character_life) + """

    """)
    input("Press Enter to begin your adventure, if you dare...")


def play_again():
    cls()
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def win():
    print("Congratulations! You have successfully completed the game!")
    if play_again():
        start_game()
    else:
        print("Thank you for playing! Goodbye.")
        exit()


def lose():
    print("You Died!!.....Alas!!Your friends will never be freed......!!! ")
    if play_again():
        start_game()
    else:
        print("Thank you for playing! Goodbye.")
        exit()


def start_game():
    Intro()
    create_character()
    create_character_skill_sheet()
    modify_skill()
    Scene_1()


def Scene_1():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
    You have entered the Castle Dungeons.. 
    It is dark, however, thankfully your torch is lit and you can see up to 20 feet away from you.
    The stone walls are damp, the smell of rats and orcs is strong. 
    You walk down a narrow corridor until you reach a thick stone wall.

    The corridor continues on the left and on the right.

    What do you do?

    1 - Turn left
    2 - Turn right    
    > """)
        if user_input == '1' or user_input.lower() == "turn left":
            choice = "1"
            Scene_2()

        elif user_input == '2' or user_input.lower() == "turn right":
            choice = "2"
            Scene_3()
        else:
            print("Not a valid choice, type a number or 'turn left' / 'turn right'")


def Scene_2():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
    From the darkness behind you.. you hear a strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input == "1" or user_input.lower() == "continue":
            choice = 1
            combat()

        elif user_input == "2" or user_input.lower() == "stop":
            choice = 2
            skill_check()
        else:
            print("""
            Not a Valid choice, type a number or "continue" / "stop"
            """)


def Scene_3():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
    From the darkness ahead of you.. you hear a strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input == "1" or user_input.lower() == "continue":
            choice = "1"
            combat()
        elif user_input == "2" or user_input.lower() == "stop":
            choice = "2"
            skill_check()
        else:
            print("""
            Not a valid choice, type a number or - "continue" / "stop"
            """)


def skill_check():
    cls()
    print("A giant rock falls from the ceiling, roll a die to see if you can dodge it.. or you will be crushed by it!")
    input("Press Enter to roll a die to save yourself from getting crushed ")
    roll = randint(1, 6)
    print("You rolled: " + str(roll))
    if roll + character_dexterity > 10:
        print("""
        You dodge the stone and survive! Danger is not over though..
        The strange noise in the darkness continues, and it feels a lot closer now..""")
        input("Press Enter to continue.....")
        combat()

    else:
        print("You are smashed by the rock.. you are dead...\nGAME OVER!!!!!!!")
        lose()


def combat():
    cls()
    global character_life
    print("A horrible Orcs Attacks you!")
    input("Press Enter to combat....")
    orc = [10, 14]  # imagine 10 as strength, 14 as life of orc
    while orc[1] > 0 or character_life > 0:
        char_roll = randint(1, 6)
        print("You Rolled: " + str(char_roll))
        monst_roll = randint(1, 6)
        print("The monster rolled: " + str(monst_roll))
        if char_roll + character_strength >= monst_roll + orc[0]:
            print("You Smashed the Monster!!")
            orc[1] -= randint(1, 6)  # damage after a hit to the orc
        else:
            print("The monster Hit You!!")
            character_life -= randint(1, 6)
    if character_life > 0:
        print("You Destroyed the Orc, Congratulations!!!!!")
        win()
    else:
        print("You Died!!.....Alas!!You friends will never be freed......!!! ")
        lose()


start_game()

