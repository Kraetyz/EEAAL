define n = Character("Narrator")

label start_scene_pronoun_select:

    n "Your name is Adam."
    Adam.c "My name is Adam."
    n "What are your pronouns?"
    
    menu:
        "What are your pronouns?"
        
        "They/Them":
            $Adam.SetPronouns(pronoun_list["They"])
            
        "He/Him":
            $Adam.SetPronouns(pronoun_list["He"])
            
        "She/Her":
            $Adam.SetPronouns(pronoun_list["She"])
            
        "Ze/Hir":
            $Adam.SetPronouns(pronoun_list["Ze"])
        
        "Xe/Xem":
            $Adam.SetPronouns(pronoun_list["Xe"])
            
    Adam.c "My pronouns are [Adam.PronounShorthand]."
        
    n "When anyone refers to Adam, they will say: [Adam.They] grabbed [Adam.their] book."

    n "The book was gifted to [Adam.them]. It was [Adam.theirs] to keep."
    
    n "Someone yelled, \"ADAM CAN GO FUCK [Adam.THEMSELVES]\" but Adam did not hear."
    
    Adam.c "I definitely heard that."
    
    jump start_scene_town_name_select
    
label start_scene_town_name_select:
    n "You are moving to another country. Which country isn't important, because the plastic hell of modern life is all-encompassing."
    Adam.c "What's the name of the town to which I am moving?"
    n "That is for you to decide."
    
    label town_name_input:
        python:
            town_name = renpy.input("What is the name of this town?", length=32)
            town_name = town_name.strip()

    if not town_name:
        jump town_name_input
    
    n "And thus, Adam moved to [town_name]. [Adam.Their] life was about to become a lot more complicated."
    
    jump dayloop