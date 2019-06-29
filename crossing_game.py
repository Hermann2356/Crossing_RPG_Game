# import pygame to gain access to library
import pygame

# Set screen title for game
SCREEN_TITLE = 'Crossy RPG'
# Set screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# Set color white with RGB
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Create a clock object from the pygame time module
clock = pygame.time.Clock()

# Create Game class to control flow of game data
class Game: 

	# Frames per second of game
	TICK_RATE = 60

	def __init__(self, title, width, height):
		# Class attributes  
		self.title = title
		self.width = width 
		self.height = height
		# Set up game window with specified parameter of width and height 
		self.game_screen = pygame.display.set_mode((self.width, self.height))
		# Set game window color to  white
		self.game_screen.fill(WHITE_COLOR)

	# Method containing Main game loop
	def run_game_loop(self):
		# Boolean variable used to determine how long while loop is ran
		is_game_over = False
		direction = 0

		player_character = PlayerObject('player.png', 375, 700, 50, 50)
		enemy_0 = EnemyObject('enemy.png', 20, 400, 50, 50)	
		treasure = GameObject('treasure.png', 375, 50, 50, 50)

		# Main game loop used to control gameplay such as events, object control etc
		while not is_game_over:

			# loop get all events in game
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						direction = 1
					elif event.key == pygame.K_DOWN:
						direction = -1
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						direction = 0
				print(event)


			# Change screen blank after every frame change
			self.game_screen.fill(WHITE_COLOR)

			# Draw player character to game
			player_character.draw(self.game_screen)
			# Move player character in game
			player_character.move(direction, self.height)

			# Draw enemy character to game
			enemy_0.draw(self.game_screen)
			# Move enemy_0 character in game
			enemy_0.move(self.width)

			# update all game graphics
			pygame.display.update()
			# Update game clock with FPS
			clock.tick(self.TICK_RATE)

			if player_character.detect_collision(enemy_0):
				is_game_over = True
			elif player_character.detect_collision(treasure):
				is_game_over = True

# GameObject class base class of subclasses player and enemy objects
class GameObject:

	# Initializer taking image_path, (x, y) positions, and (width, height) 
	def __init__(self, image_path, x, y, width, height):
		# Create image object for  object image
		object_image = pygame.image.load(image_path)
		# Scale object_image to desire size and initialize into image variable
		self.image = pygame.transform.scale(object_image, (width, height))
		# x and y position of game object in game
		self.x_pos = x
		self.y_pos = y
		# Width and height of game object
		self.width = width
		self.height = height

	# Draw method to display image in game
	def draw(self, background):
		background.blit(self.image, (self.x_pos, self.y_pos))

# Class represents player character in game 
class PlayerObject(GameObject):

	# Speed of player character  
	SPEED = 10

	# Initialize sub class and super class
	def __init__(self, image_path, x, y, width, height):
		super().__init__(image_path, x, y, width, height)

	# Move method will move player character up if direction is > 0 
	# or will move player down if direction is < 0
	def move(self, direction, max_height):
		if direction > 0:
			self.y_pos -= self.SPEED
		elif direction < 0:
			self.y_pos += self.SPEED

		# Player character stays inbound of game window boundary 
		if self.y_pos > max_height - 40:
			self.y_pos = max_height - 40

	def detect_collision(self, object_body):
		if self.y_pos > object_body.y_pos + object_body.height:
			return False
		elif self.y_pos + self.height < object_body.y_pos:
			return False

		if self.x_pos > object_body.x_pos + object_body.width:
			return False
		elif self.x_pos + self.width < object_body.x_pos:
			return False

		return True

# Class represents enemy character in game 
class EnemyObject(GameObject):

	# Speed of enemy character
	SPEED = 10

	# Initialize sub class and super class
	def __init__(self, image_path, x, y, width, height):
		super().__init__(image_path, x, y, width, height)

	# Move method will move enemy character left if enemy.x_pos is <= 20 
	# or will move enemy right if enemy.x_pos is >= max_width(of screen) - 40
	def move(self, max_width):
		if self.x_pos <= 20:
			self.SPEED = abs(self.SPEED)
		elif self.x_pos >= max_width - 40:
			self.SPEED = -abs(self.SPEED)
		self.x_pos += self.SPEED

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

# Exit pygame console
pygame.quit()
# Exit out of program
quit()
