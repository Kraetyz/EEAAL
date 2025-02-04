# The day loop should get called at the start of every day.
# It lets the player decide what to do during their day.
# Every scene chain should eventually lead back to this.

image town_name_image = ParameterizedText(xalign=0.5, yalign=0.1, size=+50)
image town_signpost = "images/signtest.png"

#TEST LOL
init python:
    Plants = 0

label dayloop:
    scene dfmap with dissolve
    show town_signpost at Position(xpos=0.1, ypos=0.75)
    show town_name_image "{font=fonts/PopulationZeroBB.otf}[town_name]{/font}" at Position(xpos=0.1, ypos=0.61)
    # Conditional logic goes here to display the correct time of day background
    
    $ TimeOfDay = Calendar.GetTimeOfDay()
    $ TimeOfDayStr = Calendar.GetTimeOfDayStr()
    $ Date = Calendar.GetDate()
    
    show Adam_Front at right, normal_size
    
    "It is [TimeOfDayStr] of day [Date] and Adam wants to waste [Adam.their] time."
    
label .dayloop_menu:
    play music "audio/music/Whimsical Creature.mp3" if_changed volume 0.2
    
    menu:
        "What should [Adam.they] do?"

        "Dev options":
            jump .dayloop_debug

        "Change outfit.":
            call dressing_room
        
        "Visit the store." if TimeOfDay != 3:
            "Sorry, not open yet. Bother the dev for more features."
            jump .dayloop_menu
        
        "Go to your garden.":
            $ Plants = Plants + 1
            "You have grown [Plants] plants. Wow! You go, champ!"
            if Plants > 4:
                "Get naked."
                call switch_adams_outfit(ret=True)
            jump dayloop_done
        
        "Go somewhere new!":
            "This is where we'll put a map, maybe. Let the player explore the world, meet people, idk."
            "Once the player is done with a set of scenes, they will write jump dayloop.dayloop_done and come back here."
            jump dayloop_done
        
        "Call a friend!":
            "If you get someone's phone number, maybe you can text them?"
            "Send them funny memes, tasteless nudes, complain. Who knows, maybe they're into that shit?"
            "Or maybe they will come meet up with you, protag-kun."
            jump dayloop_done
    
label .dayloop_debug:
    menu:
        "What are you doing?"

        "Test scene list":
            stop music
            jump test_my_scene

        "Pronoun select and town name":
            jump start_scene_pronoun_select
        
        "Back":
            jump .dayloop_menu
        
label dayloop_done:
    "The [TimeOfDayStr] is over."
    $ Calendar.NextTimeOfDay()
    "We return to the beginning."
    jump dayloop