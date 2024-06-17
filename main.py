import pygame
import random

# Инициализация всех модулей Pygame
pygame.init()

# Установка размеров окна игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Установка заголовка окна игры
pygame.display.set_caption("Игра Тир")

# Загрузка и установка иконки для окна игры
icon = pygame.image.load(
    "img/200_strelkovyy-tir-neobhodim-tolko-v-teh-shkolah-gde-realizuetsya-profilnoe-obuchenie-po-obzh.png")
pygame.display.set_icon(icon)

# Загрузка изображения цели
target_img = pygame.image.load("img/klipartz.com.png")

# Установка размеров цели
target_width = 80
target_height = 80

# Случайное начальное положение цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Случайный фон
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Переменные для хранения счета и уровня
score = 0
level = 1

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

# Начальная скорость движения цели
target_speed_x = 0.2
target_speed_y = 0.2

# Основной игровой цикл
running = True
while running:
    # Заливка экрана случайным цветом
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        # Проверка на выход из игры
        if event.type == pygame.QUIT:
            running = False
        # Проверка на нажатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания по цели
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Перемещение цели в новое случайное положение
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Увеличение счета
                score += 1
                # Повышение уровня и увеличение скорости каждые 3 попадания
                if score % 3 == 0:
                    level += 1
                    target_speed_x *= 1.9
                    target_speed_y *= 1.9

    # Перемещение цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка столкновения цели с границами окна и изменение направления движения
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    # Отображение счета и уровня на экране
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    # Отображение цели на экране
    screen.blit(target_img, (target_x, target_y))

    # Обновление экрана
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()
