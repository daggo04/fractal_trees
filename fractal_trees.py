# fractal_trees.py
#
#AUTH: DAGOBH
#DATE: 22.10.20

from turtle import *
import random

# Screen setup
bgcolor("white")
setup(width=1200, height=1000)
tracer(0,0)

def blank(): # Removes currently drawn objects
	clearscreen()
	tracer(0,0)

# Draw a singular Y tree using the y function defined furter below
def draw_tree(sz=80, level=7, angle=30, posx=0, posy=0, rotation=-90):
	new_pen = Turtle() # Defining new pen
	new_pen.speed(0)
	new_pen.right(rotation) # Starting orinentation, up by default.
	new_pen.penup() # Lifting pen while changing pos
	new_pen.goto(posx, posy) # Chaning pos
	new_pen.pendown() #Putting pen back down
	new_pen.width(5) #Pen witdth
	y(sz, level, angle, new_pen) # Calling function y
	hideturtle() # Hiding pen after tree is drawn
	update() # Updating screen

# Draw several(n) random trees in random positions	
def draw_forest(n):
	for tree in range(n):
		x = random.randint(-300, 300) # Random horisontal start position
		y = random.randint(-450, 300) # Random vertical start position
		sz = random.randint(20, 100) # Random size
		level = random.randint(5, 12) # Random recursions
		angle = random.randint(15, 45)	#Random angle
		draw_tree(sz=sz, level=level, angle=angle, posx=x, posy=y)

# Takes an inital length(sz), how many recursions(level), 
# and angle relative to starting pos(angle).
def y(sz, level, angle, new_pen):
	if level > 0:
		colormode(255)#Change to rgb color mode

		#Setting color according to current level
		new_pen.pencolor(100 ,255//level, 30)
		
		new_pen.forward(sz)
		new_pen.right(angle)
		# Recursive call for right subtree
		y(0.8 * sz, level-1, angle, new_pen)

		new_pen.pencolor(100, 255//level, 30) 
		new_pen.left( 2 * angle )

		#Recursive call for left subtree.
		y(0.8 * sz, level-1, angle, new_pen)

		new_pen.pencolor(100, 255//level, 30)
		new_pen.right(angle) 
		new_pen.forward(-sz)


#Draw one tree in each direction (left, right, up, down)
def cardinal_dir(size, level, angle):
	draw_tree(sz=size, level=level, angle=angle)
	draw_tree(sz=size, level=level, angle=angle, rotation=90)
	draw_tree(sz=size, level=level, angle=angle, rotation=0)
	draw_tree(sz=size, level=level, angle=angle, rotation=180)













