"""Vault of Glass Demo"""
__author__ = "Erick Rodriguez"

# Name: Erick Rodriguez
# Description: This program is replication of Vault of Glass
#              the first raid introduced to the game Destiny(2014).
#              The program starts of with the actually beginning of the game
#              and a little bit of world building before delving into the raid.


import os
import random
import time


# Imports functions from various libraries.

# Intro
# Character Creation
# Entrance to the Vault
# Conflux Oracles
# Oracles (Templar)
# Templar Boss


def main():
    """The purpose of this main function is to basically be road map you would
       follow leading you through various encounters, other functions in this
       case, during the raid."""
    # Intro--------------------------------------------------------------------
    # Here is the intro cinematic to Destiny if you are interested:
    # https://www.youtube.com/watch?v=Ny7XhR4URZE&ab_channel=Shirrako

    for x in range(2):
        # This iterative function repeats the output twice.
        print("."), time.sleep(1), clear()
        # The sleep function from the time library delays the output
        # to the console by whatever time, in seconds, is given between the
        # parenthesis.
        print(".."), time.sleep(1), clear()
        print("..."), time.sleep(1), clear()
        print("Strange Voice: \"Guardian\""), time.sleep(2), clear()
    print("The voice keeps getting louder."), time.sleep(2), clear()

    # All the dialogue from this point on is from here:
    # https://www.youtube.com/watch?v=asCPvv3IqFo&ab_channel=Criko04

    print("Strange Voice: \"Eyes up Guardian.\""), time.sleep(2)
    input("<Enter anything to continue.>"), clear()

    print("You open your eyes, but before you can get a good look at your "
          "surroundings."), time.sleep(2)
    print("You see a little light in front of you."), time.sleep(2)
    print("It seems to be a small drone, no bigger than your hand.")
    time.sleep(2)
    print("In the center of it is a single glowing orb, its' eye perhaps?")
    time.sleep(2)
    # This is what a Ghost looks like:
    # https://assets.vg247.com/current//2017/03/destiny-ghost.png
    input("<Enter anything to continue.>"), clear()

    print("Strange Voice: \"It worked!\""), time.sleep(2)
    print("Strange Voice: \"You are alive!\""), time.sleep(2)
    print("Strange Voice: \"You don't know how long I've been looking "
          "for you.\""), time.sleep(2)
    print("Strange Voice: \"I'm a Ghost, well now I am actually your Ghost."
          "\""), time.sleep(2)
    print("Ghost: \"And you...\""), time.sleep(2)
    print("Ghost: \"Well you've been dead a long time.\""), time.sleep(2)
    print("Ghost: \"So you are going to see a lot of things you won't "
          "understand.\""), time.sleep(2)
    print(""), time.sleep(2)
    print("     What will you say?")
    print("     (A)\"What is this place?\"")
    print("     (B)\"I can't remember anything from my past.\"")
    print("     (C)\"What do we do now?\"(Exits Conversation)")

    while True:
        # An infinite loop that will continuously loop until a certain input
        # is entered.
        print("")
        choice = input("      >")
        # condition is met. In this case being option C.
        if (choice == 'A') or (choice == 'a'):
            # The == relational operator check to see if a value is the same as
            # another
            # An if statement that is used if the user's input matches
            # the desired input
            print(""), time.sleep(2)
            print("Ghost: \"This is place is an old Cosmodrome, a Russian ")
            print("        spaceport. People would go here to travel to ")
            print("        other planets.\"")
            print("")
            print("Enter another choice or enter C/c to exit the convo.")
        elif (choice == 'B') or (choice == 'b'):
            # An elif statement that is used because there is more than one
            # possible input.
            print(""), time.sleep(2)
            print("Ghost: \"As a Guardian you don't remember anything from")
            print("        your past life prior to your resurrection.\"")
            print("")
            print("Enter another choice or enter C/c to exit the convo.")
        elif (choice == 'C') or (choice == 'c'):
            print(""), time.sleep(2)
            print("Ghost: \"My scanners indicate a derelict ship inside this")
            print("        Cosmodrome, it won't be able to leave Earth's "
                  "atmosphere")
            print("        but it will be enough to get us to the Last City "
                  "and, ")
            print("        most importantly, to Commander Zavala.\"")
            time.sleep(3)

            break  # Exits the loop
        else:
            print("     Invalid Input")
            # An else statement that comes up if the user enters anything
            # besides the desired inputs.
            print("     Please enter one of the following: A/a, B/b", end="")
            # The end= argument will print two separate lines together
            print(" or C/c")

    print("")
    print("You hear a loud roar from the distance."), time.sleep(2)
    print("")
    print("Ghost: \"We better find that ship fast this is Fallen territory.")
    print("        We aren't safe here.\"")
    time.sleep(2)
    input("<Enter anything to enter the Cosmodrome.>"), clear()

    print("You and Ghost enter the long abandoned spaceport.")
    print("[Entrance]_|__________________[Ship]"), time.sleep(2), clear()
    print("You and Ghost make you way through the long abandoned spaceport.")
    print("[Entrance]____|_______________[Ship]"), time.sleep(2), clear()
    print("You and Ghost make you way through the long abandoned spaceport.")
    print("[Entrance]_______|____________[Ship]"), time.sleep(2), clear()
    print("You and Ghost make you way through the long abandoned spaceport.")
    print("[Entrance]__________|_________[Ship]"), time.sleep(2), clear()
    print("You and Ghost make you way through the long abandoned spaceport.")
    print("[Entrance]_____________|______[Ship]"), time.sleep(2), clear()
    print("You and Ghost make you way through the long abandoned spaceport.")
    print("[Entrance]________________|___[Ship]"), time.sleep(2), clear()
    print("You and Ghost make you way through the long abandoned spaceport.")
    print("[Entrance]__________________|_[Ship]"), time.sleep(2), clear()
    print("You have arrived at the ship!")
    print("[Entrance]____________________[Ship]"), time.sleep(2), clear()
    # This is a very simple visual interpretation of progressing
    # through an area.

    print("You have arrived at the ship!")
    print("")
    print("Ghost: \"There it is, our ticket out of here.\""), time.sleep(2)
    print("Ghost: \"Ready to leave, Guardian?\"")
    time.sleep(2)

    print(""), time.sleep(2)
    print("     What will you say?")
    print("     (A)\"You said we were going to the Last City?\"")
    print("     (B)\"You mentioned someone called Commander Zavala?\"")
    print("     (C)\"You said this was Fallen territory?\"")
    print("     (D)\"You sure this will get us out in one piece?\""
          "(Exits Conversation)")

    while True:
        print("")
        choice = input("      >")
        if (choice == 'A') or (choice == 'a'):
            print(""), time.sleep(2)
            print("Ghost: \"It is the final bastion of humanity and home of "
                  "the Traveler.\""), time.sleep(2)
            print("")
            print("You: \"The Traveler?\""), time.sleep(2)
            print("")
            print("Ghost: \"Oh just wait till you see it. Quite a sight!\"")
            print("")
            print("Enter another choice or enter D/d to exit the convo.")
        elif (choice == 'B') or (choice == 'b'):
            print(""), time.sleep(2)
            print("Ghost: \"He oversees all Guardian military operations.")
            print("        He'll be wanting to meet you as soon"
                  " as possible.\"")
            print("")
            print("Enter another choice or enter D/d to exit the convo.")
        elif (choice == 'C') or (choice == 'c'):
            print(""), time.sleep(2)
            print("Ghost: \"They are a nasty bunch. No one knows where they")
            print("        came from, but they clearly aren't from here with")
            print("        their four arms and eyes.\"")
            print("")
            print("Enter another choice or enter D/d to exit the convo.")
        elif (choice == 'D') or (choice == 'd'):
            print(""), time.sleep(2)
            print("Ghost: \"We won't be leaving orbit anytime soon, but it'll "
                  "get us to the city.\""), time.sleep(4), clear()
            break
        else:
            print("     Invalid Input")
            print("     Please enter one of the following: A/a", "B/b", "C/c "
                  + "or D/d", sep=', ')
            # The sep= argument will separate objects, in this case it will
            # separate them with ', '.

    print("[Cosmodrome]_>___________________________[Last City]")
    time.sleep(2), clear()
    print("[Cosmodrome]___>_________________________[Last City]")
    time.sleep(2), clear()
    print("[Cosmodrome]______>______________________[Last City]")
    time.sleep(2), clear()
    print("[Cosmodrome]_________>___________________[Last City]")
    time.sleep(2), clear()
    print("[Cosmodrome]____________>________________[Last City]")
    time.sleep(2), clear()
    print("[Cosmodrome]_______________>_____________[Last City]")
    time.sleep(2), clear()
    print("[Cosmodrome]__________________>__________[Last City]")
    time.sleep(2), clear()
    print("[Cosmodrome]_____________________>_______[Last City]")
    time.sleep(2), clear()
    print("[Cosmodrome]________________________>____[Last City]")
    time.sleep(2), clear()
    print("[Cosmodrome]___________________________>_[Last City]")
    time.sleep(2), clear()
    # This is a depiction of the player traveling to the Last City on
    # their ship

    # Arriving at the Last City -----------------------------------------------

    print(3 * "\n")
    print(" " * 10 + "[You arrive at the Last City]")
    time.sleep(3), clear()
    # The * string operator spams the string by the integer given.
    # The + string operator concatenates two string literals together.
    last_city_icon()
    print("")
    print("    |==============================|")
    print("    |As you arrive at the Last City|")
    print("    | you notice the giant sphere  |")
    print("    |      hovering over it.       |")
    print("    |=============================+|")
    time.sleep(5), clear()
    last_city_icon()
    print("")
    print("Ghost: \"That's the Traveler."), time.sleep(2)
    print("        It created us after the Collpase to locate")
    print("        and resurrect people like you to wield the Light")
    time.sleep(2)
    print("        as Guardians.\""), time.sleep(1)
    input(" " * 8 + "<Enter anything to continue.>"), clear()
    last_city_icon()
    print("")
    print("Ghost: \"Look over there!\""), time.sleep(3), clear()
    tower_icon()
    print("")
    print("Ghost: \"That's the Tower, where all Guardians go to")
    print("        to stock up on supplies and store the valuables they")
    print("        find through out their missions.\"")
    input(" " * 8 + "<Enter anything to continue.>"), clear()
    tower_icon()
    print("")
    print("Ghost: \"It is also where we are going to meet with")
    print("        Commander Zavala.\""), time.sleep(2)
    print("Ghost: \"Just land there whenever you are ready, Guardian.\"")
    input(" " * 8 + "<Enter anything to continue.>"), clear()
    print("")
    print("    |===============================|")
    print("    |  As you get out of your ship  |")
    print("    |    you are overwhelmed with   |")
    print("    |       everything you see.     |")
    print("    |===============================|")
    input(" " * 6 + "<Enter anything to continue.>"), clear()
    print("")
    print("    |===============================|")
    print("    |  You never expected the Tower |")
    print("    |       to be this bustling     |")
    print("    |          with people.         |")
    print("    |===============================|")
    input(" " * 6 + "<Enter anything to continue.>"), clear()
    print("Ghost: \"Come on Guardian, this is the way to")
    print("        Commander Zavala's office.\"")
    time.sleep(4), clear()
    print("")
    print("    |===============================|")
    print("    | You follow Ghost through the  |")
    print("    |   Tower to Zavala's office.   |")
    print("    |===============================|")
    time.sleep(4), clear()

    # Meeting Zavala ----------------------------------------------------------

    print("")
    print("    |===============================|")
    print("    | You arrive at Zavala's Office |")
    print("    |===============================|")
    input(" " * 6 + "<Enter anything to continue.>"), clear()
    print(" You walk into the office and see a man  ")
    print(" on the opposite side of the room staring out")
    print(" a large window down at the city.")
    time.sleep(4)
    print("")
    print(" He turns around and notices you.")

    # This is what Commander Zavala looks like:
    # https://d2.destinygamewiki.com/mediawiki/images/6/64/Commander_Zavala.PNG

    time.sleep(4), clear()
    print("Commander Zavala: \"You must be the new Guardian I heard about.")
    print("                   It's always nice to see a new recruit.\"")
    time.sleep(2)
    print("Commander Zavala: \"Before I give you your first assignment")
    print("                   we should find a name for you.")
    input(" " * 6 + "<Enter anything to create your character.>"), clear()

    # Picking your name and class ---------------------------------------------

    player_class = None
    player_name = input("What is your name, Guardian? ")
    print("Pick a class:")
    player_class = guardian_classes(player_class)
    print("Guardian Info")
    print("Name:", player_name)
    print("Class:", player_class)
    input("<Enter anything to finish.>"), clear()

    print("Commander Zavala: \"Well then that settles it.")
    time.sleep(2)
    print("Commander Zavala: \"" + player_name + ", welcome to the Vanguard.")
    input(" " * 4 + "<Enter anything to begin your Destiny.>"), clear()

    # Tutorial Complete -------------------------------------------------------
    player_level = 210
    tutorial_complete = True
    # These variables are just requirements that must be met at some later
    # point in the program to begin the raid.

    # Time Skip ---------------------------------------------------------------
    print("")
    print("          5 YEARS"), time.sleep(3), clear()
    print("")
    print("          5 YEARS LATER..."), time.sleep(4), clear()

    print("    |==============================================|")
    print("    | It was 5 years ago when you were resurrected |")
    print("    |         by the light of the Traveler.        |")
    print("    |==============================================|")
    input(" " * 15 + "<Enter anything to continue.>"), clear()
    print("    |==============================================|")
    print("    |   You have made quite a name for yourself    |")
    print("    |                since then.                   |")
    print("    |==============================================|")
    input(" " * 15 + "<Enter anything to continue.>"), clear()
    print("    |==============================================|")
    print("    |      You fought back against the Fallen,     |")
    print("    |    a species of four-armed humanoid pirates  |")
    print("    |      and mercenaries who originate from a    |")
    print("    |                long dead world.              |")
    print("    |==============================================|")
    input(" " * 15 + "<Enter anything to continue.>"), clear()
    # These are the Fallen:
    # https://64.media.tumblr.com/d9c3c8398b5a0717a83713ff8f342b69/tumblr_owo457fbIP1rvqqx2o3_1280.jpg
    # https://64.media.tumblr.com/b637b4cacd0f22891c967cc6dbae9d92/tumblr_owo457fbIP1rvqqx2o2_1280.jpg
    # https://64.media.tumblr.com/f9bc915a2d0f6ae7c7f0e332acb01aff/tumblr_owo457fbIP1rvqqx2o4_1280.jpg

    print("    |==============================================|")
    print("    |     You left victorious when confronting     |")
    print("    |      the unstoppable might of the Cabal.     |")
    print("    |      A race of large bipedal rhino-like      |")
    print("    |   soldiers, who conquer worlds with their    |")
    print("    |             military superiority.            |")
    print("    |==============================================|")
    input(" " * 15 + "<Enter anything to continue.>"), clear()
    # These are the Cabal:
    # https://cdnb.artstation.com/p/assets/images/images/007/424/369/large/roderick-weise-centurion-blue-color-front.jpg?1506028559

    print("    |==============================================|")
    print("    |     You have faced Death itself with the     |")
    print("    |          countless hordes of Hive.           |")
    print("    |   An undead-like race of aliens who follow   |")
    print("    |   The Sword Logic, which dictates that they  |")
    print("    |   must destroy other civilizations in order  |")
    print("    |          to obtain paracausal power.         |")
    print("    |==============================================|")
    input(" " * 15 + "<Enter anything to continue.>"), clear()
    # These are the Hive:
    # https://pbs.twimg.com/media/EH-JiMhVUAA2_6v.jpg
    # https://i.pinimg.com/originals/e4/fe/70/e4fe7009b8aec10e2d2d76e5a8cdc9b1.png
    # https://happygamer.com/wp-content/uploads/2019/08/frozen-hive-destiny-2-warmind.jpg
    # I got some info from here: https://www.destinypedia.com/Hive

    print("    |==============================================|")
    print("    |     You have stopped the onslaught of the    |")
    print("    |        Vex, a cyber-organic species as       |")
    print("    |         ancient as the Universe itself.      |")
    print("    |    However, the full scope of their powers   |")
    print("    |                remain a mystery.             |")
    print("    |==============================================|")
    input(" " * 15 + "<Enter anything to continue.>"), clear()
    # These are the Vex:
    # https://d1lss44hh2trtw.cloudfront.net/assets/article/2017/12/20/Destiny-2-Where-to-Find-Vex-Fanatics_1200x500.jpg
    # https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2017/12/Destiny-2-Where-to-Find-Vex-Fanatics-Inverted-Spire-Strike.jpg
    # I got some info from here: https://www.destinypedia.com/Vex

    print("    |==============================================|")
    print("    |    Your story picks up with your character   |")
    print("    |                 in their ship                |")
    print("    |   making their way back to the Tower from a  |")
    print("    |  successful mission taking out the notorious |")
    print("    |     commander of the Cabal Siege Dancers,    |")
    print("    |             Valus Ta'Aurc, on Mars           |")
    print("    |                                              |")
    print("    |                When suddenly...              |")
    print("    |==============================================|")
    input(" " * 15 + "<Enter anything to continue.>"), clear()

    # Urgent message from Zavala ----------------------------------------------
    print("Ghost: \"" + player_name + ", you have an incoming")
    print("        transmission from Commander Zavala.\"")
    input("       <Enter anything to answer the call.>"), clear()

    print("Zavala: \"Good work on taking care of Valus Ta'Aurc,")
    print("         but the time for celebrations must be cut short.\"")
    time.sleep(4), clear()
    print("Zavala: \"We have recently received an alarming transmission")
    print("         from Venus...\"")
    time.sleep(3)
    print("Zavala: \"It came from a fireteam... but we never sent any")
    print("         fireteams to that sector. It is too overrun with ")
    print("         Vex forces.\"")
    input("       <Enter anything to continue.>"), clear()
    print("Zavala: \"But if what the transmission says is ture, then")
    print("         we must get to the bottom of what that fireteam")
    print("         was doing on Venus and what they found.\"")
    input("       <Enter anything to continue.>"), clear()
    print("Zavala: \"You will rendezvous with five other Guardians")
    print("         on Venus were the signal originated.\"")
    time.sleep(3)
    print("Zavala: \"Be careful", player_name + ", this could be a trap.\"")
    time.sleep(3)
    print("Zavala: \"Zavala, out.\"")
    print("")

    # Raid Requirement Check --------------------------------------------------
    input("<Enter anything to begin the raid>")
    while True:
        # This checks if the player meets the requirements to begin the raid.
        if (player_level > 200) and not (tutorial_complete is False):
            print("BEGINNING VAULT OF GLASS RAID!"), time.sleep(2)
            clear()
            break
        else:
            input("YOU ARE NOT PREPARED!")

    # Vault Door --------------------------------------------------------------
    print("")
    print("                   _____________")
    print("                  /      |      \\")
    print("                 /       O       \\")
    print("                 |       |       |")
    print("                 |       O       |")
    print("                 |       |       |")
    print("                 \\       O       /")
    print("             _____\\______|______/_____")
    print("            /    /===============\\    \\")
    print("           /   /===================\\   \\")
    print("          /__/=======================\\__\\")
    print("         /===============================\\")
    time.sleep(3)
    print("    |==============================================|")
    print("    | You approach what appears to be a vault door |")
    print("    |  You notice that there are three mechanisms  |")
    print("    |They could be what are keeping the door locked|")
    print("    |==============================================|")
    time.sleep(6), clear()

    vault_door()

    # Entering the Vault ------------------------------------------------------
    print("You enter the vault")
    time.sleep(3), clear()
    # Finding the Conflux Room ------------------------------------------------
    print("You enter a large room")
    time.sleep(3), clear()
    conflux_oracles()
    print("             IT GOES DARK...")
    time.sleep(1), clear()
    print("             IT GOES DARK... THEN...")
    time.sleep(3), clear()
    # Templar Appears ---------------------------------------------------------
    for x in range(4):
        templar_arena(oracle_position=6)
        time.sleep(0.2)
        clear()
        templar_arena(oracle_position=4)
        time.sleep(0.2)
        clear()
        templar_arena(oracle_position=2)
        time.sleep(0.2)
        clear()
        templar_arena(oracle_position=5)
        time.sleep(0.2)
        clear()
        templar_arena(oracle_position=1)
        time.sleep(0.2)
        clear()
        templar_arena(oracle_position=6)
        time.sleep(0.2)
        clear()
        templar_arena(oracle_position=3)
        time.sleep(0.2)
        clear()

    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]  \\     /  [  ]  |")
    print("       |         \\   /         |")
    print("       |   -------[ ]-------   |")
    print("       |         /   \\         |")
    print("       |  [  ]  /     \\  [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\___    [   ]    ___/")
    print("          |       YOU       |")
    print("          |=================|")
    time.sleep(1), clear()
    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |         \\   /         |")
    print("       |       ---[ ]---       |")
    print("       |         /   \\         |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    time.sleep(1), clear()
    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |                       |")
    print("       |          [ ]          |")
    print("       |                       |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    time.sleep(3), clear()

    for x in range(6):
        print("")
        print("")
        print("")
        print("     ==========================================")
        print("      ! !YOU HEAR A LOUD MECHANICAL SCREECH! ! ")
        print("     ==========================================")
        time.sleep(0.5)
        clear()
        print("")
        print("")
        print("")
        print("     ==========================================")
        print("     ! ! YOU HEAR A LOUD MECHANICAL SCREECH ! !")
        print("     ==========================================")
        time.sleep(0.5)
        clear()

    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |                       |")
    print("       |           o           |")
    print("       |                       |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    print("")
    print("    |=============================|")
    print("    |           SUDDENLY          |")
    print("    |     A WHITE GLOW APPEARS    |")
    print("    | IN THE CENTER OF THE ARENA  |")
    print("    |=============================|")
    time.sleep(1), clear()
    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |                       |")
    print("       |          (o)          |")
    print("       |                       |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    print("")
    print("    |=============================|")
    print("    |           SUDDENLY          |")
    print("    |     A WHITE GLOW APPEARS    |")
    print("    | IN THE CENTER OF THE ARENA  |")
    print("    |=============================|")
    time.sleep(1), clear()
    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |                       |")
    print("       |         ((o))         |")
    print("       |                       |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    print("")
    print("    |=============================|")
    print("    |           SUDDENLY          |")
    print("    |     A WHITE GLOW APPEARS    |")
    print("    | IN THE CENTER OF THE ARENA  |")
    print("    |=============================|")
    time.sleep(1), clear()
    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |                       |")
    print("       |         (( ))         |")
    print("       |                       |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    print("")
    print("    |=============================|")
    print("    |           SUDDENLY          |")
    print("    |     A WHITE GLOW APPEARS    |")
    print("    | IN THE CENTER OF THE ARENA  |")
    print("    |=============================|")
    time.sleep(1), clear()
    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |                       |")
    print("       |         (   )         |")
    print("       |                       |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    print("")
    print("    |=============================|")
    print("    |           SUDDENLY          |")
    print("    |     A WHITE GLOW APPEARS    |")
    print("    | IN THE CENTER OF THE ARENA  |")
    print("    |=============================|")
    time.sleep(1), clear()
    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |         <<o>>         |")
    print("       |          <V>          |")
    print("       |           v           |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    print("")
    print("    |=============================|")
    print("    |      A GIANT VEX HYDRA      |")
    print("    |         HAS APPEARED        |")
    print("    |=============================|")
    time.sleep(3), clear()

    # Templar Boss Fight ------------------------------------------------------
    templar_boss()
    # To be continued ---------------------------------------------------------
    print("             To be continued...")
    time.sleep(3), clear()
    input("     <Input anything to exit the program>")


def last_city_icon():
    """The purpose of this function is to be called when a visual
       representation of the Last City is needed."""
    print("")
    print("             THE LAST CITY")
    print("")
    print("         /-------------------\\")
    print("        /                     \\")
    print("       /                       \\")
    print("      /                         \\")
    print("      |                         |")
    print("      |                         |")
    print("      |                         |")
    print("      |                         |")
    print("      |                         |")
    print("      \\                         /")
    print("       \\                       /")
    print("        \\                     /")
    print("         \\___________________/")
    print("")
    print("    _        _          /|   |\\")
    print("  _| \\_  |\\ | |   ___|\\| |\\  | \\__|| _")
    print(" | |  _\\_| || |_ /   | | | |_||\\__||| |")
    print("_|_|_|_|_|_/|_|_|____|_|_|_|__|___|_|_|_")
    # This is an interpretation of the Last City, the link in the bottom
    # is what the last city actually looks like.
    # https://static.wikia.nocookie.net/shaniverse/images/1/16/3237064-2434917184-nick-.jpg/revision/latest?cb=20200819024029


def tower_icon():
    """The purpose of this function is to be called when a visual
       representation of the Tower is needed."""
    print("")
    print("        THE TOWER")
    print("")
    print("             |\\  |\\")
    print("          __[ ]_[ ]_")
    print("      ____[__]_\\=/_[_]__")
    print("      \\_______/| |\\____/")
    print("          \\_\\__| |__/")
    print("        ___|_[]| |_|_")
    print("       /  |    | |   |")
    print("      /   |    | |   |")
    print("     /    |    | |   |")
    print("     |    |    | |   |")
    print("     |    |    | |   |")
    print("    /     |____| |___|")
    print("   /      /    | |   |")
    print("  /      / ____| |__ |")
    print(" /      / /====| |==||")
    print(" |      | |====| |==||")
    print("/       / |====| |==||")
    # This is what the tower actually looks like:
    # https://cdna.artstation.com/p/assets/images/images/000/277/412/large/1920_jessevandijk_thetower.jpg?1414687269&dl=1


def guardian_classes(player_class):
    """The purpose of this function is for the user to select which class they
       will be playing, as well as showing the abilities which those classes
       have.
       player_class - a string literal of the class name."""
    print(player_class)
    enemy_dmg_resistance = 95
    damage_taken = float(20.0)
    base_dmg = 5
    ally_health = 100
    print("A. Titan:")
    print("    Their ultimate ability launched them towards the enemy")
    print("    and does exponential damage towards their target.")
    print("    -Base Damage:", base_dmg)
    print("    -Ult Damage:", base_dmg ** 2)
    # The ** numeric operator exponentially increases any given int value.
    print("B. Hunter:")
    print("    Their ultimate ability reduces the enemies damage")
    print("    resistance by half.")
    print("    -Enemy Damage Resistance:", enemy_dmg_resistance)
    print("    -Enemy Reduced Resistance:", enemy_dmg_resistance // 2)
    # The // numeric operator divides and give the result as a whole number.
    print("C. Warlock:")
    print("    Their ultimate ability doubles allies health for")
    print("    a limited amount of time. As well as reducing the")
    print("    the damage taken by half for that same amount of ")
    print("    time.")
    print("    -Allies Health:", ally_health)
    print("    -Damage Taken:", damage_taken)
    print("    -Allies Health Buffed:", ally_health * 2)
    #
    print("    -Reduced Damage Taken:", damage_taken / 2)
    # The / numeric operator divides.
    while True:
        choice = input(">")
        if (choice == 'A') or (choice == 'a'):
            print("You chose Titan"), time.sleep(2)
            player_class = "Titan"
            clear()
            return player_class
        elif (choice == 'B') or (choice == 'b'):
            print("You chose Hunter"), time.sleep(2)
            player_class = "Hunter"
            clear()
            return player_class
        elif (choice == 'C') or (choice == 'c'):
            print("You chose Warlock"), time.sleep(2)
            player_class = "Warlcok"
            clear()
            return player_class
        else:
            print("     Invalid Input")
            print("     Please enter one of the following: A/a", "B/b" +
                  " or C/c", sep=', ')


def vault_door():
    """The purpose of this function is have the player unlock the vault door by
       finding out he remainder of an equation."""
    # This function needs to be solved in order to open the vault door.
    while True:
        alpha_lock_true = random.randint(16, 20)
        alpha_lock_false = random.randint(16, 20)
        beta_lock_true = random.randint(10, 15)
        beta_lock_false = random.randint(10, 15)
        gamma_lock_true = random.randint(17, 25)
        gamma_lock_false = random.randint(17, 25)

        vault_unlock = (alpha_lock_true + gamma_lock_true) % beta_lock_true
        # The % numeric operator divides and gives the remainder.
        print(" ALPHA")
        print(alpha_lock_true, "|", alpha_lock_false)
        print(" BETA")
        print(beta_lock_true, "|", beta_lock_false)
        print(" GAMMA")
        print(gamma_lock_true, "|", gamma_lock_false)
        print("")
        print("The Alpha and Gamma were UNITED at first,")
        print("Then the treachery of the Beta left them DIVIDED,")
        print("Only the chosen", vault_unlock, "REMAINED.")
        print("")

        # The user must solve the simple riddle and figure out that they
        # need to add one of the numbers from both the GAMMA and ALPHA locks
        # then divide it by one of the number of the BETA lock and get the
        # remainder that matches with the one in the riddle.

        print("Which cluster will you give to the ALPHA:")
        print(alpha_lock_true, "or", alpha_lock_false)
        while True:
            # This is a try/except condition that will continue to loop until
            # the user inputs an integer.
            alpha_lock_choice = input(">")
            try:
                alpha_lock_choice = int(alpha_lock_choice)
                break
            except ValueError:
                print("")
                print("     Invalid Input")
                print(" Please, input one of the")
                print("    two values given.")
                print("")
        print("")
        print("Which cluster will you give to the BETA:")
        print(beta_lock_true, "or", beta_lock_false)
        while True:
            beta_lock_choice = input(">")
            try:
                beta_lock_choice = int(beta_lock_choice)
                break
            except ValueError:
                print("")
                print("     Invalid Input")
                print(" Please, input one of the")
                print("    two values given.")
                print("")
        print("")
        print("Which cluster will you give to the GAMMA:")
        print(gamma_lock_true, "or", gamma_lock_false)
        while True:
            gamma_lock_choice = input(">")
            try:
                gamma_lock_choice = int(gamma_lock_choice)
                break
            except ValueError:
                print("")
                print("     Invalid Input")
                print(" Please, input one of the")
                print("    two values given.")
        print("")
        user_lock_combo = \
            (alpha_lock_choice + gamma_lock_choice) % beta_lock_choice

        if user_lock_combo == vault_unlock:
            print("You hear mechanism behind the door start to shift.")
            time.sleep(2)
            print("The door opens")
            time.sleep(2)
            clear()
            break
        else:
            print("The numbers glow red and begin to shift again.")
            time.sleep(2)


def conflux_oracles():
    """This functions plays the role of the oracle encounter in the actually
       VOG (Vault of Glass) raid, where the player has to keep track of the
       order in which their designated oracle appears in."""
    # This whole function is replicating this mechanic from the raid
    # https://youtu.be/ZwwvvG0dM4Q?t=355
    conflux_checkpoint = 1

    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |                       |")
    print("       |          [*]          |")
    print("       |                       |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    print("")
    print("    |=============================|")
    print("    |     Input \'q\' to shoot      |")
    print("    |           the cube          |")
    print("    |=============================|")
    # This starts the encounter
    while True:
        choice = input(" " * 17 + ">")
        if choice == 'q':
            print("")
            print("         You shoot the cube..."), time.sleep(3)
            break
        else:
            print("")
            print("             Invalid Input")
            print("           Please, input \'q\'")
    clear()

    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |                       |")
    print("       |          [*]          |")
    print("       |                       |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    time.sleep(1), clear()
    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |         \\   /         |")
    print("       |       ---[ ]---       |")
    print("       |         /   \\         |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    time.sleep(1), clear()
    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]  \\     /  [  ]  |")
    print("       |         \\   /         |")
    print("       |   -------[ ]-------   |")
    print("       |         /   \\         |")
    print("       |  [  ]  /     \\  [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\___    [   ]    ___/")
    print("          |       YOU       |")
    print("          |=================|")
    time.sleep(1), clear()
    # The three sets of figures on stop in just an animation of the
    # encounter beginning.
    templar_arena(oracle_position=0)
    # This calls the arena when no oracles have appeared.
    time.sleep(3)
    clear()
    print("")
    print("")
    print("")
    print("")
    print("     {[Conflux integrity at 100%]}"), time.sleep(4)
    clear()
    templar_arena(oracle_position=0)
    print("")
    print("    |=============================|")
    print("    |   Keep track of where the   |")
    print("    |   oracle in front of YOU    |")
    print("    |   appears in the sequence.  |")
    print("    |=============================|")
    time.sleep(5), clear()

    while True:
        templar_arena(oracle_position=0)
        time.sleep(2), clear()
        # The rest of the code under this function
        # is the random cycling of the oracle spawn sequence.
        first_oracle_set = random.randint(1, 2)
        # This first oracle set gives the player a random chance of
        # being selected and first or second in the sequence.
        # Same applies for the other sets following this one.
        for x in range(2):
            if first_oracle_set == 1:
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=4)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=5)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()

            elif first_oracle_set == 2:
                templar_arena(oracle_position=5)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=6)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()

        templar_arena(oracle_position=0)
        print("")
        print("    |=============================|")
        print("    |In what place of the sequence| ")
        print("    |  did your oracle appear in: |")
        print("    |=============================|")
        print("    | 1 : If it was the first.    |")
        print("    | 2 : If it was the second    |")
        print("    | 3 : If it was the third.    |")
        print("    | 4 : If it was the fourth.   |")
        print("    |=============================|")

        while True:
            # This is a try/except condition that will continue to loop until
            # the user inputs an integer.
            user_oracle = input("           Your answer: ")
            try:
                user_oracle = int(user_oracle)
                break
            except ValueError:
                print("")
                print("             Invalid Input")
                print("       Please, enter an integer.")
        # https://stackoverflow.com/questions/40002645/reject-user-input-if-criteria-not-met-in-python

        if user_oracle == first_oracle_set:
            clear()
            print("")
            print("")
            print("")
            print("")
            print("     {[Conflux integrity at 75%]}"), time.sleep(4)
            clear()
        elif user_oracle != first_oracle_set:
            clear()
            print("")
            print("")
            print("")
            print("    ===============================")
            print("    !!!!A LOUD ALARM IS SET OFF!!!!")
            print("    ===============================")
            time.sleep(3)
            print("      ...everything goes dark..."), time.sleep(2)
            clear(), time.sleep(2)
            fail_screen(conflux_checkpoint)
            clear()

        second_oracle_set = random.randint(2, 5)
        for x in range(2):
            if second_oracle_set == 2:
                templar_arena(oracle_position=5)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=3)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=4)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()
            elif second_oracle_set == 3:
                templar_arena(oracle_position=3)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=6)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=5)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()
            elif second_oracle_set == 4:
                templar_arena(oracle_position=6)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=4)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=5)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()
            elif second_oracle_set == 5:
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=4)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=6)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=3)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()
        templar_arena(oracle_position=0)
        print("")
        print("    |=============================|")
        print("    |In what place of the sequence| ")
        print("    |  did your oracle appear in: |")
        print("    |=============================|")
        print("    | 1 : If it was the first.    |")
        print("    | 2 : If it was the second    |")
        print("    | 3 : If it was the third.    |")
        print("    | 4 : If it was the fourth.   |")
        print("    | 5 : If it was the fifth.    |")
        print("    |=============================|")

        while True:
            user_oracle = input("           Your answer: ")
            try:
                user_oracle = int(user_oracle)
                break
            except ValueError:
                print("")
                print("             Invalid Input")
                print("       Please, enter an integer.")

        if user_oracle == second_oracle_set:
            clear()
            print("")
            print("")
            print("")
            print("")
            print("     {[Conflux integrity at 50%]}"), time.sleep(4)
            clear()
        elif user_oracle != second_oracle_set:
            clear()
            print("")
            print("")
            print("")
            print("    ===============================")
            print("    !!!!A LOUD ALARM IS SET OFF!!!!")
            print("    ===============================")
            time.sleep(3)
            print("      ...everything goes dark..."), time.sleep(2)
            clear(), time.sleep(2)
            fail_screen(conflux_checkpoint)
            clear()

        third_oracle_set = random.randint(2, 6)
        for x in range(2):
            if third_oracle_set == 2:
                templar_arena(oracle_position=3)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=5)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=6)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=4)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()
            elif third_oracle_set == 3:
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=6)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=3)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=4)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=5)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()
            elif third_oracle_set == 4:
                templar_arena(oracle_position=3)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=5)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=4)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=6)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()
            elif third_oracle_set == 5:
                templar_arena(oracle_position=5)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=3)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=4)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=6)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()
            elif third_oracle_set == 6:
                templar_arena(oracle_position=6)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=2)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=4)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=5)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=3)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=1)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=0)
                time.sleep(2)
                clear()
        templar_arena(oracle_position=0)
        print("")
        print("    |=============================|")
        print("    |In what place of the sequence| ")
        print("    |  did your oracle appear in: |")
        print("    |=============================|")
        print("    | 1 : If it was the first.    |")
        print("    | 2 : If it was the second    |")
        print("    | 3 : If it was the third.    |")
        print("    | 4 : If it was the fourth.   |")
        print("    | 5 : If it was the fifth.    |")
        print("    | 6 : If it was the sixth.    |")
        print("    |=============================|")

        while True:
            user_oracle = input("           Your answer: ")
            try:
                user_oracle = int(user_oracle)
                break
            except ValueError:
                print("")
                print("             Invalid Input")
                print("       Please, enter an integer.")

        if user_oracle == third_oracle_set:
            clear()
            print("")
            print("")
            print("")
            print("")
            print("     {[Conflux integrity at 25%]}"), time.sleep(4)
            clear()
            break
        elif user_oracle != third_oracle_set:
            clear()
            print("")
            print("")
            print("")
            print("    ===============================")
            print("    !!!!A LOUD ALARM IS SET OFF!!!!")
            print("    ===============================")
            time.sleep(3)
            print("      ...everything goes dark..."), time.sleep(2)
            clear(), time.sleep(2)
            fail_screen(conflux_checkpoint)
            clear()


