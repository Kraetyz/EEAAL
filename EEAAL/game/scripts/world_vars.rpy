init python:
    # A list of pronouns
    theythem = Pronouns()
    hehim = Pronouns("He/Him", "He", "Him", "His", "His", "Himself", "'s", "'s")
    sheher = Pronouns("She/Her", "She", "Her", "Her", "Hers", "Herself", "'s", "'s")
    zehir = Pronouns("Ze/Hir", "Ze", "Hir", "Hir", "Hirs", "Hirzelf", "'s", "'s")
    xexem = Pronouns("Xe/Xem", "Xe", "Xem", "Xir", "Xirs", "Xirself", "'s", "'s")
    
    pronoun_list = { 
        "They": theythem,
        "He": hehim,
        "She": sheher,
        "Ze": zehir,
        "Xe": xexem
    }
    
    #Calendar!!
    Calendar = Calendar()
    
    #Facts about the world
    town_name = "TOWN NAME"



    # Create Characters
    # Each character is created here by calling their associated creation method, which is defined in their EDAC_CharacterName script
    TestGuy = CreateTestGuy()
    Adam = CreateAdam()
    Librarian = CreateLibrarian()
    Pen = CreatePenpal()

    #Event history testing
    globalEvents = EventHistory()
    
    globalEvents.AddEvent("FirstEvent", ["Adam", "Narrator"], [("Avocado", True), ("Penis", "Large"), ("Apples", 6)])
    globalEvents.AddEvent("ThirdImpact", ["Shinji", "Rei", "Asuka"], [("Humans", "They're all dead!", ("Shinji's dad", "Still a piece of shit"))])