define n = Character("Narrator")

label adams_test_scenes:
    menu:
        "Defined images in screen":
            call screen test_scene
        "Adam's intro scene.":
            jump oldstartscene
            
        "Scene selection with SceneInfo":
            jump sceneinfo_test
        
        "Event History testing":
            jump eventhistory_test

        "Secret ending":
            jump NSFW
            
        "Sound test":
            jump soundtest
        
        "Back":
            jump dayloop_done
            
label eventhistory_test:
    python:
        event_test = globalEvents.GetEventData("FirstEvent", "Penis")
        thirdimpactfolks = globalEvents.GetEventParticipants("ThirdImpact")
        was_adam_at_third_impact = globalEvents.EventHasParticipant("ThirdImpact", "Adam")

    if event_test == "Large":
        "Wow, that's huge!"

    "[thirdimpactfolks] had a bad day. Was Adam there? [was_adam_at_third_impact]"
    
    jump adams_test_scenes
   
label sceneinfo_test:
    python:
        oldstart = SceneInfo("Old Start Scene", "oldstartscene", 1, ["Grasshopper Adam"])
        testscene = SceneInfo("Dumb Test", "testscene", 2, ["Test Guy", "Grasshopper Adam"])
    
    menu:
        "Pick one of the scenes."
        
        "[oldstart.Name] featuring [oldstart.CharacterList]":
            $oldstart.StartScene()
            
        "[testscene.Name] featuring [testscene.CharacterList]":
            $testscene.StartScene()

label interactable_screen_experiment:
    show screen interacting_with_background 
    "You can click that sign."
    "It will take you to the save menu."
    "You can also just not and finish the scene."
    hide screen interacting_with_background
    jump daymenu

label oldstartscene:
    # Show a background.
    scene lakeshore

    # This shows a character sprite. 
    show adam_grasshopper at left_to_right

    # These display lines of dialogue.
    n "Adam came here to sabotage the opening scene."
    show adam_grasshopper at truecenter
    n "There's really nothing here."
    show adam_grasshopper at zig_zag_vibrate
    n "Adam is getting upset at your presence."
    show adam_grasshopper at whacky_zoom
    n "You have been warned."
    hide adam_grasshopper with dissolve
    pause 0.4
    jump daymenu
 
label testscene:
    scene lakeshore

    hide adam_grasshopper with dissolve
    
    $testguy_position = center
    show testguy
    
    TestGuy.c "Pee pee poo poo."
    TestGuy.c "I can talk more than this."
    
    show testguy frown
    
    TestGuy.c "My penis is only [TestGuy.Get('testguy_inches')] inches long."
    
    show testguy at move_to_right

    pause
    
    show adam_grasshopper at left with dissolve
    
    show testguy smile
    
    $ TestGuy.Set("testguy_inches", TestGuy.Get("testguy_inches") * 2)
    
    TestGuy.c "Wow! It grew to [TestGuy.Get('testguy_inches')] inches when I saw Adam as a grasshopper!"

    # This ends the game.
    
    jump dayloop_done
    
label NSFW:
    show testguy at center
    TestGuy.c "Penis size is important for men! That's why I'm happy that mine is a whole [TestGuy.Get('testguy_inches')] inches long!"
    TestGuy.c "When pee pee hard, this happens!"
    show testguy eyes_ahegao mouth_ahegao
    TestGuy.c "Hoooo weeee THIS IS FUN!"
    $ TestGuy.Set("testguy_inches", TestGuy.Get("testguy_inches") / 3)
    show testguy smile eyes_open
    TestGuy.c "After draining my balls, my penis has shrunk to a modest [TestGuy.Get('testguy_inches')] inches. That's okay, I still feel great."
    
    menu:
        "Should I keep up this grotesque mockery of life?"
        
        "Fuck it we ball":
            jump dayloop_done
        "An hero":
            return
            
label soundtest:
    play sound "audio/sfx/analog-alarm.wav"
    play soundalt1 "audio/sfx/explosion.mp3"
    play soundalt2 "audio/sfx/blam.mp3"
    TestGuy.c "That's very noisy."
    voice "audio/voice/built-then-burnt.mp3"
    "Let's try adding some voice."
    voice sustain
    "Wow he just keeps talking don't he?"
    voice sustain
    "This is from a song by A Silver Mt Zion btw."
    stop voice
    "Okay enough of that."
    jump dayloop_done