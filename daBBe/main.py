import pygame
import os
import random
import time

# Initialize pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jump Scare Prank")

# Load jump scare image
jumpscare_image = pygame.image.load("jumpscare_image.jpg")
jumpscare_image = pygame.transform.scale(jumpscare_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load scary sound
pygame.mixer.init()
jumpscare_sound = pygame.mixer.Sound("jumpscare_sound.wav")

def jump_scare():
    screen.blit(jumpscare_image, (0, 0))
    pygame.display.flip()
    jumpscare_sound.play()

def main():
    running = True

    # Main loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Display something innocuous (optional)
        pygame.display.flip()

        # Simulate delay before jump scare
        time.sleep(random.uniform(3, 10))

        # Execute jump scare
        jump_scare()

        # Allow time for jump scare to play out
        time.sleep(3)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
