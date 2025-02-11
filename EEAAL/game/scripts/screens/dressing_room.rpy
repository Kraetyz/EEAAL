# Maybe use defined images instead of slapping transforms on there (see above)
# Or don't. See what feels best.
screen dressing_room(outfits):

    # outfits needs to contain only names that exist as images in the adam folder
    # Or "None", which is a special case for getting nakey. For now - should maybe be removed eventually.
    for i, outfit in enumerate(outfits):
        hbox:
            pos(50 + 150*i, 50)
            if outfit == "None":
                imagebutton idle "images/adam/Adam_Body.png" action Call("switch_adams_outfit", newfit=outfit, ret=False):
                    at transform:
                        zoom 0.1
            else:
                #These imagebuttons will eventually be using the "auto" setting, idle is just until we have any kind of assets
                imagebutton idle "images/adam/" + outfit + ".png" action Call("switch_adams_outfit", newfit=outfit, ret=False):
                    at transform:
                        zoom 0.1

    vbox:
        yalign 0.9
        xalign 0.3
        imagebutton idle "temp_back_btn.png" action Return()
        #textbutton "Go back" action Return():
         #   at transform:
          #      zoom 2