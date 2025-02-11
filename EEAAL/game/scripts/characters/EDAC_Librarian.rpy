init python:
    def CreateLibrarian():
        lib = EDACharacter("The Librarian")
        lib.c = Character("The Librarian")

        lib.SetPronouns(pronoun_list["She"])
        
        lib.Add("points", 0)
        
        return lib