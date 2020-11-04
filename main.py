# Inactive Pong Game



# MODULES
import pygame
from ball import Ball 		# From ball file, import item 'Ball'.
from paddle import Paddle 	# From paddle file, import item 'Paddle'.



# INITIALIZE
pygame.init()
WIN_X, WIN_Y = 800, 400
window = pygame.display.set_mode((WIN_X, WIN_Y))
clock = pygame.time.Clock()
run = True
FPS = 60



# COLORS
WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)
L_GRAY = (175, 175, 175)



# INITIALIZE OBJECTS
ball = Ball(window, WHITE, 400, 200, 10, 10)
p1   = Paddle(window, WHITE,  25, 175, 10, 50)
p2   = Paddle(window, WHITE, 775, 175, 10, 50)


# MAIN LOOP
while run:

	window.fill(0) 		# Background: BLACK

	# BOUNDARIES: Top / Bottom
	pygame.draw.rect(window, L_GRAY, (0,     0, WIN_X, 10))
	pygame.draw.rect(window, L_GRAY, (0, WIN_Y - 10, WIN_X, 10))


	# EACH EVENT
	for event in pygame.event.get():

		# IF WINDOW EXIT
		if event.type == pygame.QUIT:
			run = False


	# DRAW OBJECTS
	ball.drawBall()
	p1.drawPaddle()
	p2.drawPaddle()




	# UPDATE WINDOW
	pygame.display.update()

# IF MAIN LOOP == FALSE, QUIT.
pygame.quit()
