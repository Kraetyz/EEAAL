# Create a well defined name and object for the character

define testguy = Character("Test Guy", color="#FCFC00", what_color="#0092AD")

# Character specific variables go here

define testguy_inches = 3
define testguy_fitchoice = "white"

# End Character specific vars

# Custom images

image testguy_blink:
    "images/testguy/eyes_open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/testguy/eyes_closed.png"
    pause 0.1
    repeat
    
image testguy_outfit:
    "images/testguy/[testguy_fitchoice]_body.png"

# End Custom images

# The layeredimage definition at the bottom

layeredimage testguy:
    group outfit:
        attribute playerchoice default:
            "testguy_outfit"
        attribute white:
            "images/testguy/white_body.png"
        attribute red:
            "images/testguy/red_body.png"
            
    group head:
        attribute regular default:
            "images/testguy/head.png"

    group eyes:
        attribute eyes_open default:
            "testguy_blink"
        attribute eyes_ahegao:
            "images/testguy/eyes_ahegao.png"

    group mouth:
        attribute smile default:
            "images/testguy/smile.png"
        attribute frown:
            "images/testguy/frown.png"
        attribute mouth_ahegao:
            "images/testguy/mouth_ahegao.png"

# End layeredimage definition