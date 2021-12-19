import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = text_font.render(f'Score:{current_time}',True,'Black')
    score_rect = score_surf.get_rect(center = (245,20))
    screen.blit(score_surf,score_rect)


pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Leaf Adventure')
clock = pygame.time.Clock()
sky = pygame.image.load('more/1.JPG').convert_alpha()
ground = pygame.image.load('more/ground.PNG').convert_alpha()
enemy = pygame.image.load('more/Snail_s.PNG').convert_alpha()
player = pygame.image.load('more/leaf.PNG').convert_alpha()
player_rect = player.get_rect(topleft = (5,250))
text_font = pygame.font.Font(None, 50)
enemy_rect = enemy.get_rect(topright = (600,300))
player_gravity = 0
game_active = False
dead_screen = pygame.image.load('more/Dead screen.JPG').convert_alpha()
text_2 = text_font.render('Leaf Adventure', True, 'Black')
text_3 = text_font.render('Press space to jump ',True, 'Black')
text_4 = text_font.render('Press backspace to start',True, 'Black')
start_time = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                game_active = True
                enemy_rect.right = 600
                start_time = int(pygame.time.get_ticks() / 1000)


            
    if game_active:
        screen.blit(sky,(-50,0))
        screen.blit(ground,(0,400))
        display_score()
        enemy_rect.x -= 1
        if enemy_rect.right <= -50: enemy_rect.left = 500
        screen.blit(enemy,enemy_rect)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 450: player_rect.bottom = 450
        screen.blit(player,player_rect)
        #screen.blit(text,(180,10))
        if player_rect.colliderect(enemy_rect):
            game_active = False
    else:
        screen.blit(dead_screen,(-530,0))
        screen.blit(text_2,(120,10))
        screen.blit(text_3,(80,250))
        screen.blit(player,(157,40))
        screen.blit(text_4,(50,400))
            
            

        


    pygame.display.update()
    clock.tick(60)




       
    

           
        
    
                       
                       
                

   

