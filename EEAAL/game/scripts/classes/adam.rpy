init python:
    class Adam:
        def __init__(self, character):
            self.name = "Adam" # This does not change
            
            self.c = character
            self.p = Pronouns()
            
            # This is a test version of what will hopefully be a more refined system in the future
            # 0 = Assertive, 1 = Confident, 2 = Pensive
            self.personality = 0
            
            self.outfit = "Adam_Outfit_NPC"
            
            self.outfits = ["None", "Adam_Outfit_NPC", "Adam_Outfit_Blue", "Adam_Outfit_Red"]
        
        # These are the methods we will be using to handle the test version of our personality system
        def SetPersonality(self, new_personality):
            if new_personality > -1 and new_personality < 3:
                self.personality = new_personality
        def AdventurousPersonality(self):
            return self.personality == 0
        def BashfulPersonality(self):
            return self.personality == 2
        def ConfidentPersonality(self):
            return self.personality == 1  
        
        
        def SetPronouns(self, new_pronoun):
            self.p = new_pronoun
        
        @property
        def PronounShorthand(self):
            return self.p.Shorthand
        
        @property
        def They(self):
            return self.p.They
        @property
        def Them(self):
            return self.p.Them
        @property
        def Their(self):
            return self.p.Their
        @property
        def Theirs(self):
            return self.p.Theirs    
        @property
        def Themselves(self):
            return self.p.Themselves
        @property
        def Theyre(self):
            return self.p.Theyre
        @property
        def Theyve(self):
            return self.p.Theyve
        @property
        def Theyll(self):
            return self.p.Theyll
        @property
        def Theyd(self):
            return self.p.Theyd

        @property
        def they(self):
            return self.p.they
        @property
        def them(self):
            return self.p.them
        @property
        def their(self):
            return self.p.their
        @property
        def theirs(self):
            return self.p.theirs
        @property
        def themselves(self):
            return self.p.themselves
        @property
        def theyre(self):
            return self.p.theyre
        @property
        def theyve(self):
            return self.p.theyve
        @property
        def theyll(self):
            return self.p.theyll
        @property
        def theyd(self):
            return self.p.theyd
            
        @property
        def THEY(self):
            return self.p.THEY
        @property
        def THEM(self):
            return self.p.THEM
        @property
        def THEIR(self):
            return self.p.THEIR
        @property
        def THEIRS(self):
            return self.p.THEIRS
        @property
        def THEMSELVES(self):
            return self.p.THEMSELVES
        @property
        def THEYRE(self):
            return self.p.THEYRE
        @property
        def THEYVE(self):
            return self.p.THEYVE
        @property
        def THEYLL(self):
            return self.p.THEYLL
        @property
        def THEYD(self):
            return self.p.THEYD