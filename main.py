import pygame as py
import random
py.init()
fps = 60
# info = py.display.Info()
# window_size = (info.current_w, info.current_h)
screen = py.display.set_mode((800, 600))
py.display.set_caption("Space Warfare")
icon = py.image.load("C:\\Studies\\Python\\Game\\assets\\icon.png")
py.display.set_icon(icon)
background = py.image.load("C:\\Studies\\Python\\Game\\assets\\background.jpg")
running = True

#player
player_img = py.image.load("C:\\Studies\\Python\\Game\\assets\\player1.png")
player_img = py.transform.scale(player_img, (80, 80))
player_x = 360
player_y = 500
player_x_change = 0

#enemy
enemy_img = py.image.load("C:\\Studies\\Python\\Game\\assets\\enemy.png")
# enemy_img = py.transform.scale(player_img, (50, 50))
enemy_x = random.randint(0,768)
enemy_y = 0
enemy_x_change = 0
enemy_y_change = 0

def enemy(x,y):
    screen.blit(enemy_img,(x,y))
def player(x,y):
    screen.blit(player_img, (x, y))


while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT or event.key == py.K_a:
                player_x_change = -0.25
            if event.key == py.K_RIGHT or event.key == py.K_d:
                player_x_change = 0.25
        if event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_a:
                player_x_change = 0
            if event.key == py.K_RIGHT or event.key == py.K_d:
                player_x_change = 0

    screen.blit(background, (-400, -400))

    #enemy movement
    if enemy_y < 500:
        enemy_y_change = 0.1
        enemy_x_change = random.uniform(-1,1)
    enemy_x += enemy_x_change
    enemy_y += enemy_y_change


    #player movement
    player_x += player_x_change
    if player_x < 0:
        player_x_change =0
    if player_x > 720:
        player_x_change =0

    player(player_x, player_y)
    enemy(enemy_x,enemy_y)
    speed = 0.24
    py.display.update()


py.quit()
