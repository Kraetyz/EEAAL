label PenPal2:
    
    define Pen = Character("Pen")
    show Adam_Front at left, normal_size
    
    if pen_points <= -1:
        Pen "Hey from back home! Were you busy yesterday?"
        
        menu:
            "Yes, sorry I meant to get back to you.":
                Pen "Don't worry about it!"
                $pen_points = pen_points+1
            "Getting unpacked was a lot of work and I’m still pretty drained.":
                Pen "Oh sorry, chat later!"
                jump room_d2
            "Dismiss.":
                $pen_points = pen_points-1
                jump room_d2
    
    
    Pen "Just letting you know your garden is still alive! Lol!"

    menu:
        "Thank goodness, I was afraid they all would wither immediately overnight.":
            "..."
        "It takes a long time for plants to show signs of suffering...":
            "..."
        "Dismiss":
            $soc = soc-1
            Adam.c "I'll respond to this later." 
            jump room_d2
        
        "I'd rather you wouldn't joke about that. Those plants mean a lot to me." if Adam.BashfulPersonality():
            Pen "Sorry sorry just being stupid in the morning"
            $pen_points = pen_points-2
        "Show that garden you're the new boss!!" if Adam.ConfidentPersonality():
            Pen "Yeah you got it, I'm the boss!!!!! lol"
            $pen_points = pen_points+2
        "If you keep going at this rate you'll learn all about gardening yourself!" if Adam.AdventurousPersonality():
            Pen "Least I know which nerd I need to pick the brain of along the wayyyy"
            $pen_points = pen_points
    
    Pen "Okay okay I won't keep you any more this morning, I have to go anyway, talk later"
    jump room_d2
 
 
    label PenPal2B:    
        if pen_points <= -3:
            Pen "Hey you know you can say if I'm bugging you right?"
            
            menu:
                "You haven't stopped messaging since I got here, that's all.":
                    Pen "So tell me next time"
                    Pen "I'm not used to this, I don't know what's too much, you have to tell me that"
                    Adam.c "Okay. I'll try to do that now. Thanks for listening."
                    $pen_points = pen_points-1
                    jump room_d2
                    
                "You're not bothering me, there's just a lot on my mind.":
                    Pen "Okay sure but you can't ghost me suddenly"
                    Adam.c "I know, sorry. I'll do better about responding."
                    Pen "its cool."
                    Pen "On lighterrr topics"
                    $pen_points = pen_points+1
                    
                "Dismiss.":
                    $pen_points = pen_points-2
                    jump room_d2
        
        Pen "I have an important question for you lol"
        Pen "Is there anyone cute around??"
        
        menu:
            "Yes, it's...":
                menu:
                    "The guy in my mirror.":
                        Pen "Lmao damn right!!"
                    "The sexy librarian.":
                        $librarian_points = librarian_points+2
                        Pen "there is NOT an actual sexy librarian get out of here LMAO" 
            "No one's really my type, that's for sure.":
                Pen "Okay what about MY type"
                menu:
                    "Definitely.":
                        $pen_points = pen_points
                    "I mean, I'm here.":
                        $pen_points = pen_points+1
                        Pen "Okay I mean yeah thats true"
            "You're asking the wrong person for something like that.":
                Pen "Okay then does anyone look like they might cut it in a Wollyhood movie"
                
                menu:
                    "Me.":
                        Pen "Yeah yeah you're hot shit wahtever idiot"
                    "Librarian.":
                        $librarian_points = librarian_points+2
                    
            "Dismiss":
                $pen_points = pen_points-2
                $soc = soc-1
                jump room_d2
                  
        
        Pen "You almost make it sound worth it for me to come visit. +1 to the attractive people in town right? Lol!"
                      
        jump room_d2
        
        
        label room_d2: #Since the ONLY time you can contact Pen Pal is from your room, and by default you RETURN to your room, dismissing them means you just go back to general menu.
            $timestr = Calendar.GetTimeOfDayStr()
            $daystr = Calendar.GetDate() 

            "You are in your room. You contemplate for a while. Currently, your social score is [soc]. Your relationship with Pen is [pen_points]."
            "It is currently Day [daystr] and the time is [timestr]." 
            
            menu:
                "Let's sleep for a bit.":
                    jump dayloop_done 
            
        