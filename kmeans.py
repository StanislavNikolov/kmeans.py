import pygame
import time
import math
from random import Random

dots = []
clusters = []

pygame.init()
screen = pygame.display.set_mode( (400, 400) ) 

rgen = Random()

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __iadd__(self, v):
		self.x += v.x
		self.y += v.y
		return Vector(self.x, self.y)

class Cluster:
	def __init__(self, color):
		self.position = Vector(rgen.random() * 400, rgen.random() * 400)
		self.color = color
		self.groupDots = []

def distance(v1, v2):
	return math.sqrt( (v2.x - v1.x) * (v2.x - v1.x) + (v2.y - v1.y) * (v2.y - v1.y) )


def step():
	for i in clusters:
		i.groupDots = []

	for i in dots:
		best = clusters[0]

		for j in clusters:
			if distance(j.position, i) < distance(best.position, i):
				best = j

		best.groupDots.append(i)
			
	for i in clusters:
		posSum = Vector(0, 0)
		for j in i.groupDots:
			posSum += j
		if len(i.groupDots) > 0:
			i.position.x = posSum.x / len(i.groupDots)
			i.position.y = posSum.y / len(i.groupDots)

		moveBoost = 0
		i.position.x += rgen.random() * moveBoost - rgen.random() * moveBoost
		i.position.y += rgen.random() * moveBoost - rgen.random() * moveBoost

def render():
	screen.fill((0, 0, 0))
	for i in clusters:
		pygame.draw.circle(screen, i.color, (int(i.position.x), int(i.position.y)), 8)
		for j in i.groupDots:
			pygame.draw.circle(screen, i.color, (int(j.x), int(j.y)), 8)

	pygame.display.update()

def init(n):
	for i in range(n):
		clusters.append( Cluster( (int(rgen.random() * 255), int(rgen.random() * 255), int(rgen.random() * 255)) ) )
	for i in range(4000):
		dots.append(Vector(rgen.random() * 400, rgen.random() * 400))

init(14)

while True:
	step()
	render()
	#time.sleep(0.1)
