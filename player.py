import pygame


from settings import PLAYER_START_X, PLAYER_START_Y, PLAYER_SPEED, PLAYER_MAX_HP, PLAYER_MAX_AMMO, BULLET_SPEED, \
    SHOOT_COOLDOWN_FRAMES, JUMP_START_COUNT, JUMP_MIN_COUNT,ANIM_DELAY,JUMP_DELAY

from bullet import Bullet

class Player:
    def __init__(self, assets):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.speed = PLAYER_SPEED
        self.hp = PLAYER_MAX_HP
        self.ammo = PLAYER_MAX_AMMO
        self.anim_count = 0
        self.jump_count = JUMP_START_COUNT
        self.is_jump = False
        self.direction = 1
        self.assets = assets
        self.anim_timer = 0
        self.jump_timer = 0
        self.bullets = [] #список пуль
        self.shoot_cooldown = 0 #таймер кулдауна
    def move(self,keys):
        if keys[pygame.K_LEFT] and self.x > 10:
            self.x -= self.speed
            self.direction = -1
        elif keys[pygame.K_RIGHT] and self.x < 630:
            self.x += self.speed
            self.direction = 1
    def jump(self,keys):
        if not self.is_jump: # Игрок не в прыжке?
            if keys[pygame.K_SPACE]:
                self.is_jump = True
        else:
            if self.jump_count >= JUMP_MIN_COUNT: # Игрок летит?
                if self.jump_count > 0:
                    self.y -=(self.jump_count ** 2) / 2
                else:
                    self.y +=(self.jump_count ** 2) / 2
                self.jump_timer += 1
                if self.jump_timer >= JUMP_DELAY:
                    self.jump_timer = 0
                    self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = JUMP_START_COUNT
                self.jump_timer = 0
                self.jump_count = JUMP_START_COUNT

    def update(self,keys):
        self.move(keys)
        self.jump(keys)
        self.anim_timer += 1
        if self.anim_timer == 3:
            self.anim_timer = 0
            if self.anim_count == 3:
                self.anim_count = 0
            else:
                self.anim_count += 1
        self.shoot(keys)


    def draw(self,screen):
        if self.direction == -1:
            screen.blit(self.assets['walk_left'][self.anim_count],(self.x,self.y))
        else:
            screen.blit(self.assets['walk_right'][self.anim_count],(self.x,self.y))

    def shoot(self, keys):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            return
        if keys[pygame.K_j]:
            new_bullet = Bullet(self.x - 30, self.y + 80, -1, self.assets['bullet'])
            self.bullets.append(new_bullet)
            self.shoot_cooldown = SHOOT_COOLDOWN_FRAMES
        if keys[pygame.K_l]:
            new_bullet_right = Bullet(self.x + 30, self.y + 80, 1, self.assets['bullet'])
            self.bullets.append(new_bullet_right)
            self.shoot_cooldown = SHOOT_COOLDOWN_FRAMES





