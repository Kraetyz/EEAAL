# The script of the game goes in this file.
# The game starts here.

label start:
    jump startscene

label daymenu:
    scene dfmap with dissolve
    show testguy at right
    
    menu:
        "A recurring menu."
        
        "Go to my room.":
            tg "Gotta change my fit!"
            python:
                if testguy_fitchoice == "white":
                    testguy_fitchoice = "red"
                else:
                    testguy_fitchoice = "white"
            jump daymenu
            
        "Visit the store.":
            $ testguy_position = move_to_right
            show testguy frown
            tg "No money."
            jump daymenu
        
        "Explore the world.":
            "uwu whats this?"
            jump testscene
            
        "Masturbate." if testguy_inches > 10:
            jump NSFW