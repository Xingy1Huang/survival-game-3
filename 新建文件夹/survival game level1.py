import pygame
import random
import time

player_speed = 7

class Player(pygame.sprite.Sprite):

  def __init__(self, image, scale, x, y):  
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()  
    height = image.get_height()
    #scale image by specified scale size
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

  def update(self):
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
      self.rect.y -= player_speed
    elif keystate[pygame.K_DOWN]:
      self.rect.y += player_speed
    elif keystate[pygame.K_LEFT]:
      self.rect.x -= player_speed
    elif keystate[pygame.K_RIGHT]:
      self.rect.x += player_speed
    if self.rect.x>500:
      self.rect.x = 0
    if self.rect.y>500:
      self.rect.y = 0
    if self.rect.x<0:
      self.rect.x = 500
    if self.rect.y<0:
      self.rect.y = 500



class Enemy(pygame.sprite.Sprite):
  def __init__(self, image,scale, x , y, speed):
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()  
    height = image.get_height()
    #scale image by specified scale size
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)
    self.speed = speed

  def update(self,target):
    # self.rect.x += random.choice ([0,-self.speed,self.speed])
    # self.rect.y += random.choice ([0,-self.speed,self.speed])
    # print("rfgydbmx"
    if self.rect.x > target.rect.x:
        self.rect.x-=self.speed
    if self.rect.x < target.rect.x:
        self.rect.x+=self.speed
    if self.rect.y > target.rect.y:
      self.rect.y-=self.speed
    if self.rect.y < target.rect.y:
      self.rect.y+=self.speed

    if self.rect.x>500:
      self.rect.x = 0
    if self.rect.y>500:
      self.rect.y = 0
    if self.rect.x<0:
      self.rect.x = 500
    if self.rect.y<0:
      self.rect.y = 500





class Bomb(pygame.sprite.Sprite):
  def __init__(self, image,scale, x , y, speed):
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()  
    height = image.get_height()
    #scale image by specified scale size
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)
    self.speed = speed

  def update(self,direction):
    if direction == 1:
      if self.rect.x <= 500:
        self.rect.x += self.speed
      else:
        self.rect.x -= self.speed
      

    else:
      if self.rect.y <= 500:
        self.rect.y += self.speed
      else:
        self.rect.y -= self.speed

    if self.rect.x>500:
      self.rect.x = 0
    if self.rect.y>500:
      self.rect.y = 0
    if self.rect.x<0:
      self.rect.x = 500
    if self.rect.y<0:
      self.rect.y = 500



class Superpower(pygame.sprite.Sprite):

  def __init__(self, image, scale, x, y):  
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()  
    height = image.get_height()
    #scale image by specified scale size
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

  def update(self):
      keystate = pygame.key.get_pressed()
      if keystate[pygame.K_w]:
        self.rect.y -= 7
      elif keystate[pygame.K_s]:
        self.rect.y += 7
      elif keystate[pygame.K_a]:
        self.rect.x -= 7
      elif keystate[pygame.K_d]:
        self.rect.x += 7
      if self.rect.x>500:
        self.rect.x = 0
      if self.rect.y>500:
        self.rect.y = 0
      if self.rect.x<0:
        self.rect.x = 500
      if self.rect.y<0:
        self.rect.y = 500



def draw_text(color, text, font, size, x, y, surface):
    font_name = pygame.font.match_font(font)
    Font = pygame.font.Font(font_name, size)
    text_surface = Font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    surface.blit(text_surface,text_rect)



class Superpower(pygame.sprite.Sprite):
  def __init__(self, image,scale, x , y):
    pygame.sprite.Sprite.__init__(self)
    width = 5
    height = 5
    #scale image by specified scale size
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (random.randint(0,500), random.randint(0,500))
    self.speed = 0

  def update(self):
    self.rect.center = (random.randint(0,500), random.randint(0,500))

 

class Button(pygame.sprite.Sprite):

  def __init__(self, image, scale, x, y):
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.clicked = False # include new variable 

  def draw(self):
    screen.blit(self.image, (self.rect.x, self.rect.y))
    pressed = False
    pos = pygame.mouse.get_pos()
    
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        pressed = True
    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False
    return pressed
  


pygame.init()
clock = pygame.time.Clock() # The clock tracks how fast the game is running.
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('explosion.png')

house_img = pygame.image.load("pause.jpg")#pause
play_img = pygame.image.load("play.jpg")
pause_img = pygame.image.load("x.jpg") #quit
restart_img = pygame.image.load("restart.jpg")
level_img = pygame.image.load("next level.jpg")
bomb_img = pygame.image.load("bomb.jpg")
play_btn = Button(play_img, 0.05, 150, 250)
pause_btn = Button(pause_img, 0.05, 350, 250)
house_btn = Button(house_img, 0.05, 370, 50)
restart_btn = Button(restart_img, 0.08, 450, 55)
level_btn = Button(level_img, 0.08, 250, 250)


