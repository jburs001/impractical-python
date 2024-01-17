"""
Title: Random Name Generator
Author: Jon Burstein
Details: A program to make funny names.
"""
import sys 
import random

def main():

    print("Welcome to the dumb name generator.")
    print("These names are dumb as hell.\n")

    first = ('weiner', 'balls', 'gorgina', 'holden', 
             'hubert', 'dingus', 'chuck', 'remus', 'ribbert')
    last = ('nutsack','Mcdoodie', 'scrotus','bingus', 
            'mcdoogle', '9/11 was an inside job', 'dickhole')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("{} {}".format(first_name, last_name, file=sys.stderr))
        print("\n")

        try_again = input("\n\nTry again? Press enter else n to quit\n")
        if try_again.lower() == "n":
            break

        input("press Enter to exit.\n")
"""the __name__ is a built in variable that distinguishes stand alone or an imported module"""
if __name__ == "__main__":
    main()