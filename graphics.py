import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("neighbourhood")

greg=turtle.Turtle()
greg.speed(0)

def square(size, alternate, color):
	greg.color(color)
	greg.begin_fill()
	for i in range(4):
		greg.fd(size)
		greg.lt(90)
	greg.end_fill()
	greg.fd(size)

def row(size, alternate, color1, color2):
	for i in range(4):
		if (alternate==True):
			square(size, alternate,color1)
			square(size, alternate,color2)
		else:
			square(size, alternate,color2)
			square(size, alternate,color1)

def board(size, alternate, color1, color2):
	greg.pu()
	greg.goto(-(size * 4), (size*4))
	for i in range(8):
		row(size, alternate, color1, color2)
		greg.bk(size*8)
		greg.rt(90)
		greg.fd(size)
		greg.lt(90)
		if (alternate==True):
			alternate = False
		else:
			alternate = True

board(50, True, "green", "red")


