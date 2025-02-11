label PenPal2:
    
    show Adam_Front at left, normal_size
    
    if pen_points <= -1:
        Pen.c "Hey from back home! Were you busy yesterday?"
        
        menu:
            "Yes, sorry I meant to get back to you.":
                Pen.c "Don't worry about it!"
                $Pen.Plus("points", 1)
            "Getting unpacked was a lot of work and I’m still pretty drained.":
                Pen.c "Oh sorry, chat later!"
                jump room_d2
            "Dismiss.":
                $Pen.Minus("points", 1)
                jump room_d2
    
    
    Pen.c "Just letting you know your garden is still alive! Lol!"

    menu:
        "Thank goodness, I was afraid they all would wither immediately overnight.":
            "..."
        "It takes a long time for plants to show signs of suffering...":
            "..."
        "Dismiss":
            $Adam.Minus("social", 1)
            Adam.c "I'll respond to this later." 
            jump room_d2
        
        "I'd rather you wouldn't joke about that. Those plants mean a lot to me." if Adam.BashfulPersonality():
            Pen.c "Sorry sorry just being stupid in the morning"
            $Pen.Minus("points", 2)
        "Show that garden you're the new boss!!" if Adam.ConfidentPersonality():
            Pen.c "Yeah you got it, I'm the boss!!!!! lol"
            $Pen.Plus("points", 2)
        "If you keep going at this rate you'll learn all about gardening yourself!" if Adam.AdventurousPersonality():
            Pen.c "Least I know which nerd I need to pick the brain of along the wayyyy"
    
    Pen.c "Okay okay I won't keep you any more this morning, I have to go anyway, talk later"
    jump room_d2
 
 
    label PenPal2B:    
        if Pen.Get("points") <= -3:
            Pen.c "Hey you know you can say if I'm bugging you right?"
            
            menu:
                "You haven't stopped messaging since I got here, that's all.":
                    Pen.c "So tell me next time"
                    Pen.c "I'm not used to this, I don't know what's too much, you have to tell me that"
                    Adam.c "Okay. I'll try to do that now. Thanks for listening."
                    $Pen.Minus("points", 1)
                    jump room_d2
                    
                "You're not bothering me, there's just a lot on my mind.":
                    Pen.c "Okay sure but you can't ghost me suddenly"
                    Adam.c "I know, sorry. I'll do better about responding."
                    Pen.c "its cool."
                    Pen.c "On lighterrr topics"
                    $Pen.Plus("points", 1)
                    
                "Dismiss.":
                    $Pen.Minus("points", 2)
                    jump room_d2
        
        Pen.c "I have an important question for you lol"
        Pen.c "Is there anyone cute around??"
        
        menu:
            "Yes, it's...":
                menu:
                    "The guy in my mirror.":
                        Pen.c "Lmao damn right!!"
                    "The sexy librarian.":
                        $Librarian.Plus("points", 2)
                        Pen.c "there is NOT an actual sexy librarian get out of here LMAO" 
            "No one's really my type, that's for sure.":
                Pen.c "Okay what about MY type"
                menu:
                    "Definitely.":
                        jump PenPal2B_postmenu
                    "I mean, I'm here.":
                        $Pen.Plus("points", 1)
                        Pen.c "Okay I mean yeah thats true"
            "You're asking the wrong person for something like that.":
                Pen.c "Okay then does anyone look like they might cut it in a Wollyhood movie"
                
                menu:
                    "Me.":
                        Pen.c "Yeah yeah you're hot shit wahtever idiot"
                    "Librarian.":
                        $Librarian.Plus("points", 2)
                    
            "Dismiss":
                $Librarian.Minus("points", 2)
                $Adam.Minus("social", 1)
                jump room_d2
                  
    label PenPal2B_postmenu:    
        Pen.c "You almost make it sound worth it for me to come visit. +1 to the attractive people in town right? Lol!"
        jump room_d2
        
        
        label room_d2: #Since the ONLY time you can contact Pen.c Pal is from your room, and by default you RETURN to your room, dismissing them means you just go back to general menu.
            $timestr = Calendar.GetTimeOfDayStr()
            $daystr = Calendar.GetDate() 

            "You are in your room. You contemplate for a while. Currently, your social score is [Adam.Get('social')]. Your relationship with Pen is [Pen.Get('points')]."
            "It is currently Day [daystr] and the time is [timestr]." 
            
            menu:
                "Let's sleep for a bit.":
                    jump dayloop_done
            
        