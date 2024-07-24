from snake_core import *

snake = [(x, 1) for x in range(5, 10)]
direction = (1, 0)
food = random_food(snake)
key = "" 
score = 0

while key != "q":
	# Key inputs
	key = getch(timeout=0.1)
	if key == "d" and direction[0] == 0:
		here
	#
	elif key == "a" and direction[0] == 0:
		here
	#
	elif key == "s" and direction[1] == 0:
		here
	#
	elif key == "w" and direction[1] == 0:
		here
	#
	# Lengthen snake
	add_element_to_snake(snake, direction)
	# Check if bit itself
	if snake[-1] in snake[0:-1]:
		here
	#
	# Check for food
	if (snake[-1] != food):
		here
	#
	else:
		# Food, don't shorten snake and increase score
		food = random_food(snake)
		score = score + 1
	#
	# Draw snake and print score
	draw_snake(snake, food)
	print("Score:", score)
#

# TODO: highscore table!

