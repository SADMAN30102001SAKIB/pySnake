import pygame
import random

# Initialize Pygame
pygame.init()
game_over = False

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set block size and margin
BLOCK_SIZE = 15
MARGIN = 1

# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set clock
clock = pygame.time.Clock()

# Define functions
def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE + MARGIN):
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE + MARGIN):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, WHITE, rect)

def draw_snake(snake_list):
    for x,y in snake_list:
        rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

def game_loop():
    # Initialize variables
    game_over = False
    game_close = False

    # Set starting position of the snake
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Set initial movement direction of the snake
    x_change = 0
    y_change = 0

    # Create initial snake list and length
    snake_list = []
    snake_length = 1

    # Set random position of the food
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    # Game loop
    while not game_over:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE - MARGIN
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE + MARGIN
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -BLOCK_SIZE - MARGIN
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = BLOCK_SIZE + MARGIN

        # Move snake
        x += x_change
        y += y_change

        # Check if snake hits wall
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            game_close = True

        # Create new head of snake
        snake_head = [x, y]
        snake_list.append(snake_head)

        # Remove tail of snake if too long
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake hits itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw game elements
        screen.fill(BLACK)
        draw_grid()
        draw_snake(snake_list)
        pygame.draw.rect(screen, WHITE, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Update display
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1

        # Check if game is over
        if game_close:
            screen.fill(BLACK)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("Game Over!", True, WHITE)
            screen.blit(message, [SCREEN_WIDTH/6, SCREEN_HEIGHT/3])
            pygame.display.update()
            pygame.time.delay(2000)

            game_loop()

        # Set game speed
        clock.tick(15)
        
# Main event loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Call game loop function
    game_loop()

# Quit Pygame
pygame.quit()


