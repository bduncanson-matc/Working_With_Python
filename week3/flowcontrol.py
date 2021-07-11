#!/usr/bin/env python3

print("""You enter a dark room with three doors. 
Do you go through door #1 , door #2 or door #3?""")

door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ============================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door Number 2 Logic =====================
elif door == "2":

    print("You stare into the endless abyss at Cthulhu's retina.\n")

    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    # == Insanity Logic ======================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":
        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
        print("Would you like to see an image of the dead Old God Y/N?")
        Cthun = input("-> ")
        if Cthun.lower() == "y":
            from PIL import Image
            cthunImg = Image.open("./Img/CthunDead.jpg")
            cthunImg.show()
        else:
            print("Maybe next time")
    else:
        print("N) The insanity rots your eyes into a pool of muck.")
        print("N) Good job!")
# == Door Number 3 Logic =====================
elif door == "3":
    print(
        "Behind door there there is a room in the center of which is you computer.\nYou are reminded that you have "
        "homework to do.\nAs you sit down your Giant Schnauzer, Kolt, demands attention.\n "
        "His means of communicating this need through incessant barking.\n"
        "What do you do?")

    print("\n1. Ignore Kolt and get to work\n")
    print("2. Despite your need to be productive you tend to the beast's needs\n "
          "and play ball with him for a half an hour.")
    # == Kolt The Beast Logic
    KoltyBoy = input("-> ")
    if KoltyBoy == "1":
        print("1) Terrible choice, the beast has more will power then you anticipated and\n"
              "does not leave you alone. You get nothing done and fail your assignment")
        print("1.) You Fail!")
    elif KoltyBoy == "2":
        print("2) After spending time with Kolt he wears down and takes a nap.\n"
              "Now you can finish your assignment and get caught up\n")
        print("Congratulations, you win!")
        print("Would you like to see a tired Kolty? Y/N")
        KoltyImg = input("-> ")
        if KoltyImg.lower() == "y":
            from PIL import Image
            koltImg = Image.open("./Img/KoltyBoy.jpg")
            koltImg.show()

    else:
        print("Procrastinate and not picking an option you get nothing done.\n")
        print("You Fail!")

else:
    print("You did not select a door??? Good Call :)")