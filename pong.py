# pong!
import pygame, sys
from pygame import gfxdraw

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

scorep1 = 0
scorep2 = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))

pygame.init()

class Bar(pygame.sprite.Sprite):
    "This is the bar class"

    def __init__(self, x, y, w=10, h=60):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self):
        self.y = pygame.mouse.get_pos()[1]
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, RED, self.rect)


bar1 = Bar(0, 0)
bar2 = Bar(490, 0)
class Ball:
    "Draw the ball"

    def __init__(self, x, y):
        self.dirh = 0
        self.dirv = 0
        self.speed = 5
        self.x = x
        self.y = y
        # self.rect = pygame.Rect(self.x, self.y, 10, 10)

    def update(self):
        
        if self.dirh == 0:
            self.x -= self.speed
        if self.dirv == 0:
            self.y += self.speed
            if self.y > 490:
                self.dirv = 1
        if self.dirv:
            self.y -= self.speed
            if self.y < self.speed:
                self.dirv = 0
        if self.dirh:
            self.x += self.speed
        gfxdraw.filled_circle(screen, self.x, self.y, 5, (0, 255, 0))
        self.rect = pygame.Rect(self.x, self.y, 10, 10)

ball = Ball(480, 20)



def collision():
    global scorep1, scorep2

    pygame.display.set_caption(
        f"Player 1: {scorep1} - Player 2: {scorep2}")

    if ball.rect.colliderect(bar2):
        ball.dirh = 0  
    if ball.rect.colliderect(bar1):
        ball.dirh = 1
    if ball.x > 500:
        ball.x, ball.y = 10, 20
    if ball.x < 0:
        gfxdraw.filled_circle(screen, ball.x, ball.y, 5, (0, 0, 0))
        ball.x, ball.y = 480, 20


pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

def pause():
    loop = 1
    write("PAUSED", 500, 150)
    write("Press Space to continue", 500, 250)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    loop = 0
        pygame.display.update()
        # screen.fill((0, 0, 0))
        clock.tick(60)


def start():
    loop = 1
    while loop:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    pause()
        gfxdraw.filled_circle(screen, ball.x, ball.y, 5, (0, 0, 0))
        ball.update()
        pygame.draw.rect(screen, BLACK, bar1.rect)
        bar1.update()
        pygame.draw.rect(screen, BLACK, bar2.rect)
        bar2.update()
        collision()
        pygame.display.update()
        # screen.fill((0, 0, 0))
        clock.tick(60)

    pygame.quit()
    sys.exit()


font = pygame.font.SysFont("Arial", 24)


def write(text, x, y, color="Coral",):
    "Put text centered on the screen"
    # remeber to:
    # font = pygame.font.SysFont("Arial", 24)
    text = font.render(text, 1, pygame.Color(color))
    text_rect = text.get_rect(center=(500 // 2, y))
    screen.blit(text, text_rect)
    return text

def menu():
    loop = 1
    write("PONG 2020", 500, 150)
    write("Press Space to start", 500, 250)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    start()

        pygame.display.update()
        # screen.fill((0, 0, 0))
        clock.tick(60)

    pygame.quit()
    sys.exit()

menu()