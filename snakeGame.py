import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the game title
pygame.display.set_caption('Snake Game')

# Define game constants
block_size = 20
fps = 10
directions = ['up', 'down', 'left', 'right']

class Snake:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.direction = 'right'
        self.length = 1
        self.body = [(self.x, self.y)]

    def move(self):
        if self.direction == 'up':
            self.y -= block_size
        elif self.direction == 'down':
            self.y += block_size
        elif self.direction == 'left':
            self.x -= block_size
        elif self.direction == 'right':
            self.x += block_size

        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop(0)

class Food:
    def __init__(self):
        self.x = random.randint(0, screen_width - block_size) // block_size * block_size
        self.y = random.randint(0, screen_height - block_size) // block_size * block_size

snake = Snake()
food = Food()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction!= 'down':
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN and snake.direction!= 'up':
                snake.direction = 'down'
            elif event.key == pygame.K_LEFT and snake.direction!= 'right':
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT and snake.direction!= 'left':
                snake.direction = 'right'

    # Move the snake
    snake.move()

    # Check for collisions
    if (snake.x, snake.y) in snake.body[:-1]:
        print("Game Over")
        pygame.quit()
        sys.exit()
    elif snake.x < 0 or snake.x >= screen_width or snake.y < 0 or snake.y >= screen_height:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Check for food
    if (snake.x, snake.y) == (food.x, food.y):
        snake.length += 1
        food = Food()

    # Draw everything
    screen.fill((0, 0, 0))
    for pos in snake.body:
        pygame.draw.rect(screen, (255, 255, 255), (pos[0], pos[1], block_size, block_size))
    pygame.draw.rect(screen, (255, 0, 0), (food.x, food.y, block_size, block_size))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(fps)