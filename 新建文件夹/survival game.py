import pygame
import random

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
      self.rect.y -= 7
    elif keystate[pygame.K_DOWN]:
      self.rect.y += 7
    elif keystate[pygame.K_LEFT]:
      self.rect.x -= 7
    elif keystate[pygame.K_RIGHT]:
      self.rect.x += 7
    if self.rect.x>500:
      self.rect.x = 0
    if self.rect.y>500:
      self.rect.y = 0
    if self.rect.x<0:
      self.rect.x = 500
    if self.rect.y<0:
      self.rect.y = 500



class Enemy(pygame.sprite.Sprite):
  def __init__(self, image,scale, x , y):
    pygame.sprite.Sprite.__init__(self)
    width = image.get_width()  
    height = image.get_height()
    #scale image by specified scale size
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (random.randint(0,500), random.randint(0,500))
    self.speed = 1

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

house_img = pygame.image.load("pause.jpg")#pause
play_img = pygame.image.load("play.jpg")
pause_img = pygame.image.load("x.jpg") #quit
restart_img = pygame.image.load("restart.jpg")
play_btn = Button(play_img, 0.05, 150, 250)
pause_btn = Button(pause_img, 0.05, 350, 250)
house_btn = Button(house_img, 0.05, 370, 50)
restart_btn = Button(restart_img, 0.08, 450, 55)


hamster_img = pygame.image.load("mouse.jpg")
player = Player(hamster_img, 0.06, 500, 500)
player_group = pygame.sprite.Group()
player_group.add(player)  # add player object to player group

cat_img = pygame.image.load("cat2.jpg")
enemy = Enemy(cat_img, 0.09, 0, 0)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)  

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
game_state="menu"

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

def you_died():
  global game_state
  global score
  screen.fill((0,0,0))
  text_to_screen(screen, "You Died", 165, 120, size=100, color = (255,255,255))
  if restart_btn.draw():
    score = 0  
    game_state = "game"  
    pygame.display.update()
    
  if house_btn.draw():
    game_state = "menu"  
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
  
    if house_btn.draw():
      game_state="menu"
      pygame.display.update()

    if pygame.sprite.spritecollideany(player, enemy_group):
      print("Collision detected!")
      game_state="dead"
      pygame.display.update()

    if pygame.sprite.spritecollideany(player, superpower_group):
      score += 1
      superpower_group.update()
    
    text_to_screen(screen, 'Score: {}'.format(score), 5, 5, size=50)

    player_group.draw(screen)
    player_group.update() 
    enemy_group.draw(screen)
    enemy_group.update(player)
    superpower_group.draw(screen)
    pygame.display.set_caption("Score:{}".format(score))

  elif game_state == "dead":
    you_died()


  pygame.display.update() 
  screen.fill((0, 0, 0))
  # if play_btn.draw():
  #   print("Play")
  # if pause_btn.draw():
  #   print("Pause")


  clock.tick(60)




