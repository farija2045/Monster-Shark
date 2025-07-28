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
pygame.display.set_caption("Catch the Chicken Game")
clock = pygame.time.Clock()

# Asset directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(BASE_DIR, "assets")

# Load and scale images
player_img = pygame.image.load(os.path.join(ASSET_DIR, "player.png"))
player_img = pygame.transform.scale(player_img, (50, 50))
hen_img = pygame.image.load(os.path.join(ASSET_DIR, "chicken.png"))
hen_img = pygame.transform.scale(hen_img, (40, 40))

# Load sound effects
catch_sound = pygame.mixer.Sound(os.path.join(ASSET_DIR, "catch.wav"))
miss_sound = pygame.mixer.Sound(os.path.join(ASSET_DIR, "missed.wav"))
gameover_sound = pygame.mixer.Sound(os.path.join(ASSET_DIR, "gameover.wav"))

# Rectangles
player_rect = player_img.get_rect(topleft=(275, 350))
hen_rect = hen_img.get_rect(topleft=(random.randint(0, WIDTH - 40), random.randint(0, HEIGHT - 200)))

# Game variables
chicken_speed = 8
score = 0
missed = 0
max_missed = 60
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
            player_rect.topleft = (275, 350)
            hen_rect.topleft = (random.randint(0, WIDTH - 40), random.randint(0, HEIGHT - 200))

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

        # Chicken movement
        hen_rect.x += chicken_speed
        if hen_rect.x > WIDTH:
            hen_rect.x = 0
            hen_rect.y = random.randint(0, HEIGHT - hen_rect.height)
            missed += 1
            miss_sound.play()

        # Collision detection
        if player_rect.colliderect(hen_rect):
            score += 1
            hen_rect.x = 0
            hen_rect.y = random.randint(0, HEIGHT - hen_rect.height)
            catch_sound.play()

        # Game over condition
        if missed >= max_missed:
            game_over = True
            gameover_sound.play()

    # Draw game
    screen.blit(player_img, player_rect)
    screen.blit(hen_img, hen_rect)

    screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
    screen.blit(font.render(f"Missed: {missed}/{max_missed}", True, (255, 0, 0)), (10, 40))

    if game_over:
        game_over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
