#variables and definitions
define n = Character("Narrator")


#Need to add vars for checking WHICH characters have given you plants. Probably a var stored IN a character that you get to read.
#Could be an integer at varying stages (0 = no seeds 1 = seeds 2 = growth etc)

#flower pics: everyone needs one defined in here at all stages from seed to growth. Maybe store flowers elsewhere??? Doing this first lol.
#All images for the flowers will be stored so that if the character var returns YES, that flower appears on your window sill.
#From there the progress of the flower must be tracked depending on your relationship score.
image lew_flower = im.FactorScale("images/flower-lew.png", 0.2)
image rissa_flower = im.FactorScale("images/flower-rissa.png", 0.2)
image spy_flower = im.FactorScale("images/flower-spy.png", 0.2)
image nick_flower = im.FactorScale("images/flower-nick.png", 0.2)
image carm_flower = im.FactorScale("images/flower-carm.png", 0.2)
image aries_flower = im.FactorScale("images/flower-aries.png", 0.2)
image laiat_flower = im.FactorScale("images/flower-laiat.png", 0.2)
image sam_flower = im.FactorScale("images/flower-sam.png", 0.2)

#scene starts
#This should be a location you can visit throughout the game. It's basically your relationship tracker.
#One thing that will be important is making sure that not only do all flowers appear, they appear in the order that you received them.
#For example: If the order you go is L(arissa) N(ick) S(py), they should appear on your window sill as L N S every time.
#This will mean finding a way to fix the position of a variable flower.
#Maybe make invisible 'position' containers which are then filled by the flowers? So Pos1 = L, Pos2 = N, Pos3 = S

#Need to create a function that will check for flowers and then fix their positions.

label window_sill:

    $hasPlants = 0

    scene windowbox with dissolve

    screen flowers_in_scene ():
        imagebutton:
            xpos 0
            ypos 0.2
            hovered Show("displayTextScreen", displayText = "This is some test stuff.")
            unhovered Hide("displayTextScreen")
            idle "images/flower-rissa.png"
            action NullAction

    if hasPlants > 0:
        show rissa_flower at left

    if hasPlants == 0:
        hide rissa_flower

    n "Welcome to your room! Let's look at these flowers."

    call screen flowers_in_scene

    n "Since we're testing things, let's make it so you can get peoples' flowers in here."

    menu add_remove_flowers:
        "Add Larissa's flower.":
            $hasPlants += 1

#        "Add Nick's flower.":
#            $hasplants += 1

#        "Add Sam's flower.":
#            $hasplants += 1

        "Remove Larissa's flower.":
            $hasPlants -= 1

    if hasPlants > 0:
        show rissa_flower at left

    if hasPlants == 0:
        hide rissa_flower

    n "Okay. Now let's do it again."

    jump add_remove_flowers


#This menu is to "inspect" the flowers you're growing. You should get a short blurb that sort of describes your relationship progress.
#    menu plant_check
