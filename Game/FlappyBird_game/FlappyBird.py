import pygame, sys

def draw_floor():
    screen.blit(floor,(floor_x_pos, 450))
    screen.blit(floor,(floor_x_pos + 324, 450))
pygame.init() #Bắt buộc thêm đầu 
width_screen = 324
height_screen = 576
screen = pygame.display.set_mode((width_screen, height_screen))
clock = pygame.time.Clock()
# Chèn trọng lực
gravity = 0.25
bird_movement = 0
# Chèn background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale(bg, (324, 576))
# Chèn floor
floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale(floor, (324, 126))
floor_x_pos = 0
# Tạo chim
bird = pygame.image.load('assets/yellowbird-midflap.png').convert()
bird = pygame.transform.scale(bird, (51, 36))
bird_rect = bird.get_rect(center = (100, 288))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("chim")
    screen.blit(bg,(0, 0))
    bird_movement = gravity + 1
    bird_rect.centery = bird_movement + 1
    screen.blit(bird, bird_rect)
    floor_x_pos = floor_x_pos - 1
    draw_floor()
    if floor_x_pos <= -324:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)
    