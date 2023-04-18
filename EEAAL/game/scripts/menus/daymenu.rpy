define that_damn_music = True

label daymenu:
    scene dfmap with dissolve
    show testguy at right
    jump daymenu_inner

label daymenu_inner:
    if that_damn_music:
        play music "audio/music/funky-piano.wav" if_changed
    else:
        stop music
    menu: 
        "A recurring menu."

        "Test scene list":
            stop music
            jump test_my_scene
        
        "Go to my room.":
            tg "Gotta change my fit!"
            python:
                if testguy_fitchoice == "white":
                    testguy_fitchoice = "red"
                else:
                    testguy_fitchoice = "white"
            jump daymenu_inner
            
        "Visit the store.":
            $ testguy_position = move_to_right
            show testguy frown
            tg "No money."
            jump daymenu_inner
        
        "Turn that damn music off":
            "Lame."
            $ that_damn_music = False
            jump daymenu_inner
        
        "Explore the world.":
            "uwu whats this?"
            stop music
            jump testscene
            
        "Masturbate." if testguy_inches > 10:
            jump NSFW