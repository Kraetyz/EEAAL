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