def templar_boss():
    """The purpose of this function is to be called when the player initiates
       the fight with the Templar and when it is time to damage the boss after
       the user completes the oracle challenge, templar_oracles function."""
    print("          _______|===|_______")
    print("         /                   \\")
    print("        /        [   ]        \\")
    print("       /                       \\")
    print("       |  [  ]           [  ]  |")
    print("       |         <<o>>         |")
    print("       |          <V>          |")
    print("       |           v           |")
    print("       |  [  ]           [  ]  |")
    print("       \\                       /")
    print("        \\        [   ]        /")
    print("         \\       [   ]       /")
    print("          |       YOU       |")
    print("          |=================|")
    # This represents the arena where the Templar fight will take place in.
    # A simplified version of the templar is in the middle of the arena.
    print("")
    print("    |=============================|")
    print("    |     Input \'q\' to begin      |")
    print("    |          the fight          |")
    print("    |=============================|")
    while True:
        choice = input(" " * 17 + ">")
        if choice == 'q':
            print("")
            break
        else:
            print("")
            print("             Invalid Input")
            print("           Please, input \'q\'")
    time.sleep(3), clear()

    templar_health = 100
    while templar_health > 1:
        templar_oracles()
        print("          TEMPLAR HEALTH:", str(templar_health) + "K")
        print("")
        print("               __/\\O/\\__")
        print("            {8}\\_-<o>-_/{8}")
        print("                 \\ V /")
        print("                 o-V-o")
        print("                  <V>")
        # The text art is supposed to represent the Templar form the game
        # https://destiny.wiki.gallery/images/thumb/b/b7/TheTemplarGrimoireCard.jpg/300px-TheTemplarGrimoireCard.jpg
        print("")
        print("    |=============================|")
        print("    |     Input \'q\' to damage     |")
        print("    |           the boss!         |")
        print("    |=============================|")
        user_input = input(" " * 17 + ">")
        if user_input == str('q'):
            clear()
            print("             25K DAMAGE!!!"), time.sleep(2), clear()
            templar_health = damage_calculation(templar_health)
            print("          TEMPLAR HEALTH:", str(templar_health) + "K")
            print("")
            print("               __/\\O/\\__")
            print("            {8}\\_-<o>-_/{8}")
            print("                 \\ V /")
            print("                 o-V-o")
            print("                  <V>")
            time.sleep(3), clear()
        elif user_input != str('q'):
            print("        ==========================")
            print("        !!!!DAMAGE PHASE FAILED!!!")
            print("        ==========================")
            time.sleep(3), clear()
            print("    {The oracles begin to glow again...}"), time.sleep(3)
            clear()
            templar_oracles()
    print("    |===============================|")
    print("    |      The Templar has been     |")
    print("    |           destroyed!          |")
    print("    |===============================|")
    time.sleep(4), clear()


