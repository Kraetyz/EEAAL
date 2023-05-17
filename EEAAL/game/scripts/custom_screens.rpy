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


# Maybe use defined iamges instead of slapping transforms on there (see above)
# Or don't. See what feels best.
screen dressing_room(outfits):

    # outfits needs to contain only names that exist as images in the adam folder
    # Or "None", which is a special case for getting nakey. For now - should maybe be removed eventually.
    for i, outfit in enumerate(outfits):
        hbox:
            pos(50 + 150*i, 50)
            if outfit == "None":
                imagebutton idle "images/adam/Adam_Body.png" action Call("switch_adams_outfit", "None"):
                    at transform:
                        zoom 0.1
            else:
                #These imagebuttons will eventually be using the "auto" setting, idle is just until we have any kind of assets
                imagebutton idle "images/adam/" + outfit + ".png" action Call("switch_adams_outfit", outfit):
                    at transform:
                        zoom 0.1

    vbox:
        yalign 0.9
        xalign 0.3
        textbutton "Go back" action Return():
            at transform:
                zoom 2