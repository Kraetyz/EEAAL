label personality_test:
    image grasshopper = "adam_grasshopper.jpg"
    show Adam_Front at left, normal_size
    show grasshopper at right
    
    $winner = False

    "Hi"
    menu:
        "How are you feeling today?"
        
        "Adventurous":
            $Adam.SetPersonality(0)
        "Bashful":
            $Adam.SetPersonality(2)
        "Confident":
            $Adam.SetPersonality(1)
     
    "Let's talk about the Israel-Gaza conflict!"

    if Adam.AdventurousPersonality():
        Adam.c "From the river to the sea! Palestine will be free!"
    else:
        Adam.c "There's probably something better we can do with our time."

    menu:
        "What if we played some sports?"
        
        "I guess we can.":
            if Adam.BashfulPersonality():
                jump loser
            else:
                jump winner
        
        "I'd rather not.":
            jump finished
        
        "Anything but golf!" if Adam.ConfidentPersonality():
            "What about basketball?"
            Adam.c "Let's B some Balls, brother!"
            jump winner
            
     
     
    label winner:
        Adam.c "Wow, ez game."
        $winner = True
        jump finished
    label loser:
        Adam.c "I've never been more humiliated."
        "Don't commit sudoku, please. Even if you are a loser."
        Adam.c "No promises."
     
    label finished:
        "Wow, we had a lot of fun, didn't we?"
        
        if Adam.AdventurousPersonality():
            Adam.c "Fuckin, no?"
        elif Adam.ConfidentPersonality():
            if winner:
                Adam.c "Yeah, because I won."
            else:
                Adam.c "I always have fun!"
        elif Adam.BashfulPersonality():
            Adam.c "Uhm, I guess."
        "And, scene."
    jump dayloop_done