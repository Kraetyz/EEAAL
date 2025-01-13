define that_damn_music = True

label daymenu:
    scene dfmap with dissolve
    show town_signpost at Position(xpos=0.1, ypos=0.75)
    show town_name_image "{font=fonts/PopulationZeroBB.otf}[town_name]{/font}" at Position(xpos=0.1, ypos=0.61)
    #show text "[town_name]" at top
    show Adam_Front at right, normal_size
    jump daymenu_inner

label daymenu_inner:
    if that_damn_music:
        play music "audio/music/Whimsical Creature.mp3" if_changed volume 0.2
    else:
        stop music
    menu:
        "A recurring menu."

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
