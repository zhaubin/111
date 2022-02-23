def on_a_pressed():
    mySprite.start_effect(effects.spray)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

mySprite: Sprite = None
mySprite = sprites.create(assets.image("""
    DOG
"""), SpriteKind.player)
controller.move_sprite(mySprite)