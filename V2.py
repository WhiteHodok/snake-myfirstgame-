import pygame
import random

# Define constants for the game
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# Define the Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def move(self):
        head = self.body[0]
        x, y = self.direction
        new_head = ((head[0] + x) % GRID_WIDTH, (head[1] + y) % GRID_HEIGHT)
        if new_head in self.body:
            return False
        self.body.insert(0, new_head)
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        self.direction = direction

    def grow(self):
        self.body.append(self.body[-1])


# Define the Apple class
class Apple:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')

# Initialize the game objects
snake = Snake()
apple = Apple()

# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)


    if not snake.move():
        running = False
    if snake.body[0] == apple.position:
        apple.position = apple.generate_position()
        snake.grow()


    screen.fill((0, 0, 0))
    for segment in snake.body:
        x, y = segment
        pygame.draw.rect(screen, (0, 255, 0), (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    x, y = apple.position
    pygame.draw.rect(screen, (255, 0, 0), (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.display.flip()


    pygame.time.delay(100)

# Clean up
pygame.quit()

