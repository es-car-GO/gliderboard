import pygame

"""
Cursor Setup
In windows 11 setup, Accessibility > Mouse pointer and touch
Mouse pointer style = Inverted
Size = 9
"""
pygame.init()
screen = pygame.display.set_mode((2560, 1440))
cursor = pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_NO))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        cursor_pos = pygame.mouse.get_pos()
        color = (cursor_pos[0]/2560*255, cursor_pos[0]/2560*255, cursor_pos[1]/1440*255)

    screen.fill(color)
    pygame.display.update()

pygame.quit()