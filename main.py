import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка параметров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

# Установка параметров мишени
target_image = pygame.image.load("img/target.png")
target_width = 40
target_height = 40

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона и шрифта
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
white = (255, 255, 255)

# Переменные для игры
score = 0
clock = pygame.time.Clock()


# Класс для мишени
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = target_image
        self.rect = self.image.get_rect()
        self.rect.center = ((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.target_pos = (target_x, target_y)

    def update(self):
        if self.rect.centerx < self.target_pos[0]:
            self.rect.centerx += 1
        elif self.rect.centerx > self.target_pos[0]:
            self.rect.centerx -= 1

        if self.rect.centery < self.target_pos[1]:
            self.rect.centery += 1
        elif self.rect.centery > self.target_pos[1]:
            self.rect.centery -= 1

        if self.rect.center == self.target_pos:
            self.target_pos = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

# Группы спрайтов
all_sprites = pygame.sprite.Group()
targets = pygame.sprite.Group()

# Добавление мишени в группы
for _ in range(3):
    target = Target()
    all_sprites.add(target)
    targets.add(target)

# Основной игровой цикл
running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for target in targets:
                if target.rect.collidepoint(event.pos):
                    score += 1
                    target.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

    all_sprites.update()
    all_sprites.draw(screen)

    # Вывод очков на экран
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True,  white)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(300)

pygame.quit()
