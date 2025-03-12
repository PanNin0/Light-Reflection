# -----------------------------

# Ray Reflecting v1.0
# By - PanNino (Hey check out my other projects on github!)

# -----------------------------

# Modules

import time as t
import random as rnd
import math as m
import turtle as tr
from settings import config

# -----------------------------

# Functions and Variables

    # Variables

tr.tracer(0) # This is used so objects can be drawn instantly rather than having to be drawn out slowly

global circleTr
circleTr = tr.Turtle() # Creates a new turtle that will handle circle drawing

# Stylizing this turtle (this can be edited in settings.py).
circleTr.color(config.lineColor)
circleTr.pensize(config.lineThickness)
circleTr.penup()
circleTr.hideturtle()

global rayTr
rayTr = [] # This list is used to hand the drawing of rays

global rayCollide
rayCollide = [] # List for handling if a ray has collision

wn = tr.Screen() # This handles the window the program takes place on

# This variable handles how close the program is to spawning a new ray, it will be set back down to 0 once it spawns 
# a new ray but it starts higher up so the first ray will take less time to spawn.
countup = round(config.fps * (50 / config.spawnSpeed))

# The number countup must reach before it will spawn a new ray.
threshold = round(config.fps * (100 / config.spawnSpeed))

# How many rays the program has spawned so far. The program will end once it reaches a set threshold
raysSpawned = 0

    # Functions

# drawCircle()

# This function is used to as evident by the function name, draw the circle in the center.

def drawCircle(radius):

    circleTr.goto(0, radius * -1) # Radius has to be negative or else the circle won't be drawn around the origin

    # This all handles the actual drawing of the circle
    circleTr.pendown()
    circleTr.circle(radius)
    circleTr.penup()

# spawnRay()

# This function spawns a new ray into the program at a semirandom point with a semirandom direction

def spawnRay(arc):

    # Spawning variable set up
    
    rayCollide.append(True)

    # Spawning and stylizing the newly spawned ray
    rayTr.append(tr.Turtle()) # Adds a new ray to the ray list
    newRayPos = len(rayTr) - 1 # The position in the ray list that the newest ray is

    rayTr[newRayPos].penup()
    rayTr[newRayPos].color(config.lineColor)
    rayTr[newRayPos].pensize(config.lineThickness)

    # Logic for ray spawn pos and rotation

    spawnRotation = 90 + rnd.randint(0, config.spawningArc) + config.spawnRotation

    rayTr[newRayPos].goto(0, -400) # Goes below the circle so the position can be rotated
    rayTr[newRayPos].circle(400, spawnRotation) # Rotate the spawn position

    currentPos = [rayTr[newRayPos].xcor(), rayTr[newRayPos].ycor()] # Sets up a vector for the x and y cord of the ray
    hyp = m.sqrt((currentPos[0] * currentPos[0]) + (currentPos[1] * currentPos[1])) # Find the hypoteneuse of the ray pos

    if currentPos[0] < 0:
        rotation = m.asin((-1 * currentPos[1]) / hyp)
    else:
        rotation = m.asin(currentPos[1] / hyp) + m.pi
    
    rotation = (rotation * (180 / m.pi)) + (rnd.randint(-80, 80) / 10)

    rayTr[newRayPos].setheading(rotation)

# moveRays()

# Moves all currently existing rays by one movement

def moveRays():

    for ray in range(len(rayTr)):

        # Finding hypoteneuse
        x = rayTr[ray].xcor()
        y = rayTr[ray].ycor()
        hyp = m.sqrt((x*x) + (y*y))

        if hyp <= 600:
            rayTr[ray].pendown()
            rayTr[ray].forward(config.velocity / config.fps)
            rayTr[ray].penup()

            # Reflecting rays

            if (hyp <= config.radius) & (rayCollide[ray] == True): # Checks if the ray is touching the center circle
                
                theta1 = rayTr[ray].heading()
                theta2 = m.asin(y / hyp) * (180 / m.pi)
                theta2 -= 90
                
                if y >= 0:
                    theta3 = (2 * theta2) - theta1
                elif x < 0:
                    theta3 = (-2 * theta2) - theta1
                else:
                    theta3 = 360 - ((2 * theta2) - theta1) * -1
                
                rayTr[ray].setheading(theta3)
                rayCollide[ray] = False

# -----------------------------

# Logic

circleTr.speed(0)

drawCircle(config.radius) # Draw out the circle

while (raysSpawned < config.rays) | len(rayTr) > 0:

    moveRays()

    countup += 1

    if (countup >= threshold) & (raysSpawned < config.rays):

        spawnRay(config.spawningArc) # Spawn a new ray

        # All the code below hands incrementing variables and notifying the user a ray spawned.

        countup = 0
        raysSpawned += 1
        print('Ray successfully spawned! (' + str(raysSpawned) + '/' + str(config.rays) + ')')

    tr.update() # Updates the screen
    t.sleep(1 / config.fps) # This gives the program a pseudo fps. This can be changed in settings.py.

# -----------------------------

print('Program ended.')
wn.mainloop() # Stops the program from closing