import pygame
import random

class Snake:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = (1, 0)
        self.food = (x,y)

    def move(self):
        # Определяем новую голову змейки
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])

        # Добавляем новую голову в начало списка
        self.body.insert(0, new_head)

        # Удаляем хвост змейки, если она не съела еду
        if len(self.body) > 1 and new_head != self.food:
            self.body.pop()
        else:
            self.food = food.generate_food()

    def check_collision(self, x, y):
        # Проверяем столкновение змейки со стенами
        if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
            return True

        # Проверяем столкновение змейки с едой
        if (x, y) == self.food:
            self.food = food.generate_food()
            return False

        # Проверяем столкновение змейки с самой собой
        if (x, y) in self.body[1:]:
            return True

        return False



    def generate_food(self):
        # Генерируем новую позицию для еды
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.body:
                return (x, y)

    def turn_left(self):
        if self.direction != (1, 0):
            self.direction = (-1, 0)

    def turn_right(self):
        if self.direction != (-1, 0):
            self.direction = (1, 0)

    def turn_up(self):
        if self.direction != (0, 1):
            self.direction = (0, -1)

    def turn_down(self):
        if self.direction != (0, -1):
            self.direction = (0, 1)


class Food:
    def __init__(self):
        self.position = self.generate_food()

    def generate_food(self):
        # Генерируем случайную позицию для еды
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake.body:
                return (x, y)

    def spawn_food(self):
        """Спавнит еду в случайном месте на экране."""
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)


# Определяем размеры окна и размеры ячейки на поле
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CELL_SIZE = 20

# Определяем размеры игрового поля в ячейках
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Определяем цвета для змейки, еды и фона
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Инициализируем библиотеку pygame
pygame.init()

# Создаем окно для отображения игры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Создаем объекты для змейки и еды
snake = Snake(GRID_WIDTH // 2, GRID_HEIGHT // 2)
food = Food()

# Определяем флаг для выхода из игры
running = True

# Определяем время последнего обновления
last_update_time = pygame.time.get_ticks()

# Цикл игры
while running:
    # Обрабатываем события ввода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.turn_up()
            elif event.key == pygame.K_a:
                snake.turn_left()
            elif event.key == pygame.K_s:
                snake.turn_down()
            elif event.key == pygame.K_d:
                snake.turn_right()

    # Обновляем поле, если прошло достаточно времени с последнего обновления
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time >= 100:
        # Обновляем змейку
        snake.move()

        # Проверяем столкновение змейки со стенами и едой
        if snake.check_collision(snake.body[0][0], snake.body[0][1]):
            running = False

        # Отображаем фон
        screen.fill(BACKGROUND_COLOR)

        # Отображаем змейку
        for x, y in snake.body:
            pygame.draw.rect(screen, SNAKE_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Отображаем еду
        pygame.draw.rect(screen, FOOD_COLOR, (food.position[0] * CELL_SIZE, food.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Обновляем экран
        pygame.display.flip()

        # Обновляем время последнего обновления
        last_update_time = current_time

# Завершаем игру
pygame.quit()
