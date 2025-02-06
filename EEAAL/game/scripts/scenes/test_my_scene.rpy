label test_my_scene:
    $ TimeOfDay = Calendar.GetTimeOfDay()
    $ Date = Calendar.GetDate()
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
        
        "Pen Pal scenes":

            if Date == 0:
                if TimeOfDay == 0:
                    jump PenPal1
                if TimeOfDay == 1:
                    jump PenPal1B
                if TimeOfDay == 2:
                    jump PenPal1C
            if Date == 1:
                if TimeOfDay == 0:
                    jump PenPal2
                if TimeOfDay ==1:
                    jump PenPal2B
                if TimeOfDay == 2:
                    jump room_d2
            else:
                "Oh something is wrong."