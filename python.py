#snake Game
import pygame
import sys
import random
import time

check_errors = pygame.init()

#(6,0)

if check_errors[1] > 0:
	print('(!) Had {0} initializing error, exiting...'.format(check_errors[1]))
	sys.exit(-1)
else:
	print('(+) PyGame successfullt initialised.')	

score =0 
#Screen Play surface

playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game by MUDIT')
#colors

red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
blue = pygame.Color(0, 0, 255)   
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

#FPS controller

fpscontroller = pygame.time.Clock()

#variables

snakePos = [100, 50]
snakeBody= [[100,50], [90,50], [80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

#Game over function

def gameOver():
	myFont = pygame.font.SysFont('monaco', 72)
	GOsurf = myFont.render('Game Over!', True, red)
	GOrect = GOsurf.get_rect()
	GOrect.midtop = (360,15)
	playSurface.blit(GOsurf,GOrect)
	showScore(0)
	pygame.display.flip()
	time.sleep(5)
	pygame.quit()           #game
	sys.exit()              #console

def showScore(choice=1):
	sFont = pygame.font.SysFont('monaco', 24)
	ssurf = sFont.render('Score: '+str(score), True, black)
	srect = ssurf.get_rect()
	if choice == 1:
		srect.midtop = (80, 10)
	else:
		srect.midtop = (360, 120)
	playSurface.blit(ssurf,srect)
#main logic of the game

while 1: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('d'):
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('d'):
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('d'):
				changeto = 'DOWN'	
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))
	
	# validation of direction
	
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'

	if direction == 'RIGHT':
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'UP':
		snakePos[1] -= 10
	if direction == 'DOWN':
		snakePos[1] += 10	
	#snake body
	snakeBody.insert(0, list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		score+=1
		foodSpawn = False
	else:
		snakeBody.pop()
	
	if foodSpawn == False:
		foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
	foodSpawn = True
	playSurface.fill(white)
	for pos in snakeBody:
	 	pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))
	if snakePos[0]==720 or snakePos[1] == 460 or snakePos[0]==0 or snakePos[1]==0:
		gameOver()
	for block in snakeBody[1:]:
		if snakePos[0]==block[0] and snakePos[1] == block[1]:
			gameOver()
	pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))
	showScore(1)	
	pygame.display.flip()
	fpscontroller.tick(100)


#pyinstaller