def templar_oracles():
    """This function plays a very similar role to the conflux_oracle function,
       the only difference being that not as many oracles appear and once the
       user inputs the correct option they will start to damage the boss."""
    templar_checkpoint = 2
    while True:
        templar_arena(oracle_position=7)
        time.sleep(2), clear()

        first_oracle_set = random.randint(0, 3)
        for x in range(2):
            if first_oracle_set == 0:
                templar_arena(oracle_position=9)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=13)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=10)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=7)
                time.sleep(2)
                clear()

            elif first_oracle_set == 1:
                templar_arena(oracle_position=8)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=12)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=9)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=7)
                time.sleep(1)
                clear()

            elif first_oracle_set == 2:
                templar_arena(oracle_position=10)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=8)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=11)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=7)
                time.sleep(1)
                clear()

            elif first_oracle_set == 3:
                templar_arena(oracle_position=10)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=13)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=8)
                time.sleep(1)
                clear()
                templar_arena(oracle_position=7)
                time.sleep(1)
                clear()

        templar_arena(oracle_position=7)
        print("")
        print("    |=============================|")
        print("    |In what place of the sequence| ")
        print("    |  did your oracle appear in: |")
        print("    |=============================|")
        print("    | 0 : If it never appeared.   |")
        print("    | 1 : If it was the first.    |")
        print("    | 2 : If it was the second.   |")
        print("    | 3 : If it was the third.    |")
        print("    |=============================|")

        while True:
            user_oracle = input("           Your answer: ")
            try:
                user_oracle = int(user_oracle)
                break
            except ValueError:
                print("")
                print("             Invalid Input")
                print("       Please, enter an integer.")

        if user_oracle == first_oracle_set:
            clear()
            print("")
            print("")
            print("")
            print("")
            print("    {[TEMPLAR SHIELDS DOWN!]}"), time.sleep(1)
            print("     {[PREPARE TO ATTACK!]}"), time.sleep(3)
            clear()
            break

        elif user_oracle != first_oracle_set:
            clear()
            print("")
            print("")
            print("")
            print("    ===============================")
            print("    !!!!A LOUD ALARM IS SET OFF!!!!")
            print("    ===============================")
            time.sleep(3)
            print("      ...everything goes dark..."), time.sleep(2)
            clear(), time.sleep(2)
            fail_screen(templar_checkpoint)
            clear()


