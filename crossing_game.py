# Import pygame to gain access to library 
import pygame 

# Set screen title for game
SCREEN_TITLE = 'Crossing Game'
# Set screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# Set color white with RBG code
WHITE_COLOR = (255, 255, 255)
# Set color black with RBG code
BLACK_COLOR = (0, 0 , 0)

# Create a clock object from the pygame time module
clock = pygame.time.Clock()

# Create game class to control flow of game data
class game:

	# TICK_RATE, variable initialized with amount of frames to be displayed 
	# per second (FPS - Frames Per Second)
	TICK_RATE = 60
	# Initializer of game class , taking in title, width, and height parameters
	def __init__(self, title, width, height):
		# Class attributes  
		self.title = title
		self.width = width 
		self.height = height
		# Set up game window, takes class attribute of width and height as parameter
		self.game_screen = pygame.display.set_mode((self.width, self.height))
		# Set game window to the RBG color of white
		self.game_screen.fill(WHITE_COLOR)

# Exit pygame console
pygame.quit()
# Exit out of program
quit()
