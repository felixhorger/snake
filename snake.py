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
		direction = (1, 0)
	#
	elif key == "a" and direction[0] == 0:
		direction = (-1, 0)
	#
	elif key == "s" and direction[1] == 0:
		direction = (0, 1)
	#
	elif key == "w" and direction[1] == 0:
		direction = (0, -1)	
	#
	# Lengthen snake
	add_element_to_snake(snake, direction)
	# Check if bit itself
	if snake[-1] in snake[0:-1]:
		print("GAME OVER!") 
		exit()
	#
	# Check for food
	if (snake[-1] != food):
		snake.pop(0) # No food, shorten snake
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

