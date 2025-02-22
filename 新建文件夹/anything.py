# import pygame
# class Enemy(pygame.sprite.Sprite):
#     def _init_(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((50, 50))
#         self.image.fill((0, 0, 255))
#         self.rect = self.image.get_rect()
# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("Anything")

# enermy = Enemy()
# player_group = pygame.sprite.Group()
# player_group.add(enermy)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     pygame.display.update()  
#     screen.fill((0, 0, 0)) # fill in screen with bg color for every update 
#     player_group.draw(screen)
#     clock.tick(60)

import pygame
# class Enemy(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((50, 50))
#         self.image.fill((0, 150, 200))
#         self.rect = self.image.get_rect()
#     def update(self):
#         # self.rect.x += 5
#         self.rect.y += 5
#         if self.rect.left>500:
#             self.rect.right = 0
#         if self.rect.top>500:
#             self.rect.bottom = 0

# pygame.init()
# screen = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("Debug")
# enemy = Enemy()
# player_group = pygame.sprite.Group()
# player_group.add(enemy)
# clock = pygame.time.Clock()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((0, 0, 0))
#     player_group.draw(screen)
#     player_group.update()
#     pygame.display.update()
#     clock.tick(60)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 150, 200))
        self.rect = self.image.get_rect()
    def update(self):
        # self.rect.x += 5
        self.rect.x = 275
        self.rect.y += 5
        if self.rect.left>600:
            self.rect.right = 0
        if self.rect.top>500:
            self.rect.bottom = 0

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Debug")
enemy = Player()
player_group = pygame.sprite.Group()
player_group.add(enemy)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((0, 0, 0))
    player_group.draw(screen)
    player_group.update()
    pygame.display.update()
    clock.tick(60)
     
     