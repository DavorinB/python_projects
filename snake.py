import pygame
pygame.init ()
dis=pygame.display.set_mode ((400,300))
pygame.display.update ()
pygame.display.set_caption('Test pygame')
game_over=False
#Snake color

blue=(0,0,255)
red=(255,0,0)

#This loop is needed to keep the screen running
#while not game_over:
#	for event in pygame.event.get():
#		print(event) #show action on the screen

#Loop where you can actually quit the game
while not game_over:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			game_over=True
#Rectangle draw
	pygame.draw.rect(dis,blue,[200,150,10,10])
	pygame.display.update()			
pygame.quit ()
quit ()