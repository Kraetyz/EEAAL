init:
    transform left_to_right:
        xalign -1.0
        linear 2.5 xalign 2.0
        repeat
        
    transform zig_zag_vibrate:
        linear 0.05 xoffset 3
        linear 0.05 xoffset -6 
        linear 0.05 xoffset 6
        linear 0.05 xoffset -6
        linear 0.05 xoffset 3
        pause 1
        repeat

    transform whacky_zoom:
        easeout 0.3 zoom 2.5
        linear 0.1 zoom 1.5
        easein 0.5 zoom 4