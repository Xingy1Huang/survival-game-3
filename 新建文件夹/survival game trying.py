import pygame
import random
import time
import math

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
    if self.rect.x>1000:
      self.rect.x = 0
    if self.rect.y>1000:
      self.rect.y = 0
    if self.rect.x<0:
      self.rect.x = 1000
    if self.rect.y<0:
      self.rect.y = 1000






def checking_distance(x2,y2):
  safe=False
  while not safe:
    x1=random.randint(0,1000)
    y1=random.randint(0,1000)
    distance=math.sqrt((y2-y1)**2+(x2-x1)**2)
    if distance>400:
      safe=True
  return x1,y1





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


    if self.rect.x>1000:
      self.rect.x = 0
    if self.rect.y>1000:
      self.rect.y = 0
    if self.rect.x<0:
      self.rect.x = 1000
    if self.rect.y<0:
      self.rect.y = 1000










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
      if self.rect.x <= 1000:
        self.rect.x += self.speed
      else:
        self.rect.x -= self.speed
     


    else:
      if self.rect.y <= 1000:
        self.rect.y += self.speed
      else:
        self.rect.y -= self.speed


    if self.rect.x>1000:
      self.rect.x = 0
    if self.rect.y>1000:
      self.rect.y = 0
    if self.rect.x<0:
      self.rect.x = 1000
    if self.rect.y<0:
      self.rect.y = 1000






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
      if self.rect.x>1000:
        self.rect.x = 0
      if self.rect.y>1000:
        self.rect.y = 0
      if self.rect.x<0:
        self.rect.x = 1000
      if self.rect.y<0:
        self.rect.y = 1000







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
    self.rect.center = (random.randint(0,1000), random.randint(0,1000))
    self.speed = 0


  def update(self):
    self.rect.center = (random.randint(0,1000), random.randint(0,1000))


 


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
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('explosion.png')


house_img = pygame.image.load("pause.jpg")#pause
play_img = pygame.image.load("play.jpg")
pause_img = pygame.image.load("x.jpg") #quit
restart_img = pygame.image.load("restart.jpg")
level_img = pygame.image.load("next level.jpg")
bomb_img = pygame.image.load("bomb.jpg")
play_btn = Button(play_img, 0.05, 150+250, 250+250)
pause_btn = Button(pause_img, 0.05, 350+250, 250+250)
house_btn = Button(house_img, 0.05, 370, 50)
restart_btn = Button(restart_img, 0.08, 450, 55)
level_btn = Button(level_img, 0.08, 400, 500)




hamster_img = pygame.image.load("mouse.jpg")
player = Player(hamster_img, 0.06, 400, 400)
player_group = pygame.sprite.Group()
player_group.add(player)  # add player object to player group


enemy_speed=random.randint(1,2)
# enemy_speed2=random.randint(1,2)
# enemy_x=random.randint(100,300)
# enemy_y=random.randint(100,300)
enemy_x, enemy_y = checking_distance(player.rect.x, player.rect.y)



cat_img = pygame.image.load("cat2.jpg")
enemy = Enemy(cat_img, 0.09, enemy_x, enemy_y, enemy_speed)
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
superpower_count = 1
# direction = random.randint(1,2)


def menu():
  global game_state
  screen.fill((0,0,0))
  text_to_screen(screen, "menu", 165+250, 120+250, size=100, color = (255,255,255))
  if play_btn.draw():
    game_state="game"
    pygame.display.update()
  if pause_btn.draw():
    pygame.quit()
    quit()


def next_level():
    global game_state, level, enemy_speed, player_speed, enemy_count, bomb_count, score


    screen.fill((0, 0, 0))
    text_to_screen(screen, "Level Complete!", 235, 380, size=100, color=(255, 255, 255))


    # If "Next Level" is clicked, increase level and reset score
    if level_btn.draw():
        level += 1  # Increase the level
        score = 0   # Reset score for the next level
        game_state = "game"  # Return to game mode
        
        # Adjust settings for the new level
        if level == 1:
            enemy_speed = random.randint(1, 2)
            player_speed = 7
            enemy_count = 1
            bomb_count = 0
            superpower_count = 0

        elif level == 2:
            enemy_speed = random.randint(2, 4)
            player_speed = random.randint(7, 10)
            enemy_count = 1
            bomb_count = 1
            superpower_count = 1

        elif level == 3:
            enemy_speed = random.randint(3, 5)
            player_speed = random.randint(7, 10)
            enemy_count = 2
            bomb_count = 1
            superpower_count = 2

        else:
            enemy_speed = random.randint(int(level)*1.5)
            player_speed = int(level)*2.5
            enemy_count = int(level)-1
            bomb_count = int(level)-2
            superpower_count = int(level)-1



        # Clear previous enemies and bombs
        enemy_group.empty()
        bomb_group.empty()


        # Spawn new enemies and bombs
        for _ in range(enemy_count):
            enemy_x, enemy_y = checking_distance(player.rect.x, player.rect.y)
            enemy = Enemy(cat_img, 0.09, enemy_x, enemy_y, enemy_speed)
            enemy_group.add(enemy)


        for _ in range(bomb_count):
            bomb_x, bomb_y = checking_distance(player.rect.x, player.rect.y)
            bomb = Bomb(bomb_img, 0.09, bomb_x, bomb_y, enemy_speed)
            bomb_group.add(bomb)


        for _ in range(superpower_count):
            superpower = Superpower(superpower_img, 5, 250, 250)
            superpower_group.add(superpower)

    # If "Pause" is clicked, return to the main menu
    if pause_btn.draw():
        game_state = "menu"


    pygame.display.update()










while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    if game_state == "menu":
        menu()


    elif game_state == "game":
        screen.fill((0, 0, 0))  # Clear the screen
        
        # Check if the player should advance to the next level
        if score >= 1:
            game_state = "level"  # Move to level transition screen


        if restart_btn.draw():
            score = 0  # Reset score if the player restarts
            game_state = "game"


        if house_btn.draw():
            game_state = "menu"


        # Check for collisions
        if pygame.sprite.spritecollideany(player, enemy_group):
            print("Collision detected!")
            
            pygame.quit()
            quit()


        if pygame.sprite.spritecollideany(player, bomb_group):
            print("Bomb hit!")
            screen.blit(background, (93, 93))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            quit()


        if pygame.sprite.spritecollideany(player, superpower_group):
            score += 1
            superpower_group.update()


        # Draw everything
        text_to_screen(screen, f"Score: {score}", 5, 5, size=50)
        text_to_screen(screen, f"Level: {level}", 200, 5, size=50)
        
        player_group.draw(screen)
        player_group.update()
        enemy_group.draw(screen)
        enemy_group.update(player)
        bomb_group.draw(screen)
        bomb_group.update(random.choice([1, 2]))
        superpower_group.draw(screen)


        pygame.display.set_caption(f"Score: {score}")


    elif game_state == "level":
        next_level()


    pygame.display.update()
    clock.tick(60)







