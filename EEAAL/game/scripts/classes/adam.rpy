init python:
    class Adam:
        def __init__(self, character):
            self.name = "Adam" # This does not change
            
            self.c = character
            self.p = Pronouns()
            
        def SetPronouns(self, new_pronoun):
            self.p = new_pronoun
            
            # We create useful string attribute shorthands for the Adam object here, so they can be immediately referenced
            # Maybe we move this into the general pronoun object but especially for customizable protag, these should be immediately accessible
            self.pronoun_shorthand = self.p.Shorthand()
        
        @property
        def PronounShorthand(self):
            return self.p.Shorthand()
        
        @property
        def They(self):
            return self.p.They()
        
        @property
        def Them(self):
            return self.p.Them()
            
        @property
        def Their(self):
            return self.p.Their()
            
        @property
        def Theirs(self):
            return self.p.Theirs()
            
        @property
        def Themselves(self):
            return self.p.Themselves()
            
        @property
        def they(self):
            return self.p.they()
        
        @property
        def them(self):
            return self.p.them()
            
        @property
        def their(self):
            return self.p.their()
            
        @property
        def theirs(self):
            return self.p.theirs()
            
        @property
        def themselves(self):
            return self.p.themselves()
            
        @property
        def THEY(self):
            return self.p.THEY()
        
        @property
        def THEM(self):
            return self.p.THEM()
            
        @property
        def THEIR(self):
            return self.p.THEIR()
            
        @property
        def THEIRS(self):
            return self.p.THEIRS()
            
        @property
        def THEMSELVES(self):
            return self.p.THEMSELVES()