# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")

define tg = testguy

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lakeshore

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show adam_grasshopper at left_to_right

    # These display lines of dialogue.

    n "Adam came here to sabotage the opening scene."

    show adam_grasshopper at truecenter

    n "There's really nothing here."
    
    show adam_grasshopper at zig_zag_vibrate
    
    n "Adam is getting upset at your presence."
    
    show adam_grasshopper at whacky_zoom
    
    n "You have been warned."
    
    hide adam_grasshopper with dissolve
    
    show testguy white
    
    tg "Pee pee poo poo."
    
    show testguy red frown
    
    tg "My penis is only [testguy_inches] inches long."
    
    pause
    
    show adam_grasshopper at left with dissolve
    
    show testguy red smile
    
    $ testguy_inches = 10
    
    tg "Wow! It grew to [testguy_inches] inches when I saw Adam as a grasshopper!"

    # This ends the game.

    return
