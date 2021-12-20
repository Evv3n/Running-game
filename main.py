import pygame as pg
from sprites import *


pg.init()
pg.font.init()



WIDTH = 800
HEIGHT = 600

MIDDLE = (WIDTH/2, HEIGHT/2)

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED= (255,0,0)
 
ting_pos_x = 400
ting_pos_y = 400
 
ting_size_x = 20
ting_size_y = 20
 
speed = 5
 
direction_x = speed
direction_y = -speed
#textfont
comic_sans30 = pg.font.SysFont("MonoLisa", 30) 

screen = pg.display.set_mode((WIDTH,HEIGHT))
 
clock = pg.time.Clock()
FPS = 120
 
all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
ninja = Enemy()
all_sprites.add(ninja)
enemies.add(ninja)
player = Player()
all_sprites.add(player)

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()
 
    # tegner ting til skjerm på valgt posisjon, og størrelse
    screen.fill((30,30,30))
    #oppdaterer alle sprites
    all_sprites.update()

    #check for collision
    hits = pg.sprite.spritecollide(player, enemies, True)
    if hits:
        player.kills += 1

    while len(enemies) < 1:
        ninja = Enemy()
        all_sprites.add(ninja)
        enemies.add(ninja)
        
    #text    
    
    all_sprites.draw(screen) 


    
    text_player_kills = comic_sans30.render(str(player.kills) + " Kills", False, (BLUE))
    
    screen.blit(text_player_kills, (10, 10))


    pg.display.update()
 
