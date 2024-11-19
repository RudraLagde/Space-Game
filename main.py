import pygame as py
import random
import math
from pygame import mixer
py.init()
fps = 60
screen = py.display.set_mode((800, 600))
py.display.set_caption("Space Warfare")
icon = py.image.load("assets\\icon.png")
py.display.set_icon(icon)
background = py.image.load("assets\\background.jpg")
mixer.music.load("assets\\background.wav")
mixer.music.play(-1)
running = True


#score
score_value = 0
font = py.font.Font("assets\\ARCADE_I.TTF", 32)
text_y = 10
text_x = 10

#player
player_img = py.image.load("assets\\player1.png")
player_img = py.transform.scale(player_img, (80, 80))
player_x = 360
player_y = 500
player_x_change = 0

#enemy
enemy_img = py.image.load("assets\\enemy.png")
num_of_enemies = 5
enemy_img_list = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

for i in range(num_of_enemies):
    enemy_img_list.append(py.image.load("assets\\enemy.png"))
    enemy_x.append(random.randint(0, 768))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(0.1)
    enemy_y_change.append(0.05)

#bullet
bullet_img = py.image.load("assets\\bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 0.5
bullet_state = "ready"


def show_score(x,y):
    score = font.render("SCORE:"+ str(score_value), True , (255,255,255) )
    screen.blit(score,(x,y))
def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img,(x+25,y+10))

def enemy(x,y,i):
    screen.blit(enemy_img_list[i],(x,y))
def player(x,y):
    screen.blit(player_img, (x, y))

def collision(enemy_x, enemy_y , bullet_x , bullet_y):
    distance = math.sqrt(math.pow(enemy_x-bullet_x,2) + math.pow(enemy_y-bullet_y, 2))
    return distance <27


while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT or event.key == py.K_a:
                player_x_change = -0.5
            if event.key == py.K_RIGHT or event.key == py.K_d:
                player_x_change = 0.5
            if event.key == py.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("assets\\laser.wav")
                    bullet_sound.play()
                    bullet_x = player_x
                    bullet_y = player_y
                    bullet(bullet_x , bullet_y)
        if event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_a:
                player_x_change = 0
            if event.key == py.K_RIGHT or event.key == py.K_d:
                player_x_change = 0

    screen.blit(background, (-400, -400))

    #enemy movement
    for i in range(num_of_enemies):
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= 736:  # Reverse direction at edges
            enemy_x_change[i] = -enemy_x_change[i]
        enemy_y[i] += enemy_y_change[i]  # Always move downward
        if enemy_y[i] >= 600:  # Reset position when reaching the bottom
            enemy_y[i] = random.randint(50, 150)
            enemy_x[i] = random.randint(0, 736)

        # Collision detection
        is_collision = collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)

        if is_collision:
            collision_sound = mixer.Sound("assets\\explosion.wav")
            collision_sound.play()
            bullet_y = 500
            bullet_state = "ready"
            score_value += 1

            enemy_x[i] = random.randint(0, 768)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    #player movement
    player_x += player_x_change
    if player_x < 0:
        player_x_change =0
    if player_x > 720:
        player_x_change =0

    if bullet_state == "fire":
        bullet(bullet_x,bullet_y)
        bullet_y -= bullet_y_change
        if bullet_y <= 0:
            bullet_y = 500
            bullet_state = "ready"


    player(player_x, player_y)
    show_score(text_x,text_y)
    py.display.update()


py.quit()
