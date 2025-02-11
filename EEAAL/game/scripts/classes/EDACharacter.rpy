init python:
    class EDACharacter:

        def __init__(self, name):
            self.name = name
            self.pronouns = Pronouns()
            self.personality = 0
            self.outfit = "DNE"
            
            self.c = Character(name)
            
            self.attributes = dict()
            
            
# HELPERS
        def SetName(self, name):
            self.name = name
            self.c.name = name

                
# PERSONALITY V 1
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





# GENERIC ATTRIBUTE TRACKING
        def Add(self, attrname, attrval):
            self.attributes[attrname] = attrval
        
        def Set(self, attrname, attrval):
            if (attrname in self.attributes):
                self.attributes[attrname] = attrval
            else:
                 renpy.jump_out_of_context("Set FAIL")
        
        def Get(self, attrname):
            if (attrname in self.attributes):
                return self.attributes[attrname]
            return "DNE"      
            
        # Simple arithmetic helpers
        def Plus(self, attrname, plus):
            attrval = self.Get(attrname)
            if (attrval != "DNE"):
                self.Set(attrname, attrval + plus)
            else:
                renpy.jump_out_of_context("Plus FAIL")
        
        def Minus(self, attrname, minus):
            attrval = self.Get(attrname)
            if (attrval != "DNE"):
                self.Set(attrname, attrval - minus)
            else:
                renpy.jump_out_of_context("Minus FAIL")
        
        
            
            
            
            
# PRONOUN MANAGEMENT
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
            