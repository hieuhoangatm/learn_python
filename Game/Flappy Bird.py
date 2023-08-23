import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cài đặt giao diện trò chơi
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Cài đặt fonts
font = pygame.font.Font(None, 36)

# Tạo con chim
bird = pygame.Rect(100, height // 2, 50, 50)
bird_speed = 0
gravity = 1

# Tạo ống nước
pipes = []
pipe_speed = 4
pipe_gap = 200
pipe_frequency = 120
last_pipe_time = pygame.time.get_ticks()

# Điểm số
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -15

    # Di chuyển con chim
    bird_speed += gravity
    bird.y += bird_speed

    # Tạo ống nước mới
    if pygame.time.get_ticks() - last_pipe_time > pipe_frequency:
        pipe_height = random.randint(100, 400)
        pipes.append(pygame.Rect(width, 0, 50, pipe_height))
        pipes.append(pygame.Rect(width, pipe_height + pipe_gap,
                     50, height - pipe_height - pipe_gap))
        last_pipe_time = pygame.time.get_ticks()

    # Di chuyển ống nước
    for pipe in pipes:
        pipe.x -= pipe_speed

    # Loại bỏ ống nước đã đi qua màn hình
    pipes = [pipe for pipe in pipes if pipe.x > -50]

    # Kiểm tra va chạm
    for pipe in pipes:
        if bird.colliderect(pipe):
            running = False

    # Kiểm tra nếu con chim chạm màn hình
    if bird.y > height or bird.y < 0:
        running = False

    # Tính điểm số
    if pipes and bird.x > pipes[0].x + pipes[0].width:
        pipes.pop(0)
        pipes.pop(0)
        score += 1

    # Vẽ màn hình
    screen.fill(white)
    pygame.draw.rect(screen, blue, bird)
    for pipe in pipes:
        pygame.draw.rect(screen, black, pipe)
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
