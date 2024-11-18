import pygame as py

py.init()
# info = py.display.Info()
# window_size = (info.current_w, info.current_h)
screen = py.display.set_mode((800,600))
py.display.set_caption("Space Warfare")
icon = py.image.load("C:\\Studies\\Python\\Game\\assets\\icon.png")
py.display.set_icon(icon)
running = True

#player
playerimg = py.image.load("C:\\Studies\\Python\\Game\\assets\\player1.png")
playerx = 400
playery = 300

def player():
    screen.blit(playerimg,(playerx,playery))
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.fill((123,123,123))
    player()
    py.display.update()

py.quit()
