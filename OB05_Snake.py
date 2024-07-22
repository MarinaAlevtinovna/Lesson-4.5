import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
HEAD_COLOR = (0, 128, 0)  # Darker green for the head

# Snake block size
BLOCK_SIZE = 20

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 35)

# Load head image
try:
    head_image = pygame.image.load('snake_head.png')
    head_image = pygame.transform.scale(head_image, (BLOCK_SIZE, BLOCK_SIZE))
except pygame.error:
    head_image = None

# Load body image
try:
    body_image = pygame.image.load('snake_body.png')
    body_image = pygame.transform.scale(body_image, (BLOCK_SIZE, BLOCK_SIZE))
except pygame.error:
    body_image = None

def message(msg, color, x, y):
    text = font.render(msg, True, color)
    screen.blit(text, [x, y])

def game_loop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Initial speed
    speed = 10

    while not game_over:

        while game_close == True:
            screen.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake body
        for block in snake_List[:-1]:
            if body_image:
                screen.blit(body_image, (block[0], block[1]))
            else:
                pygame.draw.rect(screen, WHITE, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

        # Draw the head
        if head_image:
            screen.blit(head_image, (snake_List[-1][0], snake_List[-1][1]))
        else:
            pygame.draw.rect(screen, HEAD_COLOR, [snake_List[-1][0], snake_List[-1][1], BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            Length_of_snake += 1
            speed += 1

        clock.tick(speed)

    pygame.quit()
    sys.exit()

game_loop()