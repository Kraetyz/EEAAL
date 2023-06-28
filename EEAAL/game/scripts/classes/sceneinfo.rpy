init python:
    class SceneInfo:
        #sceneName: a string with a name for the sceneName
        #label: the logical renpy label which begins the sceneName
        #duration: the number of time skips the scene performs
        #characters: an array of character objects to display their pictures/names/whatever (KRATZ TO-DO: this is currently just an array of names)
        def __init__(self, sceneName, label, duration, characters):
            self.Name = sceneName
            self.Label = label
            self.Duration = duration
            self.Characters = characters
            
        def StartScene(self):
            renpy.jump(self.Label)
        
        @property
        def CharacterList(self):
            return ", ".join(self.Characters)