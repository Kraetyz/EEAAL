init python:
    class Pronouns:
        def __init__(self, pronoun_shorthand = "They/Them", subject = "They", object = "Them", possessive = "Their", possessive_pronoun = "Theirs", reflexive = "Themselves", contract_is = "'re", contract_have="'ve", contract_will="'ll", contract_would="'d"):
            self.shorthand = pronoun_shorthand
            self.subject = subject
            self.object = object
            self.possessive = possessive
            self.possessive_pronoun = possessive_pronoun
            self.reflexive = reflexive
            self.contract_is = contract_is
            self.contract_have = contract_have
            self.contract_will = contract_will
            self.contract_would = contract_would
        
        # A way to refer to the set of pronouns
        @property
        def Shorthand(self):
            return self.shorthand

        # Subject
        @property
        def They(self):
            return self.subject
        # Object
        @property
        def Them(self):
            return self.object
        # Possessive
        @property
        def Their(self):
            return self.possessive
        # Possessive pronoun
        @property
        def Theirs(self):
            return self.possessive_pronoun
        # Reflexive
        @property
        def Themselves(self):
            return self.reflexive
        # Contraction with is/are
        @property
        def Theyre(self):
            return self.subject + self.contract_is
        @property
        def Theyve(self):
            return self.subject + self.contract_have
        @property
        def Theyll(self):
            return self.subject + self.contract_will
        @property
        def Theyd(self):
            return self.subject + self.contract_would
            
        # Same as above but lower case
        @property
        def they(self):
            return self.subject.lower()
        @property
        def them(self):
            return self.object.lower()
        @property
        def their(self):
            return self.possessive.lower()
        @property
        def theirs(self):
            return self.possessive_pronoun.lower()
        @property
        def themselves(self):
            return self.reflexive.lower()
        @property
        def theyre(self):
            return (self.subject + self.contract_is).lower()
        @property
        def theyve(self):
            return (self.subject + self.contract_have).lower()
        @property
        def theyll(self):
            return (self.subject + self.contract_will).lower()
        @property
        def theyd(self):
            return (self.subject + self.contract_would).lower()

        # Same as above but capital case
        @property
        def THEY(self):
            return self.subject.upper()
        @property
        def THEM(self):
            return self.object.upper()
        @property
        def THEIR(self):
            return self.possessive.upper()
        @property
        def THEIRS(self):
            return self.possessive_pronoun.upper()
        @property
        def THEMSELVES(self):
            return self.reflexive.upper()
        @property
        def THEYRE(self):
            return (self.subject + self.contract_is).upper()
        @property
        def THEYVE(self):
            return (self.subject + self.contract_have).upper()
        @property
        def THEYLL(self):
            return (self.subject + self.contract_will).upper()
        @property
        def THEYD(self):
            return (self.subject + self.contract_would).upper()