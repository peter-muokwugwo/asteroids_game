import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create group for objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Set containers field on objects
    Player.containers = (updatable, drawable)

    # Instantiate player
    player = Player(
        SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

        
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()