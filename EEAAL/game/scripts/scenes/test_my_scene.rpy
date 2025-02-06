label test_my_scene:
    $ TimeOfDay = Calendar.GetTimeOfDay()
    menu:
        "Place a label to your scene here!"
        
        "Back to day loop":
            jump dayloop
            
        "Personality test":
            jump personality_test
        
        "Adam's test scenes":
            jump adams_test_scenes #These can be found in adam_nonsense.rpy
            
        "Librarian Scene 1":
            jump librarian_1
        
        "Pen Pal scene Day 1":
            if TimeOfDay == 0:
                jump PenPal1
            if TimeOfDay == 1:
                jump PenPal1B
            if TimeOfDay == 2:
                jump PenPal1C
            else:
                "Oh something is wrong."