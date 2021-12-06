import random
import time


def main_guess():
    count = 0
    while True:

        number = random.randrange(0, 101)
        no1 = random.randrange(0, 101)
        no2 = random.randrange(0, 101)

        a = random.randrange(0, 3)
        b = random.randrange(0, 3)
        c = random.randrange(0, 3)

        ls = [0, 0, 0]

        if (a != b) and (a != c) and (b != c) and (no1 != no2) and (no1 != number) and (no2 != number):
            count += 1
            ls[a] = no1
            ls[b] = number
            ls[c] = no2

            print("\nNOTE:\nYour PC will generate a random number, you have to guess the correct number.\nYou can exit bye typing N/n instead of a number.\n")
            print("  GUESS THE NUMBER\n")

            print(f"{'No.1':>0}| {'No.2':^7}|{'No.3':>4}\n----|--------|------")
            print(f"{ls[0]:>3} | {ls[1]:^7}|{ls[2]:>3}")

            guess = input("\nEnter Number here = ")

            try:
                if guess == 'N' or guess == 'n':
                    print("\nYou left the Game!")
                    break
                elif int(guess) == int(number):
                    print(
                        f"\nYou guess the correct Number ({number}).\nNumber of Turns: {count}.\n")
                    break
            except:
                print("\nPlease Enter a Number!")
                time.sleep(3)


if __name__ == '__main__':
    main_guess()
    while True:
        yNo = input("Do you wan't to continue the game (Y/n) = ")

        yes = ['y', 'Y']
        no = ['N', 'n']

        if yNo in yes:
            print("Loading new Game......")
            time.sleep(2)
            main_guess()
        elif yNo in no:
            print("\nGAME OVER!")
            break
        elif (yNo not in yes) and (yNo not in no):
            print("\nmmmmm...")
            time.sleep(1.5)
            print("\nOne Humble Request, Please Quit Coding.\nThank You.")
            break
