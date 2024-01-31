import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake
snake_block = 10
snake_speed = 15

# Snake initial position
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Food
food_pos = [random.randrange(1, (width//snake_block)) * snake_block,
            random.randrange(1, (height//snake_block)) * snake_block]

# Initial direction
direction = 'RIGHT'
change_to = direction

# Initial Score
score = 0

# Game over flag
game_over = False

# Clock to control speed
clock = pygame.time.Clock()

# Function to draw the snake
def draw_snake(snake_block, snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, white, [block[0], block[1], snake_block, snake_block])

# Function to generate food
def draw_food(food_pos):
    pygame.draw.rect(screen, red, [food_pos[0], food_pos[1], snake_block, snake_block])

# Game Over message
def game_over_message():
    font = pygame.font.SysFont('times new roman', 30)
    game_over_text = font.render('Your Score is: ' + str(score), True, white)
    screen.blit(game_over_text, [width / 6, height / 3])
    pygame.display.flip()
    pygame.time.wait(2 * 1000)  # 2 seconds
    pygame.quit()
    sys.exit()

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Change direction based on user input
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= snake_block
    if direction == 'DOWN':
        snake_pos[1] += snake_block
    if direction == 'LEFT':
        snake_pos[0] -= snake_block
    if direction == 'RIGHT':
        snake_pos[0] += snake_block

    # Check if snake eats the food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_pos = [random.randrange(1, (width//snake_block)) * snake_block,
                    random.randrange(1, (height//snake_block)) * snake_block]
    else:
        # Remove the last block of the snake
        snake_body.pop()

    # Add a new block at the head of the snake
    new_head = [snake_pos[0], snake_pos[1]]
    snake_body.insert(0, new_head)

    # Check if the snake collides with the screen boundaries or itself
    if (snake_pos[0] >= width or snake_pos[0] < 0 or
            snake_pos[1] >= height or snake_pos[1] < 0 or
            snake_pos in snake_body[1:]):
        game_over = True
        game_over_message()

    # Draw everything
    screen.fill(black)
    draw_snake(snake_block, snake_body)
    draw_food(food_pos)
    pygame.display.flip()

    # Set the speed of the game
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
sys.exit()
