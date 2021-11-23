@namespace
class SpriteKind:
    Vakt = SpriteKind.create()
Lyn: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . 
            e e e . . . . e e e . . . . 
            c d d c . . c d d c . . . . 
            c b d d f f d d b c . . . . 
            c 3 b d d b d b 3 c . . . . 
            f b 3 d d d d 3 b f . . . . 
            e d d d d d d d d e . . . . 
            e d f d d d d f d e b f b . 
            f d d f d d f d d f f d f . 
            f b d d b b d d 2 b f d f . 
            . f 2 2 2 2 2 2 d b d b f . 
            . f d d d d d d d f f f . . 
            . f d b d f f f d f . . . . 
            . . f f f f . . f f . . . .
    """),
    SpriteKind.player)
Vakt1 = sprites.create(img("""
        . . . . f f f f f . . . . . . . 
            . . . f e e e e e f f f . . . . 
            . . f d d d e e e e d d f . . . 
            . c d d d d d e e e b d c . . . 
            . c d d d d d d e e b d c . . . 
            c d d f d d f d e e f c . f f . 
            c d d f d d f d e e f . . f e f 
            c d e e d d d d e e f . . f e f 
            . f d d d c d e e f f . . f e f 
            . . f f f d e e e e e f . f e f 
            . . . . f e e e e e e e f f f . 
            . . . . f f e e e e e b f f . . 
            . . . f e f f e e c d d f f . . 
            . . f d d b d d c f f f . . . . 
            . . f d d c d d d f f . . . . . 
            . . . f f f f f f f . . . . . .
    """),
    SpriteKind.Vakt)
tiles.set_tilemap(tilemap("""level3"""))
for index in range(5):
    Lyn = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . 4 4 4 . . . . 4 4 4 . . . . 
                    . 4 5 5 5 e . . e 5 5 5 4 . . . 
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . . 
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . . 
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . . 
                    . e e 5 5 5 5 5 5 5 5 e e . . . 
                    . . e 5 f 5 5 5 5 f 5 e . . . . 
                    . . f 5 5 5 4 4 5 5 5 f . f f . 
                    . . . 4 5 5 f f 5 5 6 f f 5 f . 
                    . . . f 6 6 6 6 6 6 4 f 5 5 f . 
                    . . . f 5 5 5 5 5 5 5 4 5 f . . 
                    . . . . f 5 4 5 f 5 f f f . . . 
                    . . . . . f f f f f f f . . . .
        """),
        SpriteKind.food)
    tiles.place_on_random_tile(Lyn, sprites.swamp.swamp_tile16)