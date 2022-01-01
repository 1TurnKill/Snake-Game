import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400,500)) #ตัวกำหนดความกว้างเเละสูงของตัวเกม
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
test_surface.fill((0,0,255))
x_pos = 200
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    x_pos -= 1
    screen.blit(test_surface,(200,x_pos))
    pygame.display.update()
    clock.tick(60)