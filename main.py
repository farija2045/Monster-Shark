import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monster Shark Catch Fish")
clock = pygame.time.Clock()

# Asset directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(BASE_DIR, "assets")

# Load and scale images
player_img = pygame.image.load(os.path.join(ASSET_DIR, "shark.png"))
player_img = pygame.transform.scale(player_img, (90, 90))  # make shark bigger
fish_img = pygame.image.load(os.path.join(ASSET_DIR, "fish.png"))
fish_img = pygame.transform.scale(fish_img, (40, 40))
background_img = pygame.image.load(os.path.join(ASSET_DIR, "background.png"))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Load sound effects
catch_sound = pygame.mixer.Sound(os.path.join(ASSET_DIR, "catch.wav"))

gameover_sound = pygame.mixer.Sound(os.path.join(ASSET_DIR, "gameover.wav"))

# Rectangles
player_rect = player_img.get_rect(topleft=(255, 310))  # adjust position for bigger shark
fish_rect = fish_img.get_rect(topleft=(random.randint(0, WIDTH - 40), random.randint(0, HEIGHT - 200)))

# Game variables
fish_speed = 8
score = 0
missed = 0
max_missed = 100
font = pygame.font.SysFont("Arial", 24)

# Game state
running = True
game_over = False

while running:
    clock.tick(60)
    screen.fill((200, 255, 200))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # Reset game
            score = 0
            missed = 0
            game_over = False
            player_rect.topleft = (255, 310)
            fish_rect.topleft = (random.randint(0, WIDTH - 40), random.randint(0, HEIGHT - 200))

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= 5
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += 5
        if keys[pygame.K_UP] and player_rect.top > 0:
            player_rect.y -= 5
        if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
            player_rect.y += 5

        # Fish movement
        fish_rect.x += fish_speed
        if fish_rect.x > WIDTH:
            fish_rect.x = 0
            fish_rect.y = random.randint(0, HEIGHT - fish_rect.height)
            missed += 1

    # Define mouth area
    mouth_width = player_rect.width // 4  # smaller width for left mouth
    mouth_height = player_rect.height // 7  # small height for mouth
    mouth_x = player_rect.left - 2  # move even further left
    mouth_y = player_rect.top + player_rect.height // 2 - 10  # move higher
    mouth_width = player_rect.width // 6
    mouth_height = player_rect.height // 5
    mouth_rect = pygame.Rect(mouth_x, mouth_y, mouth_width, mouth_height)

    if mouth_rect.collidepoint(fish_rect.center):
            score += 1
            fish_rect.x = 0
            fish_rect.y = random.randint(0, HEIGHT - fish_rect.height)
            catch_sound.play()

        # Game over condition
    if missed >= max_missed:
            game_over = True
            gameover_sound.play()

    # Draw game
    screen.blit(background_img, (0, 0))
    screen.blit(player_img, player_rect)
    screen.blit(fish_img, fish_rect)
    # (Mouth area frame removed for production)

    screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
    screen.blit(font.render(f"Missed: {missed}/{max_missed}", True, (255, 0, 0)), (10, 40))

    if game_over:
        game_over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
    


    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
