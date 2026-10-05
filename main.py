import pygame


from settings import FPS, SCREEN_H, SCREEN_W
from assets import load_assets
from player import Player

pygame.init()

assets = load_assets()
player = Player(assets)
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption('Crocodile Hunter')
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    player.update(keys)
    for bullet in player.bullets:
        bullet.update()
    for i in range(len(player.bullets) -1, -1, -1):
        if player.bullets[i].is_off_screen():
            player.bullets.pop(i)

    screen.blit(assets['bg'],(0,0))
    player.draw(screen)
    for bullet in player.bullets:
        bullet.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()