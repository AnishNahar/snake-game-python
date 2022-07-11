import pygame
import random

pygame.init()

c1 = (255,255,255)
c2 = (0,255,0)
c3 = (255,0,0)
c4 = (0,0,255)

w , h = 1000,700

display = pygame.display.set_mode((w, h))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

s_size = 10
s_sipeed = 10

message_font = pygame.font.SysFont('Arial', 20)
score_font = pygame.font.SysFont('Arial' , 20)

def print_score(score):
    text = score_font.render("score: " + str(score) , True , c4)
    display.blit(text,[0,0])

def display_snake(s_size , pix):
    for pixel in pix:
        pygame.draw.rect(display , c1 , [pixel[0] , pixel[1] , s_size , s_size])

def game():
    game_over = False
    game_close = False
    
    x = w / 2
    y = h / 2

    x_speed = 0
    y_speed = 0

    pix = []
    snake_length = 1
    
    target_x = round(random.randrange(0,w - s_size)/10.0)*10.
    target_y = round(random.randrange(0,h - s_size)/10.0)*10.

    while not game_over:
        while game_close:
            display.fill(c2)
            final_msg = message_font.render('GAME OVER!!!', True , c3)
            display.blit( final_msg , [w/3,h/3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.QUIT:
                        game_over = True
                        game_close = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = - s_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed =  s_size
                    y_speed = 0                    
                if event.key == pygame.K_UP:
                    x_speed =  0
                    y_speed = -s_size  
                if event.key == pygame.K_DOWN:
                    x_speed =  0
                    y_speed = s_size  
        if x>= w or x<0 or y>= h or y<0:
            game_close = True

        

        x += x_speed
        y += y_speed

        display.fill(c2)
        pygame.draw.rect(display,c4,[target_x,target_y , s_size,s_size])

        pix.append([x,y])
        

        if len(pix) > snake_length:
            del pix[0]

        for pixel in pix[:-1]:
            if pixel == [x,y]:
                game_close = True
        
        display_snake(s_size,pix)
        print_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0,w - s_size)/10.0)*10.
            target_y = round(random.randrange(0,h - s_size)/10.0)*10.
            snake_length += 1
        
        if (snake_length) < 5:
            snake_speed=15
            clock.tick(snake_speed)
        else:
            snake_speed = 20
            clock.tick(snake_speed)
    pygame.quit()
    quit()

game()
