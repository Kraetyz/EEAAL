### Playground for trying scene stuff?
screen interacting_with_background():
    tag interactable_background
    layer "scene_bg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton idle "stolen_wooden_sign.jpg" action ShowMenu('save')

### DEFINED IMAGE AS IMAGEBUTTON PROOF OF CONCEPT
image test_image:
    "stolen_wooden_sign.jpg"
screen test_scene():
    imagebutton idle 'test_image' action ShowMenu('save')


# This needs to be expanded so that the clothes are filled into the screen via a loop
# And maybe use defined iamges instead of slapping transforms on there (see above)
# Or don't. See what feels best.
screen dressing_room():
    hbox:
        pos(50, 50)
        imagebutton idle "images/adam/Adam_Body.png" action Call("switch_adams_outfit", "None"):
            at transform:
                zoom 0.1
    
    hbox:
        pos(200, 50)
        imagebutton idle "images/adam/Adam_Outfit_NPC.png" action Call("switch_adams_outfit", "Adam_Outfit_NPC"):
            at transform:
                zoom 0.1
        
    hbox:
        pos(350, 50)
        imagebutton idle "images/adam/Adam_Outfit_Red.png" action Call("switch_adams_outfit", "Adam_Outfit_Red"):
            at transform:
                zoom 0.1
        
    hbox:
        pos(500, 50)
        imagebutton idle "images/adam/Adam_Outfit_Blue.png" action Call("switch_adams_outfit", "Adam_Outfit_Blue"):
            at transform:
                zoom 0.1
    
    vbox:
        yalign 0.9
        xalign 0.3
        textbutton "Go back" action Return():
            at transform:
                zoom 2