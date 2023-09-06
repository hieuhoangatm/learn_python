import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cài đặt cửa sổ trò chơi
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gold Miner Game")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)

# Font
font = pygame.font.Font(None, 36)

# Hàm để hiển thị màn hình bắt đầu
def show_start_screen():
    screen.fill(BLACK)
    start_text = font.render("Start", True, WHITE)
    screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

# Gọi hàm hiển thị màn hình bắt đầu
show_start_screen()

# Khởi tạo người chơi
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_speed = 5

# ... (phần còn lại của mã trò chơi)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # ... (phần còn lại của vòng lặp game)

pygame.quit()
