controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.startEffect(effects.spray)
})
let mySprite: Sprite = null
mySprite = sprites.create(assets.image`DOG`, SpriteKind.Player)
controller.moveSprite(mySprite)
