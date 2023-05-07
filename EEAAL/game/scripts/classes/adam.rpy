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

            # Subject
            self.They = self.p.They()
            # Object
            self.Them = self.p.Them()
            # Possessive
            self.Their = self.p.Their()
            # Possessive pronoun
            self.Theirs = self.p.Theirs()
            # Reflexive
            self.Themselves = self.p.Themselves()
                
            # Same as above but lower case
            self.they = self.p.they()
            self.them = self.p.them()
            self.their = self.p.their()
            self.theirs = self.p.theirs()
            self.themselves = self.p.themselves()

            # Same as above but capital case
            self.THEY = self.p.THEY()
            self.THEM = self.p.THEM()
            self.THEIR = self.p.THEIR()
            self.THEIRS = self.p.THEIRS()
            self.THEMSELVES = self.p.THEMSELVES()
