init python:
    def CreatePenpal():
        paypal = EDACharacter("Pen")
        paypal.c = Character("Pen")

        paypal.SetPronouns(pronoun_list["They"])
        
        paypal.Add("points", 0)
        
        return paypal