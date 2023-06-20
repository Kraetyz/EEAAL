label switch_adams_outfit(newfit="None", ret=false):
    python:
        if newfit in Adam.outfits:
            Adam.outfit = newfit
    if (ret):
        return

label dressing_room:
    show Adam_Front at right
    call screen dressing_room(Adam.outfits)
    call dayloop.dayloop_menu