# Create a well defined name and object for the character

define testguy = Character("Test Guy")

# Character specific variables go here

define testguy_inches = 5

# End Character specific vars

# Animated images for body parts

image testguyblink:
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

# End Animated images

# The layeredimage definition at the bottom

layeredimage testguy:
    group outfit:
        attribute white:
            "images/testguy/white_body.png"
        attribute red:
            "images/testguy/red_body.png"
            
    group head:
        attribute regular default:
            "images/testguy/head.png"

    group eyes:
        attribute open default:
            "testguyblink"

    group mouth:
        attribute smile default:
            "images/testguy/smile.png"
        attribute frown:
            "images/testguy/frown.png"

# End layeredimage definition