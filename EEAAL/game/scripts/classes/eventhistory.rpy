init python:
    class EventHistoryElement:
        def __init__(self, participants, tuples):
            self.participants = participants
            self.data = dict()
            for tuple in tuples:
                self.data[tuple[0]] = tuple[1]
        
        def GetData(self, key):
            if (key in self.data):
                return self.data[key]
            return "DNE"
        
        def GetParticipants(self):
            return self.participants

    class EventHistory:
    
        def __init__(self):
            self.history = dict()
        
        # participants is a list of characters
        # tuples is a list of tuple values
        def AddEvent(self, name, participants, tuples):
            newEvent = EventHistoryElement(participants, tuples)
            self.history[name] = newEvent
        
        def GetEvent(self, name):
            if (name in self.history):
                return self.history[name]
            return "DNE"
        
        def GetEventData(self, name, key):
            event = self.GetEvent(name)
            if (event == "DNE"):
                return event
            return event.GetData(key)
        
        def GetEventParticipants(self, name):
            event = self.GetEvent(name)
            if (event == "DNE"):
                return event
            return event.GetParticipants()
            
        def EventHasParticipant(self, name, participant):
            event = self.GetEvent(name)
            if (event == "DNE"):
                return event
            participants = event.GetParticipants()
            return participant in participants