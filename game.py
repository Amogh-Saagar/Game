import pygame

pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')


moving_left = 0
moving_right = 0

clock = pygame.time.Clock()
clock.tick(60)

class Soldier(pygame.sprite.Sprite):
	def __init__(self, x, y, scale, speed):
		pygame.sprite.Sprite.__init__(self)
		self.speed = speed
		self.animation_list = [ ]
		self.index = 1
		self.update_time = pygame.time.get_ticks()
		self.flip = False
		for i in range(3):
			img = pygame.image.load(f'assets/{i}.png')
			img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
			self.animation_list.append(img)
		self.image = self.animation_list[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		
		
	def update_animation(self):
	
		self.image = self.animation_list[self.index]
		if pygame.time.get_ticks() - self.update_time > 200:
			self.update_time = pygame.time.get_ticks()
			self.index += 1
			if self.index >= len(self.animation_list):
				self.index = 0

	def move(self, moving_left, moving_right):
		dx = 0
		dy = 0
		
		if moving_left:
			dx = -self.speed
			self.flip = True
		
		if moving_right:
			self.flip = False
			dx = self.speed
			
		self.rect.x += dx
		self.rect.y += dy
		
	def draw(self):
		screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
		

player = Soldier(100, 100, 1, 1)



run = True
while run:
	screen.fill("black")
	player.draw()
	player.move(moving_left, moving_right)
	player.update_animation()
	for event in pygame.event.get():
        #quit game
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				moving_left = 1

			if event.key == pygame.K_d:
				moving_right = 1
			
			if event.key == pygame.K_ESCAPE:
				run = 0
		if event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					moving_left = 0

				if event.key == pygame.K_d:
					moving_right = 0			

	
	pygame.display.update()

pygame.quit()