import pygame

# Initialize Pygame
pygame.init()

# Set the window size and title

flags = pygame.RESIZABLE | pygame.SCALED
screen = pygame.display.set_mode((256, 224), flags)
pygame.display.set_caption("Pokémon Red")

# Load the start screen image and set it as the background
start_screen = pygame.image.load("start_screen.png")
screen.blit(start_screen, (0, 0))
pygame.display.flip()

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
