# Pygame skeleton for a new pygame project
import pygame
import random

WIDTH = 512
HEIGHT = 512
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
SIZE = 32
colors = [WHITE, BLACK, RED, GREEN, BLUE, PINK, YELLOW]
# init pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
# other variabales
pos_x = [WIDTH / 2]
pos_y = [HEIGHT / 2]
tailSize = 0


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x * SIZE
        self.rect.y = y * SIZE
        self.x = 0
        self.y = 0
        self.tail = 0

    def move(self, sx, sy):
        self.x += sx
        self.y += sy

    def update(self):
        self.rect.x += self.x * SIZE
        self.rect.y += self.y * SIZE
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
        if self.rect.top < 0:
            self.rect.bottom = HEIGHT
        global pos_x, pos_y
        pos_x[0] = self.rect.x
        pos_y[0] = self.rect.y


class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - 1) * SIZE
        self.rect.y = random.randrange(0, HEIGHT - 1) * SIZE


class Tail(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        global pos_x, pos_y
        self.rect.x = x + 30
        self.rect.y = y + 30
        self.last_update = 0
        pos_x.append(self.rect.x)
        pos_y.append(self.rect.y)
        self.size = size
        self.speedx = 0
        self.speedy = 0

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            global pos_x, pos_y
            pos_x[self.size] = self.rect.x
            pos_y[self.size] = self.rect.y
            self.rect.x = pos_x[self.size - 1] + 30
            self.rect.y = pos_y[self.size - 1]


def draw_grid(screen):
    for x in range(0, WIDTH, SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))


# making all the sprites
all_sprites = pygame.sprite.Group()
# adding the snake
snake = Snake(0, 0)
all_sprites.add(snake)
# adding the fruits
fruits = pygame.sprite.Group()
fruit = Fruit()
fruits.add(fruit)
all_sprites.add(fruit)
# adding the Tail
tails = pygame.sprite.Group()
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Procces input(events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            snake.move(-1, 0)
        if keystate[pygame.K_RIGHT]:
            snake.move(1, 0)
        if keystate[pygame.K_UP]:
            snake.move(0, -1)
        if keystate[pygame.K_DOWN]:
            snake.move(0, 1)
    # Update
    all_sprites.update()
    # if tails != 0:
    #    hits = pygame.sprite.spritecollide(snake, tails, False)
    #    if hits:
    #        running = False
    hits = pygame.sprite.spritecollide(snake, fruits, True)
    if hits:
        fruit = Fruit()
        all_sprites.add(fruit)
        fruits.add(fruit)
        tailSize += 1
        tail = Tail(pos_x[tailSize - 1],
                    pos_y[tailSize - 1], tailSize)
        print(pos_x, pos_y)
        tails.add(tail)
        all_sprites.add(tail)

    # Draw / render
    screen.fill(CYAN)
    draw_grid(screen)
    all_sprites.draw(screen)
    # after drawing everything
    pygame.display.flip()

pygame.quit()
