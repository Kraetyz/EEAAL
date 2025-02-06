label PenPal1:
    
    define Pen = Character("Pen")
    show Adam_Front at left, normal_size
    
    Pen "You know, it’s crazy because sending you this message."
    Pen "It’s like, I still think if I say ‘hey let’s hang out’ you can just come down to my place and do that. ??? I have not accepted it yet lol"
    menu:
        "Yeah. Same.":
            "..."
        "You'll get used to it.":
            "..."
        "Dismiss":
            $soc = soc-1
            Adam.c "I'll respond to this later." 
            jump room_d1
        
        "Don’t say that, you’re going to make me regret this decision…" if Adam.BashfulPersonality():
            Pen "I diddd try to talk you out of it."
            $pen_points = pen_points-2
        "Once I get this town figured out, I’ll fly you out and we CAN hang out." if Adam.ConfidentPersonality():
            Pen "So confident already! That’s good at least."
            $pen_points = pen_points+2
        "No no we can still do that. Come find me." if Adam.AdventurousPersonality():
            Pen "Nice try. :P I wish."
            $pen_points = pen_points
    
    Pen "Everyone is going to miss you a ton, but they’re also excited for you. Will you send lots of pics?"
    
    menu:
        "Of course.":
            Pen "GOOD!!!! Tag us on your socials OK??"
        "I'll try. I might be busy.":
            Pen "Of course of course yeah. Just once in a while is fine, so we know you’re not dead!"
        
    Pen "Hey, so, I wanna be positive and all, but without me around…"
    Pen "Just make sure you don’t get back into you-know-what again. Got it?"
    Adam.c "Yeah, I got it."
    Pen "Great!!! Thanks for chatting. I know you gotta big day ahead so. Good luck!" 
    
    jump room_d1
    
    label PenPal1B:
        Pen "I just checked the weather over there, fuckk man it’s HOT and DRY I would nottt survive"
        Pen "How are you gonna grow anything out there? Maybe it’s time for a new hobby"
        
        menu:
            "I know I can do it, I’ve always been the greenest thumb around.":
                $pen_points = pen_points 
            "It’s just a matter of knowing what plants grow in this environment.":
                $pen_ponts = pen_points+1
            "Dismiss":
                $pen_points = pen_points-1
                $soc = soc-1
            "I don’t know yet, but it’ll be fun to explore the local ecology!" if Adam.AdventurousPersonality():
                $pen_points = pen_points 
            "I still want to try. This will be my first test of character."  if Adam.BashfulPersonality():
                $pen_points = pen_points-2
            "I’m gonna make the environment my bitch >:)" if Adam.ConfidentPersonality():
                $pen_points = pen_points+2
            
        
        Pen "Nothing ever gets you down!! You gotta show me your progress reportsss"
        Pen "I’ll keep your garden back home alive"
            
        menu:
            "Just ‘alive’?":
                Pen "I mean, I’ll try to do better than that, but I’m not as good as you are at this!"
            "I really appreciate it.":
                Pen "It’s the least I can do, right?"
            
        Pen "It’s like I’ll be keeping some part of you alive back home, here. So I’ll try my hardest."
        Adam.c "Don’t worry, you can do it."
        Pen "I appreciate the support. Talk later!"
            
        jump room_d1
        
        label PenPal1C: #tired I'm done this for now 
            "Woah. Carm didn't put anything in here yet."
            jump room_d1 
        
        label room_d1: #Since the ONLY time you can contact Pen Pal is from your room, and by default you RETURN to your room, dismissing them means you just go back to general menu.
            $timestr = Calendar.GetTimeOfDayStr()
            $daystr = Calendar.GetDate() 

            "You are in your room. It sure is a room."
            "It is currently Day [daystr] and the time is [timestr]." 
            
            menu:
                "Let's sleep for a bit.":
                    jump dayloop_done 
            
        