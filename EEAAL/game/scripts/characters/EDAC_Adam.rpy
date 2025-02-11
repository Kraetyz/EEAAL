init python:
    def CreateAdam():
        Adam = EDACharacter("Adam")
        Adam.c = Character("Adam", color="#F5DA56", what_color="#7D5F7A")

        Adam.SetPronouns(pronoun_list["They"])
        
        Adam.Add("social", 0)
        
        Adam.Add("outfit", "Adam_Outfit_NPC")
        Adam.Add("outfits", ["None", "Adam_Outfit_NPC", "Adam_Outfit_Blue", "Adam_Outfit_Red"])
        
        return Adam