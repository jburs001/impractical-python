import sys, random

print("Welcome to the dumb name generator.")
print("These names are dumb as hell.\n")

first = ('weiner', 'balls', 'gorgina', 'holden', 'hubert', 'dingus', 'chuck', 'remus', 'ribbert')
last = ('nutsack','Mcdoodie', 'scrotus','bingus', 'mcdoogle', '9/11 was an inside job', 'dickhole')

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print("{} {}".format(firstName, lastName, file=sys.stderr))
    print("\n")

    try_again = input("\n\nTry again? Press enter else n to quit\n")
    if try_again.lower() == "n":
        break

    input("\npress Enter to exit.")