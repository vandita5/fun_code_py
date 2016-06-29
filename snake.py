import pygame, sys, time, random
from math import floor
from pygame.locals import *

def gameOver():
	gameOverFont = pygame.font.Font('freesansbold.ttf',72)
	gameOverSurf = gameOverFont.render('Game Over', True, greyColor)
	gameOverRect = gameOverSurf.get_rect()
	gameOverRect.midtop = (320,10)
	playSurface.blit(gameOverSurf,gameOverRect)
	pygame.display.flip()
	time.sleep(2)
	pygame.quit()
	sys.exit()

def checkOverlap(a,b):
	for item in a:
		if item == b:
			return True
	return False

def displaySnake(a):
	pygame.draw.rect(playSurface, whiteColor, Rect(a[0][0], a[0][1], 20, 20))
	for index in range (1,len(a)-1):
		if a[index-1][0] == a[index+1][0]:
			pygame.draw.rect(playSurface, whiteColor, Rect(a[index][0]+2, a[index][1], 16, 20))
		elif a[index-1][1] == a[index+1][1]:
			pygame.draw.rect(playSurface, whiteColor, Rect(a[index][0], a[index][1]+2, 20, 16))
		else:
			if a[index][0] > a[index+1][0] or a[index][0] > a[index-1][0]:
				pygame.draw.rect(playSurface, whiteColor, Rect(\
					a[index][0], a[index][1]+2, 18, 16))
			else:
				pygame.draw.rect(playSurface, whiteColor, Rect(a[index][0]+2, a[index][1]+2, 18, 16))
			if a[index][1] < a[index-1][1] or a[index][1] < a[index+1][1]:
				pygame.draw.rect(playSurface, whiteColor, Rect(a[index][0]+2, a[index][1]+18, 16, 2))
			else:
				pygame.draw.rect(playSurface, whiteColor, Rect(a[index][0]+2, a[index][1], 16, 2))
	if a[-1][1] == a[-2][1]:
		pygame.draw.rect(playSurface, whiteColor, Rect(a[-1][0], a[-1][1]+2, 20, 16))
	else:
		pygame.draw.rect(playSurface, whiteColor, Rect(a[-1][0]+2, a[-1][1], 16, 20))

