import os
import pygame
pygame.init()
pygame.mixer.init()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_assets():
    assets = {}
    assets['icon'] = pygame.image.load(os.path.join(BASE_DIR,'images','icona.png'))
    assets['bg'] = pygame.image.load(os.path.join(BASE_DIR,'images', 'game_background.png'))
    assets['walk_right'] = [
        pygame.image.load(os.path.join(BASE_DIR,'images','player_right','pl_on.png')),
        pygame.image.load(os.path.join(BASE_DIR,'images','player_right','pl_tw.png')),
        pygame.image.load(os.path.join(BASE_DIR, 'images', 'player_right', 'pl_fr.png')),
        pygame.image.load(os.path.join(BASE_DIR, 'images', 'player_right', 'pl_fo.png')),
        ]
    assets['walk_left'] = [
        pygame.image.load(os.path.join(BASE_DIR,'images','player_left','pl_one.png')),
        pygame.image.load(os.path.join(BASE_DIR, 'images','player_left', 'pl_two.png')),
        pygame.image.load(os.path.join(BASE_DIR, 'images','player_left', 'pl_free.png')),
        pygame.image.load(os.path.join(BASE_DIR, 'images', 'player_left', 'pl_four.png')),
        ]
    assets['bullet'] = pygame.image.load(os.path.join(BASE_DIR,'images','bullet.png'))
    assets['crocodile'] = pygame.image.load(os.path.join(BASE_DIR,'images','crocodile.png'))
    assets['bg_sound'] = pygame.mixer.Sound(os.path.join(BASE_DIR,'sounds','zvuki-lesa.mp3'))
    return assets
if __name__ == '__main__': #проверка главный ли это файл, эта строка выводится только в этом файле
    loaded = load_assets()
    print("Загруженно ключей: ",list(loaded.keys()))
    print("Привет, я assets.py! Моё имя:", __name__)