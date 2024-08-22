import pygame
import sys


pygame.init()



screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Ping pong!")

start_pos_leftHand = [750,250]
end_pos_leftHand = [750,350]
start_pos_rightHand = [50,250]
end_pos_rightHand =[50,350]
velocity = 7

ball_x = screen_width // 2 
ball_y = screen_height // 2 

ball_radius = 20

x_velocity =5
y_velocity =5






def draw_hands ():
    pygame.draw.line(screen,(249,222,167),start_pos_leftHand ,end_pos_leftHand , 5)
    pygame.draw.line(screen,(249,222,167), start_pos_rightHand ,end_pos_rightHand , 5)
    

def ball_bounce():
    global x_velocity, y_velocity, ball_x, ball_y
    
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        y_velocity = -y_velocity
    
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_x = screen_width // 2
        ball_y = screen_height // 2
    
    if (ball_x + ball_radius >= start_pos_leftHand[0] and 
        ball_y >= start_pos_leftHand[1] and ball_y <= end_pos_leftHand[1]):
        x_velocity = -abs(x_velocity)  
    
    if (ball_x - ball_radius <= start_pos_rightHand[0] + 5 and 
        ball_y >= start_pos_rightHand[1] and ball_y <= end_pos_rightHand[1]):
        x_velocity = abs(x_velocity)
    


run =True 
while run :
    screen.fill((37, 150, 190))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
    keys= pygame.key.get_pressed()  
             
    if keys[pygame.K_KP_8] and start_pos_leftHand[1]>=0:
                start_pos_leftHand[1] -= velocity
                end_pos_leftHand[1] -= velocity
    if keys[pygame.K_KP_2] and end_pos_leftHand[1]<=600:
                start_pos_leftHand[1] += velocity
                end_pos_leftHand[1] += velocity
    if keys[pygame.K_z] and start_pos_rightHand[1]>=0:
                start_pos_rightHand[1] -= velocity
                end_pos_rightHand[1] -= velocity
    if keys[pygame.K_s] and end_pos_rightHand[1]<=600:
                start_pos_rightHand[1] += velocity
                end_pos_rightHand[1] += velocity
    ball_x += x_velocity            
    ball_y += y_velocity
    draw_hands()
    ball_bounce()
    pygame.draw.circle(screen,(0,0,0),(int(ball_x),int(ball_y)),ball_radius)
    pygame.display.flip()    
    pygame.time.Clock().tick(60)  


