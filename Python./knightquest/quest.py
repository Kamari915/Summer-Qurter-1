import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zelda Full Game")
FPS = 60

WHITE = (255, 255, 255)
GREEN = (50, 168, 82)
RED = (200, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5
        self.health = 5
        self.mana = 5
        self.max_mana = 5
        self.gold = 0
        self.inventory = []
        self.is_attacking = False
        self.attack_cooldown = 0
        self.spell_cooldown = 0
        self.blocking = False

    def update(self, keys):
        dx = dy = 0
        if keys[pygame.K_LEFT]: dx = -self.speed
        if keys[pygame.K_RIGHT]: dx = self.speed
        if keys[pygame.K_UP]: dy = -self.speed
        if keys[pygame.K_DOWN]: dy = self.speed
        self.rect.x += dx
        self.rect.y += dy

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.spell_cooldown > 0:
            self.spell_cooldown -= 1

    def attack(self):
        if self.attack_cooldown == 0:
            self.is_attacking = True
            self.attack_cooldown = 30

    def block(self):
        self.blocking = True

    def stop_blocking(self):
        self.blocking = False

class Sword(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((180, 180, 180))
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center
        self.rect.y -= 30

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        self.speed = 2

    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((100, 0, 100))
        self.rect = self.image.get_rect(center=(WIDTH // 2, 100))
        self.health = 20
        self.speed = 2

    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

class BossProjectile(pygame.sprite.Sprite):
    def __init__(self, boss, player):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 100, 100))
        self.rect = self.image.get_rect(center=boss.rect.center)
        self.speed = 6
        dx = player.rect.x - boss.rect.x
        dy = player.rect.y - boss.rect.y
        distance = (dx**2 + dy**2) ** 0.5
        self.velocity = (dx / distance * self.speed, dy / distance * self.speed)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

class MagicSpell(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 200, 255))
        self.rect = self.image.get_rect(center=player.rect.center)
        self.speed = 8
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - player.rect.x
        dy = mouse_y - player.rect.y
        dist = (dx**2 + dy**2) ** 0.5
        self.velocity = (dx / dist * self.speed, dy / dist * self.speed)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

def draw_health(surface, health):
    for i in range(health):
        pygame.draw.rect(surface, RED, (10 + i * 25, 10, 20, 20))

def draw_mana(surface, mana, max_mana):
    for i in range(max_mana):
        color = (0, 200, 255) if i < mana else (50, 50, 50)
        pygame.draw.rect(surface, color, (10 + i * 25, 40, 20, 10))

def draw_inventory(surface, gold):
    font = pygame.font.SysFont("arial", 20)
    text = font.render(f"Gold: {gold}", True, WHITE)
    surface.blit(text, (WIDTH - 120, 10))

def save_game(player):
    with open("savefile.txt", "w") as f:
        f.write(f"{player.health},{player.mana},{player.gold}\n")

def load_game(player):
    try:
        with open("savefile.txt", "r") as f:
            data = f.read().split(",")
            player.health = int(data[0])
            player.mana = int(data[1])
            player.gold = int(data[2])
    except:
        pass

def main():
    clock = pygame.time.Clock()

    player = Player()
    sword_group = pygame.sprite.Group()
    magic_group = pygame.sprite.Group()

    enemies = pygame.sprite.Group([Enemy() for _ in range(5)])
    boss = None
    boss_projectiles = pygame.sprite.Group()
    boss_active = False

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(enemies)

    load_game(player)

    running = True
    while running:
        clock.tick(FPS)
        WIN.fill((20, 20, 40) if not boss_active else (50, 0, 0))

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game(player)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.attack()
                    sword_group.add(Sword(player))
                elif event.key == pygame.K_f:
                    if player.mana > 0 and player.spell_cooldown == 0:
                        magic_group.add(MagicSpell(player))
                        player.mana -= 1
                        player.spell_cooldown = 20
                elif event.key == pygame.K_b:
                    player.block()
                elif event.key == pygame.K_s:
                    save_game(player)
                elif event.key == pygame.K_l:
                    load_game(player)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_b:
                    player.stop_blocking()

        player.update(keys)
        enemies.update(player)

        if not boss_active and len(enemies) == 0:
            boss_active = True
            boss = Boss()
            all_sprites.add(boss)

        if boss_active:
            boss.update(player)
            boss_projectiles.update()
            if random.randint(1, 30) == 1:
                boss_projectiles.add(BossProjectile(boss, player))

        if player.is_attacking:
            for enemy in pygame.sprite.groupcollide(enemies, sword_group, True, False):
                player.gold += 1
            if boss and pygame.sprite.spritecollide(boss, sword_group, False):
                boss.health -= 1
            player.is_attacking = False
            sword_group.empty()

        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                if not player.blocking:
                    player.health -= 1
                enemies.remove(enemy)

        for projectile in boss_projectiles:
            if projectile.rect.colliderect(player.rect):
                if not player.blocking:
                    player.health -= 1
                boss_projectiles.remove(projectile)

        for enemy in pygame.sprite.groupcollide(enemies, magic_group, True, True):
            player.gold += 2

        if boss:
            if pygame.sprite.spritecollide(boss, magic_group, True):
                boss.health -= 1

        if boss and boss.health <= 0:
            print("YOU WIN!")
            save_game(player)
            pygame.quit()
            sys.exit()

        if player.health <= 0:
            print("GAME OVER")
            save_game(player)
            pygame.quit()
            sys.exit()

        all_sprites.draw(WIN)
        sword_group.update(player)
        sword_group.draw(WIN)
        magic_group.update()
        magic_group.draw(WIN)
        boss_projectiles.draw(WIN)

        draw_health(WIN, player.health)
        draw_mana(WIN, player.mana, player.max_mana)
        draw_inventory(WIN, player.gold)

        pygame.display.update()

main()