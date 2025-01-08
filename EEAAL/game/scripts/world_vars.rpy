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
    
    #Character creation
    # This should probably, eventually, live somewhere else, but I don't have graphics or whatever yet
    # So when we figure out how the EDACharacter class should look, and we create character scripts for each of them
    # This line below will probably belong in one of those scripts
    Adam = Adam(Character("Adam", color="#F5DA56", what_color="#7D5F7A"))
    
    #Calendar!!
    Calendar = Calendar()
    
    #Facts about the world
    town_name = ""





    #Event history testing
    globalEvents = EventHistory()
    
    globalEvents.AddEvent("FirstEvent", ["Adam", "Narrator"], [("Avocado", True), ("Penis", "Large"), ("Apples", 6)])
    globalEvents.AddEvent("ThirdImpact", ["Shinji", "Rei", "Asuka"], [("Humans", "They're all dead!", ("Shinji's dad", "Still a piece of shit"))])