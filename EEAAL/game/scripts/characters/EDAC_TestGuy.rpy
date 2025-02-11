init python:
    def CreateTestGuy():
        tg = EDACharacter("Test Guy")
        tg.c = Character("Test Guy", color="#FCFC00", what_color="#0092AD")

        tg.SetPronouns(pronoun_list["He"])
        
        tg.Add("testguy_inches", 3)
        tg.Add("testguy_fitchoice", "white")
        
        return tg