pygame.init()
fpsClock = pygame.time.Clock()
playSurface = pygame.display.set_mode((640,480))
pygame.display.set_caption('Raspberry Snake')
redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(0, 255, 0)
blackColor = pygame.Color(0, 0, 0)
blueColor = pygame.Color(0, 0, 255)
whiteColor = pygame.Color(255, 255, 255)
greyColor = pygame.Color(150, 150, 150)
snakePosition = [100,100]
snakeSegments = [[100,100],[80,100],[60,100]]
raspberryPosition = [300,300]
raspberrySpawned = 1
nSteps = 0
direction = 'right'
changeDirection = direction
score = 0
bonus = 0
nStepsBonus = 0
bonusColor = redColor
level = 1

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_RIGHT or event.key == ord('d'):
				changeDirection = 'right'
			if event.key == K_LEFT or event.key == ord('a'):
				changeDirection = 'left'
			if event.key == K_UP or event.key == ord('w'):
				changeDirection = 'up'
			if event.key == K_DOWN or event.key == ord('s'):
				changeDirection = 'down'
			if event.key == K_ESCAPE :
				pygame.event.post(pygame.event.Event(QUIT))

	if changeDirection == 'right' and not direction == 'left':
		direction = changeDirection
	if changeDirection == 'left' and not direction == 'right':
		direction = changeDirection
	if changeDirection == 'up' and not direction == 'down':
		direction = changeDirection
	if changeDirection == 'down' and not direction == 'up':
		direction = changeDirection
	if direction == 'right':
		snakePosition[0] += 20
	if direction == 'left':
		snakePosition[0] -= 20
	if direction == 'up':
		snakePosition[1] -= 20
	if direction == 'down':
		snakePosition[1] += 20
	snakeSegments.insert(0,list(snakePosition))
	if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
		raspberrySpawned = 0
		score += 1
	elif bonus == 1:
		if snakePosition[0] == bonusPosition[0] and snakePosition[1] == bonusPosition[1]:
			bonus = 0
			score += 10
		else:
			snakeSegments.pop()
	else:
		snakeSegments.pop()
	if raspberrySpawned == 0:
		x = random.randrange(1,32)
		y = random.randrange(1,24)
		raspberryPosition = [int(x*20),int(y*20)]
		while checkOverlap(snakeSegments, raspberryPosition):
			x = random.randrange(1,32)
			y = random.randrange(1,24)
			raspberryPosition = [int(x*20),int(y*20)]
		raspberrySpawned = 1
		nSteps = 0
		rnum = random.randrange(0,100)
		if  rnum < 40 and bonus == 0:
			bonus = 1
			x = random.randrange(1,32)
			y = random.randrange(1,24)
			bonusPosition = [int(x*20),int(y*20)]
			while checkOverlap(snakeSegments, bonusPosition) or checkOverlap(raspberryPosition, bonusPosition):
				x = random.randrange(1,32)
				y = random.randrange(1,24)
				bonusPosition = [int(x*20),int(y*20)]
			nStepsBonus = 0
	playSurface.fill(blackColor)
	#for position in snakeSegments:
	#	pygame.draw.rect(playSurface, whiteColor, Rect(position[0], position[1], 20, 20))
	displaySnake(snakeSegments)
	pygame.draw.rect(playSurface,redColor, Rect(raspberryPosition[0],raspberryPosition[1], 20,20))
	
	if bonus == 1:
		if bonusColor == redColor:
			bonusColor = blueColor
		elif bonusColor == blueColor:
			bonusColor = greenColor
		elif bonusColor == greenColor:
			bonusColor = redColor
		pygame.draw.rect(playSurface,bonusColor, Rect(bonusPosition[0],bonusPosition[1], 20,20))
	if snakePosition[0] > 620 or snakePosition[0] < 0:
		gameOver()
	if snakePosition[1] > 460 or snakePosition[1] < 0:
		gameOver()
	for position in snakeSegments[1:]:
		if snakePosition[0] == position[0] and snakePosition[1] == position[1]:
			gameOver()
	nSteps += 1
	nStepsBonus += 1
	if nSteps == 30:
		raspberrySpawned = 0
	if nStepsBonus == 20:
		bonus = 0
	scoreFont = pygame.font.Font('freesansbold.ttf',20)
	scoreSurf = scoreFont.render('SCORE: ' + str(score), True, blueColor)
	scoreRect = scoreSurf.get_rect()
	if snakePosition[1] < 30 or raspberryPosition[1] < 30 :
		scoreRect.bottomright = (630, 470)
	elif bonus == 1:
		if bonusPosition[1] < 30:
			scoreRect.bottomright = (630, 470)
	else:
		scoreRect.topleft = (10,10)
	playSurface.blit(scoreSurf,scoreRect)
	
	raspberryLifeFont = pygame.font.Font('freesansbold.ttf', 10)
	raspberryLifeSurf = raspberryLifeFont.render('Raspberry: ', True, redColor)
	raspberryLifeRect = raspberryLifeSurf.get_rect()
	bonusLifeFont = pygame.font.Font('freesansbold.ttf', 10)
	bonusLifeSurf = bonusLifeFont.render('Bonus: ', True, bonusColor)
	bonusLifeRect = bonusLifeSurf.get_rect()
	if snakePosition[1] < 30 or raspberryPosition[1] < 30 :
		raspberryLifeRect.bottomleft = (10, 470)
		pygame.draw.rect(playSurface, redColor, Rect(80,460, (30-nSteps), 10))	
	else:
		raspberryLifeRect.topleft = (530,10)
		pygame.draw.rect(playSurface, redColor, Rect(600,10, (30-nSteps), 10))
	if bonus == 1:
		if bonusPosition[1] < 30 or snakePosition[1] < 30 or raspberryPosition[1] < 30 :
			bonusLifeRect.bottomleft = (10, 480)
			pygame.draw.rect(playSurface, bonusColor, Rect(80,470, (20-nStepsBonus), 10))
		else:
			bonusLifeRect.topleft = (530,20)
			pygame.draw.rect(playSurface, bonusColor, Rect(600,20, (20-nStepsBonus), 10))
		playSurface.blit(bonusLifeSurf, bonusLifeRect)
	playSurface.blit(raspberryLifeSurf, raspberryLifeRect)
	
	pygame.display.flip()
	#if f:
	#	level += 1
	#print (5 +(floor(score/20)))
	fpsClock.tick(5 +(floor(score/20)))
	
