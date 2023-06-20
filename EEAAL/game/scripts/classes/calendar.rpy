init python:
    class Calendar:
    
        def __init__(self):
            #I am lazy so this is just an integer. 0 = Morning, 1 = Day, 2 = Afternoon, 3 = Evening
            #Every pass through the day loop increases timeofday by one, then resets after 3 and updates the day.
            self.timeofday = 0
            
            #See above as per laziness. In time we will have proper dates here.
            self.date = 0
            
            #TO-DO: What else do we put here?
            #Information about Time of Day display images?
            #UI rendering more generally? (probably not? idk)
            
        def GetTimeOfDay(self):
            return self.timeofday
            
        def GetTimeOfDayStr(self):
            if (self.timeofday == 0):
                return "Morning"
            if (self.timeofday == 1):
                return "Lunch"
            if (self.timeofday == 2):
                return "Afternoon"
            if (self.timeofday == 3):
                return "Evening"
            return "What the fuck?"
        
        def GetDate(self):
            return self.date
            
        def NextTimeOfDay(self):
            self.timeofday = (self.timeofday + 1) % 4
            if (self.timeofday == 0):
                self.NextDay()
        
        def NextDay(self):
            self.date = self.date + 1