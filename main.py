# import necessary libraries
import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monster Shark Game")
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 24)

# Asset directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(BASE_DIR, "assets")

# Load and scale images
shark_img = pygame.image.load(os.path.join(ASSET_DIR, "shark.png"))
shark_img = pygame.transform.scale(shark_img, (150, 150))

fish_img = pygame.image.load(os.path.join(ASSET_DIR, "fish.png")).convert_alpha()
fish_img = pygame.transform.scale(fish_img, (60, 60))

background_img = pygame.image.load(os.path.join(ASSET_DIR, "background.png")).convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

grass = pygame.image.load(os.path.join(ASSET_DIR, "grass.png")).convert_alpha()
grass = pygame.transform.scale(grass, (WIDTH, 100))
grass_y = HEIGHT - grass.get_height() + 30

# Sound effects
catch_sound = pygame.mixer.Sound(os.path.join(ASSET_DIR, "catch.wav"))
gameover_sound = pygame.mixer.Sound(os.path.join(ASSET_DIR, "gameover.wav"))

# Rectangles
shark_rect = shark_img.get_rect(topleft=(275, 350))
mouth_rect = pygame.Rect(
    shark_rect.centerx - 10,
    shark_rect.top + 10,
    20,
    shark_rect.height - 20
)
fish_rect = fish_img.get_rect(
    topleft=(random.randint(0, WIDTH - 60), random.randint(0, HEIGHT - 60))
)

# Game variables
score = 0
missed = 0
base_speed = 5
max_missed = 100
shark_speed = base_speed + 5
fish_speed = base_speed + 3

# Game state
running = True
game_over = False

# Game loop
while running:
    dt = clock.tick(60)

    screen.blit(background_img, (0, 0))
    screen.blit(grass, (0, grass_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            score = 0
            missed = 0
            game_over = False
            shark_rect.topleft = (275, 350)
            fish_rect.topleft = (
                random.randint(0, WIDTH - 60),
                random.randint(0, grass_y - 60)
            )
            

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and shark_rect.left > 0:
            shark_rect.x -= shark_speed
        if keys[pygame.K_RIGHT] and shark_rect.right < WIDTH:
            shark_rect.x += shark_speed
        if keys[pygame.K_UP] and shark_rect.top > 0:
            shark_rect.y -= shark_speed
        if keys[pygame.K_DOWN] and shark_rect.bottom < grass_y:
            shark_rect.y += shark_speed

        # Stay above grass
        if shark_rect.bottom > grass_y:
            shark_rect.bottom = grass_y
        if fish_rect.bottom > grass_y:
            fish_rect.bottom = grass_y


        # Update mouth position
        mouth_width = 30
        mouth_height = 38
        mouth_rect.update(
            shark_rect.left - 10,
            shark_rect.centery - mouth_height // 2,
            mouth_width,
            mouth_height
        )

        # Move fish
        fish_rect.x += fish_speed + score // 10  # Increase speed with score
        if fish_rect.x > WIDTH:
            fish_rect.x = 0
            fish_rect.y = random.randint(0, grass_y - 60)
            missed += 1

        if mouth_rect.colliderect(fish_rect):
            score += 1
            fish_rect.x = 0
            fish_rect.y = random.randint(0, grass_y - 60)
            catch_sound.play()

        if missed >= max_missed:
            game_over = True
            gameover_sound.play()

    # Draw game elements
    screen.blit(shark_img, shark_rect)
    screen.blit(fish_img, fish_rect)
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Missed: {missed}/{max_missed}", True, (0, 255, 0)), (10, 40))

    if game_over:
        game_over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
    
    pygame.display.flip()

# Quit game
pygame.quit()
sys.exit()
