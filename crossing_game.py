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
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)
scoreFont=pygame.font.SysFont('comicsans', 30)
# Create Game class to control flow of game data
class Game: 


	# Frames per second of game
	TICK_RATE = 60
	# score of game
	score = 0 

	def __init__(self, title, image_path, width, height):
		# Class attributes  
		self.title = title
		self.width = width 
		self.height = height
		# Set up game window with specified parameter of width and height 
		self.game_screen = pygame.display.set_mode((self.width, self.height))
		# Set game window color to  white
		self.game_screen.fill(WHITE_COLOR)
		image = pygame.image.load(image_path)
		self.background_image = pygame.transform.scale(image, (self.width, self.height))

	# Method to display score in game
	def displayScore(self):
		text = scoreFont.render("SCORE: " + str(self.score),True, WHITE_COLOR)
		self.game_screen.blit(text,(665, 40))
		#clock.sleep(10)

	# Method containing Main game loop
	def run_game_loop(self,level_speed,score):
		# Boolean variable used to determine how long while loop is ran
		is_game_over = False
		did_win = False
		direction = 0

		# Player object
		player_character = PlayerObject('player.png', 375, 700, 50, 50)
		# Empty array used to store enemy objects
		enemy = []
		# Add enemy objects to array using append method
		enemy.append(EnemyObject('enemy.png', 20, 600, 50, 50))	
		enemy.append(EnemyObject('enemy.png', self.width - 40, 400, 50, 50))
		enemy.append(EnemyObject('enemy.png', 20, 200, 50, 50))
		# Increase enemy[0] speed
		enemy[0].SPEED *= level_speed
		# Increase enemy[1] speed
		enemy[1].SPEED *= level_speed
		# Increase enemy[2] speed
		enemy[2].SPEED *= level_speed

		# Treasure object
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

			# Draw backgroud to game
			self.game_screen.blit(self.background_image, (0, 0))

			# Draw treasure object to game
			treasure.draw(self.game_screen)

			# Draw player character to game
			player_character.draw(self.game_screen)
			# Move player character in game
			player_character.move(direction, self.height)
			
			
			# Draw enemy character to game
			enemy[0].draw(self.game_screen)
			# Move enemy_0 character in game
			enemy[0].move(self.width)

			# Add new enemy when level_sped  reaches 3
			if level_speed > 2:
				# Draw enemy character to game
				enemy[1].draw(self.game_screen)
				# Move enemy_0 character in game
				enemy[1].move(self.width)

			# Add new enemy when level_sped reaches 5
			if level_speed > 4:
				# Draw enemy character to game
				enemy[2].draw(self.game_screen)
				# Move enemy_0 character in game
				enemy[2].move(self.width)





			# End game if collision between enemy and treasure
			if player_character.detect_collision(enemy[0]):
				is_game_over = True
				did_win = False
				text = font.render('You lose! :(',True, BLACK_COLOR)
				self.game_screen.blit(text,(300, 350))
				self.score=0
				pygame.display.update()
				clock.tick(1)
				pygame.time.delay(100)
				break
			elif player_character.detect_collision(enemy[1]):
				is_game_over = True
				did_win = False
				text = font.render('You lose! :(',True, BLACK_COLOR)
				self.game_screen.blit(text,(300, 350))
				self.score=0
				pygame.display.update()
				clock.tick(1)
				pygame.time.delay(100)
				break
			elif player_character.detect_collision(enemy[2]):
				is_game_over = True
				did_win = False
				text = font.render('You lose! :(',True, BLACK_COLOR)
				self.game_screen.blit(text,(300, 350))
				self.score=0
				pygame.display.update()
				clock.tick(1)
				pygame.time.delay(100)
				break
			elif player_character.detect_collision(treasure):
				is_game_over = True
				did_win = True
				text = font.render('You Win! :)',True, BLACK_COLOR)
				self.game_screen.blit(text,(300, 350))
				self.score +=100
				pygame.display.update()
				clock.tick(1)
				pygame.time.delay(100)
				break
			

			# Display score
			self.displayScore()

			# update all game graphics
			pygame.display.update()
			# Update game clock with FPS
			clock.tick(self.TICK_RATE)

		if did_win:
			self.run_game_loop(level_speed + .5, self.score)
		else:
			self.run_game_loop(1, self.score)
			
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

	# Return False (no collision) if y positions and x positions do not overlap
	# Return True x and y overlap
	def detect_collision(self, other_body):
		if self.y_pos > other_body.y_pos + other_body.height:
			return False
		elif self.y_pos + self.height < other_body.y_pos:
			return False

		if self.x_pos > other_body.x_pos + other_body.width:
			return False
		elif self.x_pos + self.width < other_body.x_pos:
			return False

		return True

                # Player character stays inbound of game window boundary 
		if self.y_pos > max_height - 40:
			self.y_pos = max_height - 40

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

pygame.init()
new_game = Game(SCREEN_TITLE, 'background.png', SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1,0)

# Exit pygame console
pygame.quit()
# Exit out of program
quit()
