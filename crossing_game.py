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
	# Initializer for game class , taking in title, width, and height parameters
	def __init__(self, title, width, height):
		# Class attributes  
		self.title = title
		self.width = width 
		self.height = height
		# Set up game window with specified parameter of width and height 
		self.game_screen = pygame.display.set_mode((self.width, self.height))
		# Set game window color to  white
		self.game_screen.fill(WHITE_COLOR)

	# Function containing Main game loop
	def run_game_loop(self):
		# Boolean variable used to determine how long while loop is ran
		is_game_over = False

		# Main game loop used to control gameplay such as events, object control etc
		while not is_game_over:
			#  for-loop to get any events that occur in game
		 	for event in pygame.event.get():
		 		if event.type == pygame.QUIT:
		 			is_game_over = True
		 		print(event)

		 	# update all game graphics
			pygame.display.update()
			# Update game clock with FPS
			clock.tick(self.TICK_RATE)


# Exit pygame console
pygame.quit()
# Exit out of program
quit()
