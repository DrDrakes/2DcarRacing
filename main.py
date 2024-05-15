import pygame
import random
import os

clock = pygame.time.Clock()
fps = 60

#Инициализация игры
pygame.init()

screen = pygame.display.set_mode((400, 500))

bg_road = pygame.image.load("images/roadmarkings-22.jpg")#Дорога
car_img = pygame.image.load("images/car/klipartz.com.png")#Игрок
t_car_img = pygame.image.load("images/car/2024-05-01_16.30.19-removebg-preview.png")#Бот

km = 0

label = pygame.font.Font("fonts/Pacifico-Regular.ttf", 40)
lose_label = label.render("Ты проиграл", True, (193, 196, 199))
restart_label = label.render("Начать заново.", True, (105, 25, 208))
restart_label_rect = restart_label.get_rect(topleft=(64, 400))
#score_label = label.render(str(km), True, (193, 196, 199))

bg_road_y = 0

car_x = 170#>
car_y = 350#^
car_speed = 4
car_speed_x = 4

t_car_y = -500


run = True
gameplay = True
while run:
    rand = random.randint(600, 800)

    screen.blit(bg_road, (0, bg_road_y))
    screen.blit(bg_road, (0, bg_road_y - 500))
    screen.blit(car_img, (car_x, car_y))
    screen.blit(t_car_img, (75, t_car_y))

    if gameplay:
        km += 0.1
        print(fps)

        car_rect = car_img.get_rect(topleft=(car_x, car_y))
        t_car_rect = t_car_img.get_rect(topleft=(75, t_car_y)) 
        if car_rect.colliderect(t_car_rect):
            gameplay = False


        bg_road_y += 4
        if bg_road_y >= +500:
            bg_road_y = 0

        t_car_y += 5
        if t_car_y >= +500:
            nrand = rand * -1
            t_car_y = nrand

        #Управление
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: car_x -= car_speed_x
        if keys[pygame.K_RIGHT]: car_x += car_speed_x
        if keys[pygame.K_UP]:
            car_y -= car_speed

        if keys[pygame.K_DOWN]:
            car_y += car_speed

    else:
        km = int(km)
        score_label = label.render("Твой счет: " + str(km), True, (245, 123, 79))
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (90, 200))
        screen.blit(score_label, (90, 250))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            car_x = 170
            car_y = 350
            t_car_y = -500
            km = 0
            gameplay = True
    
    pygame.display.flip()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            print("exit..")
            pygame.quit()
    clock.tick(fps)
