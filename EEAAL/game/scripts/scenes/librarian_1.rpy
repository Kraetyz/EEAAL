label librarian_1:
    show Adam_Front at left, normal_size
    
    Librarian.c "I haven’t seen you around before, what brings you to this small, deserted part of the world? The name’s Grace if you’re wonderin’."
    $Librarian.SetName("Grace")
    
    menu:
        "I just moved to town and I’m looking for new adventures!":
            jump option_1
        "I’m hoping that with the help of my green thumb I can bring some colour to this town. My name is Adam, by the way.":
            jump option_2
    
    label option_1:
        Librarian.c "Do you realize you’ve just stepped into a world that is far more complicated than they want you to believe? You’ll find adventures here all right, for better or worse. Just you wait…"
        
        menu:
            "Oh, okay. It was nice meeting you Grace. I’m Adam.":
                $Librarian.Plus("points", 1)
            "You’re kind of weird.":
                $Librarian.Minus("points", 1)
            "Say nothing and leave.":
                Librarian.c "Oh, okay then."
            "Sounds like a great opportunity then! My name’s Adam, by the way, and it was nice to meet you." if Adam.AdventurousPersonality():
                $Librarian.Minus("points", 2)
            "Oh no, uh, that sounds a bit ominous. My name’s Adam. Please let me know if anything bad is going to happen…" if Adam.BashfulPersonality():
                $Librarian.Plus("points", 2)
            "Don’t you worry Grace, I can handle anything life throws at me. My name’s Adam, by the way, though one day I won’t even need to introduce myself." if Adam.ConfidentPersonality():
                $librarian_points = librarian_points
                
        jump dayloop_done
        
    label option_2:
        Librarian.c "Hah! Colour. Don’t you know that the government spreading those toxic chemtrails from their flying machines is the whole reason nothing will grow here anymore!?"
        
        menu:
            "I’m not sure that is true, but either way I’m going to try!":
                $Librarian.Plus("points", 1)
            "Are you crazy? You know chemtrails aren’t real right?":
                $Librarian.Minus("points", 1)
            "Say nothing and leave.":
                Librarian.c "Oh, okay then."
            "So you’re saying I have a challenge to overcome! I’ll get down to the bottom of it and try my hardest." if Adam.AdventurousPersonality():
                $Librarian.Minus("points", 2)
            "Do you really think that’s why nothing grows here? I’m not sure about that but maybe I can still try." if Adam.BashfulPersonality():
                $Librarian.Plus("points", 2)
            "That won’t stop me from making this place beautiful, I’m going to prove you wrong, you’ll see!" if Adam.ConfidentPersonality():
                $librarian_points = librarian_points
                
        jump dayloop_done