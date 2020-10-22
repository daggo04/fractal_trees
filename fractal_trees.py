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

def blank():
	clearscreen()
	tracer(0,0)

def draw_tree(sz=80, level=7, angle=30, posx=0, posy=0, rotation=-90):
	new_pen = Turtle()
	new_pen.speed(0)
	new_pen.right(rotation)
	new_pen.penup()
	new_pen.goto(posx, posy)
	new_pen.pendown()
	new_pen.width(5)
	y(sz, level, angle, new_pen)
	hideturtle()
	update()
	
def draw_forest(n):
	for tree in range(n):
		x = random.randint(-300, 300)
		y = random.randint(-450, 300)
		sz = random.randint(20, 100)
		level = random.randint(5, 12)
		angle = random.randint(15, 45)
		draw_tree(sz=sz, level=level, angle=angle, posx=x, posy=y)

def y(sz, level, angle, new_pen):
	if level > 0:
		colormode(255)
		# splitting the rgb range for green 
        # into equal intervals for each level 
        # setting the colour according 
        # to the current level 
		new_pen.pencolor(100 ,255//level, 30)
		# drawing the base
		new_pen.forward(sz)
		new_pen.right(angle)
		# recursive call for 
        # the right subtree 
		y(0.8 * sz, level-1, angle, new_pen)
		new_pen.pencolor(100, 255//level, 30) 
		new_pen.left( 2 * angle ) 
		# recursive call for 
		# the left subtree 
		y(0.8 * sz, level-1, angle, new_pen)
		new_pen.pencolor(100, 255//level, 30) 
		new_pen.right(angle) 
		new_pen.forward(-sz)


def cardinal_dir(size, level, angle):
	draw_tree(sz=size, level=level, angle=angle)
	draw_tree(sz=size, level=level, angle=angle, rotation=90)
	draw_tree(sz=size, level=level, angle=angle, rotation=0)
	draw_tree(sz=size, level=level, angle=angle, rotation=180)













