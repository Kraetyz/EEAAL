# Create a well defined name and object for the character
#charname is the code name used for dialogue
#define charname = Character("Character Name", color="#name_color", what_color="#text_color")

# Character specific variables go here

#define python_variable = None

# End Character specific vars

# Custom images
#I am including here the example code for making a character's eyes blink
#image testguy_blink:
#    "images/testguy/eyes_open.png"
#    choice:
#        4.5
#    choice:
#        3.5
#    choice:
#        1.5
#    "images/testguy/eyes_closed.png"
#    pause 0.1
#    repeat

#This is an example of how to define a customizable body part
#Must also define a charname_fitchoice variable near the top of the document to hold the body part name
#image testguy_outfit:
#    "images/testguy/[charname_fitchoice]_body.png"

# End Custom images

# The layeredimage definition at the bottom
#Place your layeredimage of the character here
#See technical doc for an explanation

# End layeredimage definition