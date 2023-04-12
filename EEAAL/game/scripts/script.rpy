﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("Narrator")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lake shore

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show adam grasshopper at left_to_right

    # These display lines of dialogue.

    narrator "Adam came here to sabotage the opening scene."

    show adam grasshopper at truecenter

    narrator "There's really nothing here."
    
    show adam grasshopper at zig_zag_vibrate
    
    narrator "Adam is getting upset at your presence."
    
    show adam grasshopper at whacky_zoom
    
    narrator "Leave."

    # This ends the game.

    return
