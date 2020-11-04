# Ball class for the game Pong.

# MODULES
import pygame



class Ball:

	# INITIALIZE
	def __init__(self, window, color, x, y, radius, velocity):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.radius = radius
		self.velocity = velocity

	# DRAW BALL
	def drawBall(self):
		pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)
