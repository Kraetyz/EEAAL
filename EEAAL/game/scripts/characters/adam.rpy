# Create a well defined name and object for the character

# Character specific variables go here

# These actually live in the Adam class, this code is temporary

# End Character specific vars

# Custom images

image adam_blink:
    "images/adam/Adam_Eyes_Open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/adam/Adam_Eyes_Closed.png"
    pause 0.1
    repeat
    
image adam_outfit:
    "images/adam/[Adam.outfit].png"

# End Custom images

# The layeredimage definition at the bottom

layeredimage Adam_Front:
    group body:
        attribute regular default:
            "images/adam/Adam_Body.png"
            
    group head:
        attribute regular default:
            "images/adam/Adam_Head.png"

    group outfit:
        attribute playerchoice default:
            "adam_outfit"
        #Can add more attributes here for forced outfits?

    group eyes:
        attribute regular default:
            "adam_blink"

    group mouth:
        attribute regular default:
            "images/adam/Adam_Mouth.png"

# End layeredimage definition