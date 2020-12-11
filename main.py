import pygame

pygame.init()

win = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Algo")

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()