def damage_calculation(boss_health):
    """This function calculates and returns the boss' health after damage is
       done to it.
       boss_health - an int value of the boss' health"""
    boss_health -= 25
    # This is a shortcut operator for subtraction
    return boss_health


def fail_screen(fail_code):
    """The purpose of this function is to play the role of a fail screen which
       is called when player player fails an encounter.
       fail_code - is an int value that dictates what checkpoint the player
       will be returned to."""
    # This function is called when the user fails an encounter
    # and sends them back to the previous checkpoint.

    print("               ______________")
    print("              /              \\")
    print("             /   ____  ____   \\")
    print("             |  /   /  \\   \\  |")
    print("             |  \\__/ /\\ \\ _/  |")
    print("              \\_     ||    __/")
    print("                 \\        /")
    print("                  UUUUUUUU")
    print("       /_____________________________\\")
    print("       |<<THE DARKNESS CONSUMED YOU>>|")
    print("       \\-----------------------------/")
    print("         <Enter anything to respawn>")
    print("          <at the last checkpoint.>")
    input("                  >")
    clear()

    if fail_code == 1:
        conflux_oracles()
    elif fail_code == 2:
        templar_boss()


def templar_arena(oracle_position):
    """The purpose of this function is to return a visual representation of the
       oracle's location on the arena.
       oracle_position - multiple lines of code that form the appearance of
       an arena."""
    if oracle_position == 0:
        print("          _______|===|_______")
        print("         /   \\           /   \\")
        print("        /     \\  [   ]  /     \\")
        print("       /       \\       /       \\")
        print("       |  [  ]  \\     /  [  ]  |")
        print("       |         \\   /         |")
        print("       |----------[ ]----------|")
        print("       |         /   \\         |")
        print("       |  [  ]  /     \\  [  ]  |")
        print("       \\       /       \\       /")
        print("        \\     /  [   ]  \\     /")
        print("         \\___/   [   ]   \\___/")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 1:
        print("          _______|===|_______")
        print("         /   \\           /   \\")
        print("        /     \\  [   ]  /     \\")
        print("       /       \\       /       \\")
        print("       |  [  ]  \\     /  [  ]  |")
        print("       |         \\   /         |")
        print("       |----------[ ]----------|")
        print("       |         /   \\         |")
        print("       |  [  ]  /     \\  [  ]  |")
        print("       \\       /       \\       /")
        print("        \\     /  [(O)]  \\     /")
        print("         \\___/  [DING!]  \\___/")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 2:
        print("          _______|===|_______")
        print("         /   \\           /   \\")
        print("        /     \\  [   ]  /     \\")
        print("       /       \\       /       \\")
        print("       |  [  ]  \\     /  [  ]  |")
        print("       |         \\   /         |")
        print("       |----------[ ]----------|")
        print("       |         /   \\         |")
        print("       | [DING!]/     \\  [  ]  |")
        print("       \\       /       \\       /")
        print("        \\     /  [   ]  \\     /")
        print("         \\___/   [   ]   \\___/")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 3:
        print("          _______|===|_______")
        print("         /   \\           /   \\")
        print("        /     \\  [   ]  /     \\")
        print("       /       \\       /       \\")
        print("       | [DING!]\\     /  [  ]  |")
        print("       |         \\   /         |")
        print("       |----------[ ]----------|")
        print("       |         /   \\         |")
        print("       |  [  ]  /     \\  [  ]  |")
        print("       \\       /       \\       /")
        print("        \\     /  [   ]  \\     /")
        print("         \\___/   [   ]   \\___/")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 4:
        print("          _______|===|_______")
        print("         /   \\           /   \\")
        print("        /     \\ [DING!] /     \\")
        print("       /       \\       /       \\")
        print("       |  [  ]  \\     /  [  ]  |")
        print("       |         \\   /         |")
        print("       |----------[ ]----------|")
        print("       |         /   \\         |")
        print("       |  [  ]  /     \\  [  ]  |")
        print("       \\       /       \\       /")
        print("        \\     /  [   ]  \\     /")
        print("         \\___/   [   ]   \\___/")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 5:
        print("          _______|===|_______")
        print("         /   \\           /   \\")
        print("        /     \\  [   ]  /     \\")
        print("       /       \\       /       \\")
        print("       |  [  ]  \\     /[DING!] |")
        print("       |         \\   /         |")
        print("       |----------[ ]----------|")
        print("       |         /   \\         |")
        print("       |  [  ]  /     \\  [  ]  |")
        print("       \\       /       \\       /")
        print("        \\     /  [   ]  \\     /")
        print("         \\___/   [   ]   \\___/")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 6:
        print("          _______|===|_______")
        print("         /   \\           /   \\")
        print("        /     \\  [   ]  /     \\")
        print("       /       \\       /       \\")
        print("       |  [  ]  \\     /  [  ]  |")
        print("       |         \\   /         |")
        print("       |----------[ ]----------|")
        print("       |         /   \\         |")
        print("       |  [  ]  /     \\[DING!] |")
        print("       \\       /       \\       /")
        print("        \\     /  [   ]  \\     /")
        print("         \\___/   [   ]   \\___/")
        print("          |       YOU       |")
        print("          |=================|")
    # TEMPLAR ORACLES ---------------------------------------------------------
    elif oracle_position == 7:
        print("          _______|===|_______")
        print("         /                   \\")
        print("        /        [   ]        \\")
        print("       /                       \\")
        print("       |  [  ]           [  ]  |")
        print("       |         <<o>>         |")
        print("       |          <V>          |")
        print("       |           v           |")
        print("       |  [  ]           [  ]  |")
        print("       \\                       /")
        print("        \\        [   ]        /")
        print("         \\       [   ]       /")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 8:
        print("          _______|===|_______")
        print("         /                   \\")
        print("        /        [   ]        \\")
        print("       /                       \\")
        print("       |  [  ]           [  ]  |")
        print("       |         <<o>>         |")
        print("       |          <V>          |")
        print("       |           v           |")
        print("       |  [  ]           [  ]  |")
        print("       \\                       /")
        print("        \\        [(O)]        /")
        print("         \\      [DING!]      /")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 9:
        print("          _______|===|_______")
        print("         /                   \\")
        print("        /        [   ]        \\")
        print("       /                       \\")
        print("       |  [  ]           [  ]  |")
        print("       |         <<o>>         |")
        print("       |          <V>          |")
        print("       |           v           |")
        print("       | [DING!]         [  ]  |")
        print("       \\                       /")
        print("        \\        [   ]        /")
        print("         \\       [   ]       /")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 10:
        print("          _______|===|_______")
        print("         /                   \\")
        print("        /        [   ]        \\")
        print("       /                       \\")
        print("       | [DING!]         [  ]  |")
        print("       |         <<o>>         |")
        print("       |          <V>          |")
        print("       |           v           |")
        print("       |  [  ]           [  ]  |")
        print("       \\                       /")
        print("        \\        [   ]        /")
        print("         \\       [   ]       /")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 11:
        print("          _______|===|_______")
        print("         /                   \\")
        print("        /       [DING!]       \\")
        print("       /                       \\")
        print("       |  [  ]           [  ]  |")
        print("       |         <<o>>         |")
        print("       |          <V>          |")
        print("       |           v           |")
        print("       |  [  ]           [  ]  |")
        print("       \\                       /")
        print("        \\        [   ]        /")
        print("         \\       [   ]       /")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 12:
        print("          _______|===|_______")
        print("         /                   \\")
        print("        /        [   ]        \\")
        print("       /                       \\")
        print("       |  [  ]         [DING!] |")
        print("       |         <<o>>         |")
        print("       |          <V>          |")
        print("       |           v           |")
        print("       |  [  ]           [  ]  |")
        print("       \\                       /")
        print("        \\        [   ]        /")
        print("         \\       [   ]       /")
        print("          |       YOU       |")
        print("          |=================|")
    elif oracle_position == 13:
        print("          _______|===|_______")
        print("         /                   \\")
        print("        /        [   ]        \\")
        print("       /                       \\")
        print("       |  [  ]           [  ]  |")
        print("       |         <<o>>         |")
        print("       |          <V>          |")
        print("       |           v           |")
        print("       |  [  ]        [DING!]  |")
        print("       \\                       /")
        print("        \\        [   ]        /")
        print("         \\       [   ]       /")
        print("          |       YOU       |")
        print("          |=================|")


def clear():
    """The purpose of this function is to clear the console of any outputs
       prior to the moment it is called."""
    command = 0
    if os.name in ('nt', 'cls'):
        command = 'cls'
    os.system(command)
    # https://www.delftstack.com/howto/python/python-clear-console/
    # I got this function from this website as a way to clear the screen
    # at certain points of the program so the console won't end up cluttered.


# Calls to Main ---------------------------------------------------------------
if __name__ == "__main__":
    main()
