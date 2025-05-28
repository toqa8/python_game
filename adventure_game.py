import time
import random
enemy = ["Here is the pirate!", "Here is the dragon!"]


def print_pause(message_to_print):
        print(message_to_print)
        time.sleep(2)


def intro():
        print_pause("Get ready!")
        print_pause("You'r about to face the fighters.")
        print_pause(random.choice(enemy))


def win():
        print_pause("It's a good choice.")
        print_pause("Congratulations!")
        print_pause("You won!")
        playagain()


def playagain():
        again = input("Do you want to play again?(yes/no)")
        if "no" in again:
            print_pause("thanks for playing")
        elif "yes" in again:
            print_pause("OK, Let's go!")
            intro()
            play()
        else:
            print_pause("I can't understand")
            playagain()


def lose():
        print_pause("You lost!")
        print_pause("Game over")
        playagain()


def play():
        tool = input("would you use (sword) or the (dagger)?")
        if "sword" in tool:
            win()
        elif "dagger" in tool:
            lose()
        else:
            print_pause("I can't understand")
            play()
intro()
play()
