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
            
    Adam.c "My pronouns are [Adam.pronoun_shorthand]."
    
    n "When anyone refers to Adam, they will say: [Adam.They] grabbed [Adam.their] book."

    n "The book was gifted to [Adam.them]. It was [Adam.theirs] to keep."
    
    n "Someone yelled, \"ADAM CAN GO FUCK [Adam.THEMSELVES]\" but Adam did not hear."
    
    Adam.c "I definitely heard that."
    
    n "All becomes black. And Adam returns to hell."
    
    n "[Adam.They] will come with us, for this is [Adam.their] story."
    
    jump daymenu