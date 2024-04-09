import pgzrun
import sys
import os
from random import randint

TITLE = "Space Chase"

WIDTH = 700
HEIGHT = 600
score = 0
gameover = False

plr1 = Actor("plr1")
plr1.pos=(100,100)

plr2 = Actor("plr2")
plr2.pos=(200,200)

star = Actor("star")
star.pos=(500,500)

def draw():
    screen.blit("bg",(0,0))
    screen.draw.text("Score: "+str(score),color="red",topleft=(10,10))
    plr1.draw()
    plr2.draw()
    star.draw()

    if gameover:
        screen.fill("purple")
        screen.draw.text("You Lost! Your final score was "+str(score),midtop=(WIDTH/4,20),fontsize=40,color="yellow")

def move_star():
    global score
    star.x=randint(70,(WIDTH-70))
    star.y=randint(70,(HEIGHT-70))

def update():
    global score
    if keyboard.left:
        plr1.x -= 2
    if keyboard.right:
        plr1.x += 2
    if keyboard.up:
        plr1.y -= 2
    if keyboard.down:
        plr1.y += 2


    if keyboard.w:
        plr2.y -= 2
    if keyboard.s:
        plr2.y += 2
    if keyboard.a:
        plr2.x -= 2
    if keyboard.d:
        plr2.x += 2

    plr2score = plr2.colliderect(star)
    if plr2score:
        score += 1
        move_star()

    if plr1.colliderect(plr2):
        gameover = True
        print(gameover)

pgzrun.go()