import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(item, option):
    print_pause("You find yourself confused and surrounded by fire "
                "hearing screams and shrieks all around you.\n")
    print_pause("You see a tall figure in front of you " + option + " carrying a golden fiddle "
                "I know... you know how to play one of these.\n")
    print_pause("He lets out an evil laugh and offers you a bet to return home.\n")
    print_pause("If you can beat me in a fiddle contest I will send you home and give you this golden fiddle.\n")
    print_pause("A fiddle appears in your hand (not yours, but still "
                "decent) hmmm.\n")


def bet(item, option):
    if "fiddle" in item:
        print_pause("\nYou look at the figure and then the fiddle in your hand.")
        print_pause("\nYou've been here before, with friends in bar"
                    " and you know you're the best there's ever been. Is it just an empty bet"
                    " now?")
        print_pause("\nYou lift the fiddle to your shoulder.\n")
    else:
        print_pause("\nYou peer cautiously into the figure's eyes.")
        print_pause("\nIt turns out to be the devil.")
        print_pause("\nYou tell him you're the best "
                    "ever.")
        print_pause("\nYou take the bet")
        print_pause("\nYou lost going first and the devil starts to play "
                    "the golden fiddle you want to be yours.")
        print_pause("\nYou start to play as the devil finishes.\n")
        item.append("fiddle")
    pit_of_fire(item, option)


def pit_of_fire(item, option):
    print_pause("\nYou approach the devil with fiddle in hand.")
    print_pause("\nYou remind him they could back out because your the best there's ever been "
                "you bring the fiddle to your shoulder and " + option + ".")
    print_pause("\nEep! Out pops a " + option + "'s jabbing your backside!")
    print_pause("\nThe " + option + " attacks you!\n")
    if "bet" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny fiddle.\n")
    while True:
        choice2 = input("Would you like to (1) play or (2) "
                        "loose your soul?")
        if choice2 == "1":
            if "fiddle" in item:
                print_pause("\nAs the " + option + " moves to play, "
                            "you see he has a back up band.")
                print_pause("\nThe fiddle is dull and the future is not looking brightly in "
                            "your hand as you brace yourself for the "
                            "music.")
                print_pause("\nBut " + option + "takes one listen to "
                            "your fiddle playing and runs away!")
                print_pause("\nYou have beat the devil in a fiddle contest " + option +
                            ". What will you do with your solid gold fiddle?\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your devil's fiddle playing is no match for you and "
                            + option + ".")
                print_pause("\nYou have been defeated and lost your soul!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back into the reality. "
                        "\nLuckily, you don't seem to have been "
                        "followed including by your soul.\n")
            pit_of_fire(item, option)
            break


def field(item, option):
    print_pause("Enter 1 to take the bet.")
    print_pause("Enter 2 to peer around the pit of fire.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            house(item, option)
            break
        elif choice1 == "2":
            pit_of_fire(item, option)
            break


def play_again():
    again = input("Would you like to try to regain your soul? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the bet ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you real soon. Hahaha\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["wicked fairie", "pirate", "evil spirit", "demonic troll",
                            "Mr. Burns", "Charlie Daniels"])
    intro(item, option)
    field(item, option)


play_game()

