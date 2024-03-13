import pygame
import random

SIZE_BLOCK  = 20
FRAME_COLOR = (0, 255, 204)
WHITE =     (255, 255, 255)
BLUE  =     (205, 255, 255)
RED   =     (225, 10, 10)
HEADER_COLOR = (0, 205, 155)
SNAKE_COLOR  = (0, 105, 0)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1

size = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Вуж :)')
timer = pygame.time.Clock()

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

def draw_block(color, row, column):
    pygame.draw.rect(screen, color,
                     [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                      HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                      SIZE_BLOCK, SIZE_BLOCK])

snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
apple = SnakeBlock(random.randint(0, COUNT_BLOCKS - 1), random.randint(0, COUNT_BLOCKS - 1))
d_row = 0
d_col = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, column)

    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    draw_block(RED, apple.x, apple.y)

    head = snake_blocks[-1]
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)

    # Перевірка зіткнення з межами поля
    if not new_head.is_inside():
        # Якщо зіткнулась, то кінець гри
        print("Кінець гри!")
        pygame.quit()

    # Перевірка поїдання ягоди
    if new_head == apple:
        apple = SnakeBlock(random.randint(0, COUNT_BLOCKS - 1), random.randint(0, COUNT_BLOCKS - 1))
        snake_blocks.append(new_head)

    else:
        snake_blocks.append(new_head)
        snake_blocks.pop(0)

    pygame.display.flip()
    timer.tick(5)  # Кількість кадрів за секунду