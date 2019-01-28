import random

print("All women are QUEENS")

print("vs.")

print("If she BREATHES, she's a THOT!")

print("\n\nWho wins? Let's find out!")

inspirational = ''
flip = -1
while(flip != 1):
    inspirational = input("Type something inspirational.")
    flip = random.randint(0, 1)
    if flip == 0:
        print("If she breathes she's a THOT wins!")
        print("Just kidding! This game is rigged.")
    else:
        print("All women are QUEENS wins!")

print("Here's something inspirational for you: " + inspirational)
