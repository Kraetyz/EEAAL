# Custom images
#I am including here the example code for making a character's eyes blink
image xoos_blink:
    "images/characters/xoos/xoos_l7_eyelids_open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/xoos/xoos_l7_eyelids_closed.png"
    pause 0.1
    repeat

# End Custom images

# The layeredimage definition at the bottom

layeredimage Xoos_Front:
    group backhair:
        attribute regular default:
            "images/characters/xoos/xoos_l0_hairback.png"
    group body:
        attribute regular default:
            "images/characters/xoos/xoos_l1_body.png"
            
    group outfit:
        attribute regular default:
            "images/characters/xoos/xoos_l2_outfit.png"

    group head:
        attribute regular default:
            "images/characters/xoos/xoos_l3_head.png"

    group mouth:
        attribute closed default:
            "images/characters/xoos/xoos_l4_mouth_closed.png"
        attribute open:
            "images/characters/xoos/xoos_l4_mouth_open.png"

    group eyewhites:
        attribute regular default:
            "images/characters/xoos/xoos_l5_eyewhite.png"

    # See about animating these for fun some time! Make them look left/right
    group eyeballs:
        attribute regular default:
            "images/characters/xoos/xoos_l6_eyes.png"

    group eyelids:
        attribute regular default:
            "xoos_blink"

    group fronthair:
        attribute regular default:
            "images/characters/xoos/xoos_l8_hairfront.png"

# End layeredimage definition