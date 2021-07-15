import pygame
pygame.init ()
dis=pygame.display.set_mode ((400,300))
pygame.display.update ()
pygame.display.set_caption('Test pygame')
game_over=False
#Snake color

blue=(0,0,255)
red=(255,0,0)

#Move var
a1 = 300
b1 = 300

a1_change = 0
b1_change = 0

#This loop is needed to keep the screen running
#while not game_over:
#	for event in pygame.event.get():
#		print(event) #show action on the screen

clock = pygame.time.Clock()
#Loop where you can actually quit the game
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		if event.TYPE == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
			a1_change = -10
			b1_change = 0
		elif event.key == pygame.K_RIGHT:
			a1_change = 10
			b1_change = 0
		elif event.key == pygame.K_UP:
			a1_change = -10
			b1_change = 0
		elif event.key == pygame.K_DOWN:
			a1_change = 10
			b1_change = 0
	a1 += a1_change
	b1 += b1_change
	pygame.draw.rect(dis, black, [a1, b1, 10, 10])
	pygame.display.update()
	clock.tick(30)

#Rectangle draw
	pygame.draw.rect(dis,blue,[200,150,10,10])
	pygame.display.update()
pygame.quit ()
quit ()