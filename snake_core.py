
from random import randint
import tty, sys, termios, os
import select

height = 20
width = 40

def setup_term(fd, when=termios.TCSAFLUSH):
	mode = termios.tcgetattr(fd)
	mode[tty.LFLAG] = mode[tty.LFLAG] & ~(termios.ECHO | termios.ICANON)
	termios.tcsetattr(fd, when, mode)
#

def getch(timeout=None):
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		setup_term(fd)
		try:
			rw, wl, xl = select.select([fd], [], [], timeout)
		except select.error:
			return
		#
		if rw:
			return sys.stdin.read(1)
		#
	#
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	#
#

def draw_snake(snake, food):
	global width, height
	print("\033c", end="")
	for j in range(height):
		for i in range(width):
			if (i, j) in snake:
				print("O", end="")
			#
			else:
				if (i, j) == food:
					print("x", end="")
				#
				else:
					print(" ", end="")
				#
			#
		print("|")
	#
	print(width * "_" + "/")
#

def add_element_to_snake(snake, direction):
	global width, height
	snake.append(
		(
			(snake[-1][0] + direction[0]) % width,
			(snake[-1][1] + direction[1]) % height
		)
	)
	return snake
#

def random_food(snake):
	global width, height
	food = snake[-1]
	while food in snake:
		food = (randint(0, width-1), randint(0, height-1))
	return food
#


