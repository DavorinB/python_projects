import pygame
pygame.init ()
dis=pygame.display.set_mode ((400,300))
pygame.display.update ()
pygame.set.caption('Test pygame')
game_over=false
#This loop is needed to keep the screen running
while not game_over:
	for event in pygame.event.get():
		print(event) #show action on the screen
pygame.quit ()
quit ()