from pygame import *
class GameSprite (sprite. Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.start_x = player_x
        self.start_y = player_y

    def update(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def reset(self, window):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.update(window)
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    def handle_events(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.move(-self.speed, 0)
        if keys[K_RIGHT]:
            self.move(self.speed, 0)
        if keys[K_UP]:
            self.move(0, -self.speed)
        if keys[K_DOWN]:
            self.move(0, self.speed)