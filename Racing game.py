import sys, pygame, time, random


pygame.init()

size = width, height = 600, 600

screen = pygame.display.set_mode(size)
red = (255,0,0)
blue = (255, 255, 0)
white = (255,255,255)
pink = (206, 18, 125, 1)


x = 0
y = 0
z = 0

ai_x_right = 0
ai_x_left = 0

car_right_left = 0
car_up_down = 0

def collisionWall_right():

    pygame.draw.line(screen, (red), (315, -302 + ai_x_right), ( 485, -302 + ai_x_right)) # top_side
    t = pygame.draw.line(screen, (red), (315, -105 + ai_x_right), ( 485, -105 + ai_x_right)) # bottom_side
    pygame.draw.line(screen, (red), (485, -302 + ai_x_right), ( 485, -105 + ai_x_right)) # right_side
    pygame.draw.line(screen, (red), (315, -302 + ai_x_right), ( 315, -105 + ai_x_right)) # left_side

    return(t)

def collisionWall_left():

    pygame.draw.line(screen, (red), (125, -122 + ai_x_left), ( 295, -122 + ai_x_left)) # top_side
    f = pygame.draw.line(screen, (red), (125, 72 + ai_x_left), (295, 72 + ai_x_left)) # bottom_side
    pygame.draw.line(screen, (red), (125, -122 + ai_x_left), ( 125, 72 + ai_x_left)) # right_side
    pygame.draw.line(screen, (red), (295, -122 + ai_x_left), ( 295, 72 + ai_x_left)) # left_side

    return(f)

def aiCar_right():
    
    last_last_list = []

    pygame.draw.rect(screen, (pink), [350, -280 + ai_x_right, 100, 150])
    j = pygame.draw.rect(screen, (pink), [330, -300 + ai_x_right, 30, 50])
    pygame.draw.rect(screen, (pink), [330, -160 + ai_x_right, 30, 50])
    j_1 = pygame.draw.rect(screen, (pink), [440, -300 + ai_x_right, 30, 50])
    pygame.draw.rect(screen, (pink), [440, -160 + ai_x_right, 30, 50])

    collisionWall_right()
    

    last_last_list.append(j)
    last_last_list.append(j_1)

    return(last_last_list)

def aiCar_left():

    last_last_last_list = []
  
    pygame.draw.rect(screen, (pink), [200-40, -100 + ai_x_left, 100, 150])
    pygame.draw.rect(screen, (pink), [180-40, -120 + ai_x_left, 30, 50])
    k = pygame.draw.rect(screen, (pink), [180-40, 20 + ai_x_left, 30, 50])
    pygame.draw.rect(screen, (pink), [300-50, -120 + ai_x_left, 30, 50])
    s = pygame.draw.rect(screen, (pink), [300-50, 20 + ai_x_left, 30, 50])


    collisionWall_left()


    last_last_last_list.append(k)
    return(last_last_last_list)


def drawCar():

    new_list = []

    pygame.draw.rect(screen, (white), [180 + car_right_left, 400 + car_up_down, 100, 150])
    b = pygame.draw.rect(screen, (white), [160 + car_right_left, 380 + car_up_down, 30, 50])
    pygame.draw.rect(screen, (white), [160 + car_right_left, 520 + car_up_down, 30, 50])
    c = pygame.draw.rect(screen, (white), [270 + car_right_left, 380 + car_up_down, 30, 50])
    pygame.draw.rect(screen, (white), [270 + car_right_left, 520 + car_up_down, 30, 50])


    new_list.append(b)
    new_list.append(c)

    return(new_list)

def drawMap():

    pygame.draw.rect(screen, (red), [100,0, 10, 600])
    pygame.draw.rect(screen, (red), [500,0, 10, 600])
    pygame.draw.line(screen, (red), (500, 10+x), (600, 10+x), 5)
    pygame.draw.line(screen, (red), (0, 10+x), (100, 10+x), 5)

    pygame.draw.rect(screen, (blue), [300,-100+x, 8, 80])
    pygame.draw.rect(screen, (blue), [300,200+y, 8, 80])
    pygame.draw.rect(screen, (blue), [300,400+z, 8, 80])

direction = 0


p = 0




while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
            
        k = random.randint(0, 1)

    x += 10
    z += 10
    y += 10




    random_speed = random.uniform(0.4, 1.15)

    random_speed_left = random.uniform(0.1, 0.5)


    drawMap()
    drawCar()
    number = random.randint(0, 1)

    if drawCar()[0][0] in range(174, 344) and drawCar()[0][1] == collisionWall_right()[1]:
        break

    if drawCar()[0][0] in range(100, 260) and drawCar()[0][1] == collisionWall_left()[1]:
        break


    ai_x_right += random_speed
    ai_x_left += random_speed_left

    patterns = [(ai_x_right-2080 > 600), (ai_x_left-600 > 600)]


    if patterns[number]:
        if number == 0:
            ai_x_right = 0
        elif number == 1:
            ai_x_left = 0



    aiCar_left()
    aiCar_right()

    keys = pygame.key.get_pressed()
 
    if keys[pygame.K_a]:
        car_right_left -= 0.5
        if drawCar()[0][0] == 110:
            car_right_left = -48


    elif keys[pygame.K_d]:
        car_right_left += 0.5
        if drawCar()[0][0] == 360:
            car_right_left = +200


    elif keys[pygame.K_w]:
        car_up_down -= 0.5


    elif keys[pygame.K_s]:
        car_up_down += 0.5


    if x == 600:
        x -= 600
    if y == 400:
        y -= 400
    if z == 200:
        z -= 200



    time.sleep(0.001)
    pygame.display.update()

pygame.quit()
