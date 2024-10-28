import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('test')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill('black')

    pygame.display.update()
    

pygame.quit()
