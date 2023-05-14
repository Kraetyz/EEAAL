label switch_adams_outfit(newfit="None"):
    python:
        if newfit in Adam.outfits:
            Adam.outfit = newfit

label dressing_room:
    show Adam_Front at right
    call screen dressing_room
    call daymenu