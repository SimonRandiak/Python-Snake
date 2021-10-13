#!/usr/bin/python3.9

import pygame
import sys 
import random

WIDTH, HEIGHT = 640, 480

GRID_SIZE = 20

GRID_X = WIDTH // GRID_SIZE
GRID_Y = HEIGHT // GRID_SIZE

FPS = 10

SNAKE_COLOR = (50, 168, 82)
FOOD_COLOR = (255, 0, 0)

SNAKE_UP = 1
SNAKE_DOWN = 2
SNAKE_LEFT = 3
SNAKE_RIGHT = 4

loop = True
FPSClock = pygame.time.Clock()

def DrawSnake(window, snake_body):
    for snake in snake_body:
        rectangle = pygame.Rect(GRID_SIZE * snake[0], GRID_SIZE * snake[1], GRID_SIZE, GRID_SIZE) 
        pygame.draw.rect(window, SNAKE_COLOR, rectangle, 1)

def DrawFood(window, food):
    rectangle = pygame.Rect(GRID_SIZE * food[0], GRID_SIZE * food[1], GRID_SIZE, GRID_SIZE) 
    pygame.draw.rect(window, FOOD_COLOR, rectangle, 1)

def GetFoodPosition():
    return [random.randint(1, GRID_X - 1), random.randint(1, GRID_Y - 1)]

def UpdateSnakeHead(snake_head, position):
    if position == SNAKE_UP:
        snake_head[1] -=1
        return True
    elif position == SNAKE_DOWN:
        snake_head[1] +=1
        return True
    elif position == SNAKE_LEFT:
        snake_head[0] -= 1
        return True
    elif position == SNAKE_RIGHT:
        snake_head[0] += 1
        return True

def Collision(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True
    return False

def SnakeBodyCollision(snake_body):
    for snake in snake_body[1:]:
        if Collision(snake_body[0][0], snake_body[0][1], snake[0], snake[1]):
            return True
    return False

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    snake_body = []
    snake_body.append([GRID_X // 2, GRID_Y // 2])
    snake_head = snake_body[0]
    snake_position = 0

    food = []
    spawn_food = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_position = SNAKE_UP 
                elif event.key == pygame.K_DOWN:
                    snake_position = SNAKE_DOWN 
                elif event.key == pygame.K_LEFT:
                    snake_position = SNAKE_LEFT 
                elif event.key == pygame.K_RIGHT:
                    snake_position = SNAKE_RIGHT
                elif event.key == pygame.K_ESCAPE:
                    snake_position = 0

        UpdateSnakeHead(snake_head, snake_position) 
        snake_body.insert(0, [snake_head[0], snake_head[1]])
        
        if spawn_food:
            food = GetFoodPosition()
            while food in snake_body:
                food = GetFoodPosition()
            spawn_food = False
        
        if len(snake_body) > 4:
            if SnakeBodyCollision(snake_body):
                print("Game Over")
                sys.exit()

        if Collision(snake_body[0][0], snake_body[0][1], food[0], food[1]):
            spawn_food = True
            food = [0,0]
        else:
            snake_body.pop()

        print(snake_body)

        window.fill((0,0,0))
        DrawSnake(window, snake_body)
        DrawFood(window, food)

        pygame.display.update()

        FPSClock.tick(FPS)
    pygame.quit()

