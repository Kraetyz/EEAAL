init python:
    # A list of pronouns
    theythem = Pronouns()
    hehim = Pronouns("He/Him", "He", "Him", "His", "His", "Himself")
    sheher = Pronouns("She/Her", "She", "Her", "Her", "Hers", "Herself")
    zehir = Pronouns("Ze/Hir", "Ze", "Hir", "Hir", "Hirs", "Hirzelf")
    xexem = Pronouns("Xe/Xem", "Xe", "Xem", "Xir", "Xirs", "Xirself")
    
    pronoun_list = { 
        "They": theythem,
        "He": hehim,
        "She": sheher,
        "Ze": zehir,
        "Xe": xexem
    }
    
    #Character creation
    Adam = Adam(Character("Adam", color="#F5DA56", what_color="#7D5F7A"))