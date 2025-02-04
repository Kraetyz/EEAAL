label PenPal1:
    
    define Pen = Character("Pen")
    show Adam_Front at left, normal_size
    
    Pen "You know, it’s crazy because sending you this message."
    "It’s like, I still think if I say ‘hey let’s hang out’ you can just come down to my place and do that. ??? I have not accepted it yet lol"
    menu:
        "Yeah. Same.":
            "..."
        "You'll get used to it.":
            "..."
        "Dismiss":
            Adam.c "I'll respond to this later." 
        
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
    
    jump dayloop_done