from pygame import *
from Sprite import GameSprite
from enemy import EnemySprite
window = display.set_mode((300, 168))
display.set_caption("Catch")
background = transform.scale(image.load("D:\\Proiecte VsCode Algorithmics\\Pygame\\fn1.jpg"), (300, 168))
window.blit(background, (0,0))
mixer.init()
mixer.music.load("D:\Proiecte VsCode Algorithmics\Pygame\music.mp3")
mixer.music.set_volume(0.3)
mixer.music.play()

bd = GameSprite("D:\Proiecte VsCode Algorithmics\Pygame\sprite(bd).png", 0,0, 1)

clock = time.Clock()
FPS = 144

game = True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    bd.update(window)
    bd.handle_events()
    display.update()
    display.update()
    clock.tick(FPS)

