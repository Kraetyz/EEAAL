init python:
    class Pronouns:
        def __init__(self, pronoun_shorthand = "They/Them", subject = "They", object = "Them", possessive = "Their", possessive_pronoun = "Theirs", reflexive = "Themselves"):
            self.shorthand = pronoun_shorthand
            self.subject = subject
            self.object = object
            self.possessive = possessive
            self.possessive_pronoun = possessive_pronoun
            self.reflexive = reflexive
        
        # A way to refer to the set of pronouns
        def Shorthand(self):
            return self.shorthand

        # Subject
        def They(self):
            return self.subject
        # Object
        def Them(self):
            return self.object
        # Possessive
        def Their(self):
            return self.possessive
        # Possessive pronoun
        def Theirs(self):
            return self.possessive_pronoun
        # Reflexive
        def Themselves(self):
            return self.reflexive
            
        # Same as above but lower case
        def they(self):
            return self.subject.lower()
        def them(self):
            return self.object.lower()
        def their(self):
            return self.possessive.lower()
        def theirs(self):
            return self.possessive_pronoun.lower()
        def themselves(self):
            return self.reflexive.lower()

        # Same as above but capital case
        def THEY(self):
            return self.subject.upper()
        def THEM(self):
            return self.object.upper()
        def THEIR(self):
            return self.possessive.upper()
        def THEIRS(self):
            return self.possessive_pronoun.upper()
        def THEMSELVES(self):
            return self.reflexive.upper()