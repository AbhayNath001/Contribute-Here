import pygame
pygame.init()
pygame.display.set_caption("Abhay Nath")

from implementation import WIDTH, HEIGHT, FPS
from implementation import Player, Block, Block_1, Block_2, Fire, get_background, draw, handle_move


def lvl_1(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    block_size = 96

    player = Player(100, 100, 50, 50)       #100,100,50,50
    fire = Fire(510, HEIGHT - block_size - 324, 16, 32)
    fire1 = Fire(1110, HEIGHT - block_size - 64, 16, 32)
    fire2 = Fire(1510, HEIGHT - block_size - 324, 16, 32)
    fire.on(),fire1.on(),fire2.on()
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 1) // block_size)]
    objects = [*floor,Block(block_size * 1, HEIGHT - block_size * 3.7, block_size),fire,fire1,fire2,
               Block(block_size * 2, HEIGHT - block_size * 3.7, block_size),
               Block(block_size * 3, HEIGHT - block_size * 3.7, block_size),
               Block(block_size * 4, HEIGHT - block_size * 3.7, block_size),
               Block(block_size * 5, HEIGHT - block_size * 3.7, block_size),
               Block(block_size * 6, HEIGHT - block_size * 3.7, block_size),
               
               Block(block_size * 8, HEIGHT - block_size * 6, block_size),
               Block(block_size * 9, HEIGHT - block_size * 6, block_size),
               Block(block_size * 10, HEIGHT - block_size * 6, block_size),
               
               Block(block_size * 13, HEIGHT - block_size * 3.7, block_size),
               Block(block_size * 14, HEIGHT - block_size * 3.7, block_size),
               Block(block_size * 15, HEIGHT - block_size * 3.7, block_size),
               Block(block_size * 16, HEIGHT - block_size * 3.7, block_size),
               
               Block(block_size * 20, HEIGHT - block_size * 3.7, block_size),
               
               Block(block_size * 25, HEIGHT - block_size * 6, block_size),
               Block(block_size * 26, HEIGHT - block_size * 6, block_size),
               Block_1(block_size * 27, HEIGHT - block_size * 6, block_size),
               Block(block_size * 28, HEIGHT - block_size * 6, block_size),
               Block(block_size * 29, HEIGHT - block_size * 6, block_size),
               Block(block_size * 30, HEIGHT - block_size * 6, block_size),
               
               Block(block_size * 33, HEIGHT - block_size * 1, block_size),
               Block(block_size * 38, HEIGHT - block_size * 3, block_size),
               Block(block_size * 40, HEIGHT - block_size * 5.5, block_size),
               Block_1(block_size * 41, HEIGHT - block_size * 5.5, block_size),
               Block(block_size * 42, HEIGHT - block_size * 5.5, block_size),
               Block(block_size * 43, HEIGHT - block_size * 5.5, block_size),
               
               Block_2(block_size * 46, HEIGHT - block_size * 4, block_size),
               Block_2(block_size * 47, HEIGHT - block_size * 4, block_size),
               Block_2(block_size * 47, HEIGHT - block_size * 6, block_size),
               Block_2(block_size * 47, HEIGHT - block_size * 7, block_size),
               Block_2(block_size * 47, HEIGHT - block_size * 8, block_size),
               Block_2(block_size * 47, HEIGHT - block_size * 9, block_size),
               Block_2(block_size * 47, HEIGHT - block_size * 10, block_size),
               Block_2(block_size * 47, HEIGHT - block_size * 3, block_size),
               Block_2(block_size * 47, HEIGHT - block_size * 2, block_size),
               Block_2(block_size * 47, HEIGHT - block_size * 1, block_size),
               Block_2(block_size * 48, HEIGHT - block_size * 4, block_size),
               Block_2(block_size * 48, HEIGHT - block_size * 3, block_size),
               Block_2(block_size * 48, HEIGHT - block_size * 2, block_size),
               Block_2(block_size * 48, HEIGHT - block_size * 1, block_size),
               Block_2(block_size * 50, HEIGHT - block_size * 3, block_size),
               Block_2(block_size * 50, HEIGHT - block_size * 2, block_size),
               Block_2(block_size * 50, HEIGHT - block_size * 1, block_size),
               Block_2(block_size * 49, HEIGHT - block_size * 3, block_size),
               Block_2(block_size * 49, HEIGHT - block_size * 2, block_size),
               Block_2(block_size * 49, HEIGHT - block_size * 1, block_size),
               Block_2(block_size * 51, HEIGHT - block_size * 2, block_size),
               Block_2(block_size * 52, HEIGHT - block_size * 2, block_size),
               Block_2(block_size * 51, HEIGHT - block_size * 1, block_size),
               Block_2(block_size * 52, HEIGHT - block_size * 1, block_size),
               Block_2(block_size * 53, HEIGHT - block_size * 1, block_size),
               Block_2(block_size * 54, HEIGHT - block_size * 1, block_size),
               Block_2(block_size * 55, HEIGHT - block_size * 1, block_size),
               ]

    offset_x = 0         #0
    scroll_area_width = 900

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        fire.loop(),fire1.loop(),fire2.loop()
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()