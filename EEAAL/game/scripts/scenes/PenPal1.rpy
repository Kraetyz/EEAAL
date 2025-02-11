label PenPal1:
    
    show Adam_Front at left, normal_size
    
    Pen.c "You know, it’s crazy because sending you this message."
    Pen.c "It’s like, I still think if I say ‘hey let’s hang out’ you can just come down to my place and do that. ??? I have not accepted it yet lol"
    menu:
        "Yeah. Same.":
            "..."
        "You'll get used to it.":
            "..."
        "Dismiss":
            $Adam.Minus("social", 1)
            Adam.c "I'll respond to this later." 
            jump room_d1
        
        "Don’t say that, you’re going to make me regret this decision…" if Adam.BashfulPersonality():
            Pen.c "I diddd try to talk you out of it."
            $Pen.Minus("points", 2)
        "Once I get this town figured out, I’ll fly you out and we CAN hang out." if Adam.ConfidentPersonality():
            Pen.c "So confident already! That’s good at least."
            $Pen.Plus("points", 2)
        "No no we can still do that. Come find me." if Adam.AdventurousPersonality():
            Pen.c "Nice try. :P I wish."
    
    Pen.c "Everyone is going to miss you a ton, but they’re also excited for you. Will you send lots of pics?"
    
    menu:
        "Of course.":
            Pen.c "GOOD!!!! Tag us on your socials OK??"
        "I'll try. I might be busy.":
            Pen.c "Of course of course yeah. Just once in a while is fine, so we know you’re not dead!"
        
    Pen.c "Hey, so, I wanna be positive and all, but without me around…"
    Pen.c "Just make sure you don’t get back into you-know-what again. Got it?"
    Adam.c "Yeah, I got it."
    Pen.c "Great!!! Thanks for chatting. I know you gotta big day ahead so. Good luck!" 
    
    jump room_d1
    
    label PenPal1B:
        Pen.c "I just checked the weather over there, fuckk man it’s HOT and DRY I would nottt survive"
        Pen.c "How are you gonna grow anything out there? Maybe it’s time for a new hobby"
        
        menu:
            "I know I can do it, I’ve always been the greenest thumb around.":
                jump PenPal1B_postmenu
            "It’s just a matter of knowing what plants grow in this environment.":
                $Pen.Plus("points", 1)
            "Dismiss":
                $Pen.Minus("points", 1)
                $Adam.Minus("social", 1)
                jump room_d1
            "I don’t know yet, but it’ll be fun to explore the local ecology!" if Adam.AdventurousPersonality():
                jump PenPal1B_postmenu
            "I still want to try. This will be my first test of character."  if Adam.BashfulPersonality():
                $Pen.Minus("points", 2)
                Pen.c "Okay deep lol" 
            "I’m gonna make the environment my bitch >:)" if Adam.ConfidentPersonality():
                $Pen.Plus("points", 2)
                Pen.c "I am NOT convinced it works like that lol"
                Adam.c "Just you watch me."
            
    label PenPal1B_postmenu:    
        Pen.c "Nothing ever gets you down!! You gotta show me your progress reportsss"
        Pen.c "I’ll keep your garden back home alive"
            
        menu:
            "Just ‘alive’?":
                Pen.c "I mean, I’ll try to do better than that, but I’m not as good as you are at this!"
            "I really appreciate it.":
                Pen.c "It’s the least I can do, right?"
            
        Pen.c "It’s like I’ll be keeping some part of you alive back home, here. So I’ll try my hardest."
        Adam.c "Don’t worry, you can do it."
        Pen.c "I appreciate the support. Talk later!"
            
        jump room_d1
        
    label PenPal1C: #tired I'm done this for now 
    
        Pen.c "My folks made YOUR FAVOURITE for dinner AND YOU CAN’T SHARE ANY. Who wishes [Adam.their] was back home now??"
        Pen.c "But seriously how was day 1?"
        
        menu:
            "Dismiss":
                $Pen.Minus("points", 1)
                $Adam.Minus("social", 1)
                jump room_d1
            "Eventful, but I think it was good. I got to meet some of the locals.":
                $Pen.Plus("points", 1)
                Pen.c "Trying to fit in already, huh? That’s just like you"
                Pen.c "It would’ve taken me months tbh"
                Adam.c "It’s not that hard if you give people a chance."
            "The people here are a little strange, that's for sure.":
                Pen.c "Or are YOU strange? You’re not from there and showed up suddenly"
                Adam.c "I guess I didn't think of it like that."
            "It could have gone better. Definitely missing home.":
                $Pen.Minus("points", 1) 
                Pen.c "I’m not the person to ask bc I will just say to come back lol"
                Pen.c "Is that how you're really feeling though?"
                Adam.c "Not sure. It’s probably too early to be sure."
            "It has such a rich and unique culture and I'm looking forward to seeing more!" if Adam.AdventurousPersonality():
                jump PenPal1C_postmenu
            "It certainly made me think about the decisions that I've made to get here."  if Adam.BashfulPersonality():
                $Pen.Minus("points", 2)
            "I've asserted my dominance just like I promised! Soon everyone in town will be eating out of my hand." if Adam.ConfidentPersonality():
                $Pen.Plus("points", 2)

    label PenPal1C_postmenu:
        Adam.c "I guess we’ll see what happens from here. It’ll take some getting used to."
        Pen.c "Don’t sweat it!! If things don’t gel you can always come back home."
        Adam.c "Thanks, man."
        jump room_d1 
    
    label room_d1: #Since the ONLY time you can contact Pen.c Pal is from your room, and by default you RETURN to your room, dismissing them means you just go back to general menu.
        $timestr = Calendar.GetTimeOfDayStr()
        $daystr = Calendar.GetDate() 

        "You are in your room. You contemplate for a while. Currently, your social score is [Adam.Get('social')]. Your relationship with Pen is [Pen.Get('points')]."
        "It is currently Day [daystr] and the time is [timestr]." 
        
        menu:
            "Let's sleep for a bit.":
                jump dayloop_done 
            
        