hamster_img = pygame.image.load("mouse.jpg")
player = Player(hamster_img, 0.06, 400, 400)
player_group = pygame.sprite.Group()
player_group.add(player)  # add player object to player group

enemy_speed=random.randint(1,2)
# enemy_speed2=random.randint(1,2)
enemy_x=random.randint(100,300)
enemy_y=random.randint(100,300)


cat_img = pygame.image.load("cat2.jpg")
enemy = Enemy(cat_img, 0.09, enemy_x, enemy_y, enemy_speed)
# enemy2 = Enemy(cat_img, 0.09, enemy_x, enemy_x, enemy_speed2)
# bomb1 = Bomb(cat_img, 0.09, enemy_x, enemy_x, enemy_speed2)
enemy_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()
enemy_group.add(enemy)  
# bomb_group.add(bomb1)  

superpower_img = pygame.image.load("cheese2.jpg")
superpower = Superpower(superpower_img, 5, 250, 250)
superpower_group = pygame.sprite.Group()
superpower_group.add(superpower)  # add player object to player group

def text_to_screen(screen, text, x, y, size = 30, color = (255, 255, 255)):
    try:
        text = str(text)
        font = pygame.font.Font("Pixellettersfull-BnJ5.ttf", size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
    except Exception as e:
      print('Font Error:', e)
      
score = 0
game_state = "menu"
level = 1
enemy_count = 1
bomb_count = 0
# direction = random.randint(1,2)

def menu():
  global game_state
  screen.fill((0,0,0))
  text_to_screen(screen, "menu", 165, 120, size=100, color = (255,255,255))
  if play_btn.draw():
    game_state="game"
    pygame.display.update()
  if pause_btn.draw():
    pygame.quit()
    quit()

def next_level():
  global game_state
  global enemy_speed
  global player_speed
  global enemy_count
  global bomb_count
  screen.fill((0,0,0))
  text_to_screen(screen, "level complete", 165, 120, size=100, color = (255,255,255))
  if level_btn.draw():
    game_state="level"
    if level == 1:
      enemy_speed=random.randint(1,2)
      player_speed=7
      enemy_count=1
      bomb_count=0
    elif level ==2:
      enemy_speed=random.randint(2,4)
      player_speed=random.randint(7,10)
      enemy_count=1
      bomb_count=2
    elif level ==3:
      enemy_speed=random.randint(4,6)
      player_speed=random.randint(7,10)
      enemy_count=2
      bomb_count=2
  for _ in range(enemy_count): 
    enemy = Enemy(cat_img, 0.09, enemy_x, enemy_y, enemy_speed) 
    enemy_group.add(enemy)
  for _ in range(bomb_count): 
    bomb = Bomb(bomb_img, 0.09, enemy_x, enemy_y, enemy_speed) 
    bomb_group.add(bomb)
  if pause_btn.draw():
    pygame.quit()
    quit()
  pygame.display.update()


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()  

  
    # for event in pygame.event.get():
    #   if event.type == pygame.QUIT:

  if game_state == "menu":
    menu()

  elif game_state == "game":
    if restart_btn.draw():
      score = 0
      enemy_speed=random.randint(1,2)
      enemy_speed2=random.randint(1,2)
      enemy_x=random.randint(100,300)
      enemy_y=random.randint(100,300)
  
    if score == 3:
      game_state="level"


    if house_btn.draw():
      game_state="menu"
      pygame.display.update()

    if pygame.sprite.spritecollideany(player, enemy_group):
      print("Collision detected!")
      pygame.quit() 
      quit()

    if pygame.sprite.spritecollideany(player, bomb_group):
      print("Collision detected!")
      pygame.display.update()
      screen.blit(background, (93, 93))
      pygame.display.update()
      time.sleep(2)
      pygame.quit() 
      quit()

    if pygame.sprite.spritecollideany(player, superpower_group):
      score += 1
      superpower_group.update()
    
    text_to_screen(screen, 'Score: {}'.format(score), 5, 5, size=50)

    player_group.draw(screen)
    player_group.update() 
    enemy_group.draw(screen)
    enemy_group.update(player)
    # bomb_group.draw(screen)
    # bomb_group.update(direction)
    superpower_group.draw(screen)
    pygame.display.set_caption("Score:{}".format(score))
  elif game_state == "level":
    next_level()

  pygame.display.update() 
  screen.fill((0, 0, 0))
  # if play_btn.draw():
  #   print("Play")
  # if pause_btn.draw():
  #   print("Pause")


  clock.tick(60)








