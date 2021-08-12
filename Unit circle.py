import pygame, sys, math

w = 400
h = 400
r = 100

screen = pygame.display.set_mode((w, h))

def unit_circle(cos_, sin_):
	pygame.draw.circle(screen, ((255,255,255)), (int(w/2), int(h/2)), r)
	pygame.draw.circle(screen, ((0,0,0)), (int(w/2), int(h/2)), r-1)
	pygame.draw.line(screen, ((255,255,255)), (int(w/2-r), int(h/2)), (w/2+r, int(h/2)))
	pygame.draw.line(screen, ((255,255,255)), (int(w/2), int(h/2-r)), (int(w/2), int(h/2+r)))

	pygame.draw.line(screen, ((255, 0, 0)), [w/2, h/2],[w/2 + int(( r * cos_ )), h/2 ], 3)
	pygame.draw.line(screen, ((0, 0, 255)), [w/2, h/2],[w/2 + int(( r * cos_ )), h/2 - int((sin_* r))], 3)
	pygame.draw.line(screen, ((0, 255, 0)), [w/2 + int(( r * cos_ )), h/2],[w/2 + int(( r * cos_ )), h/2 - int((sin_* r))], 2)


def unit_circle_two(cos_, sin_):
	pygame.draw.line(screen, ((255, 0, 0)), [20, h/2], [20 + x, h/2], 1)
	return pygame.draw.circle(screen, ((0, 255, 0)), [20 + x, int(h/2) + int(100*sin_*cos_)], 0)

x = 0
y = 0

new_list = []

while True:

	screen.fill((0,0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	x += 1

	sin_ = math.sin(math.radians(x))
	cos_ = math.cos(math.radians(x))

	unit_circle(cos_,sin_)

	pygame.time.delay(int(1000/60))
	pygame.display.update()
