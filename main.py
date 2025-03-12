import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Braxbuitin')

clock = pygame.time.Clock()
FPS = 60

SCROLL_THRESH  = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0

WHITE = (255, 255, 255)


jumpy_image = pygame.image.load('Assets/pixil-frame-0.png').convert_alpha()
bg_image = pygame.image.load('Assets/PygameBG.webp').convert_alpha()
platform_image = pygame.image.load('Assets/PLATFORM.png').convert_alpha()

def draw_bg(bg_scroll):
     screen.blit(bg_image, (0, 0 + bg_scroll))
     screen.blit(bg_image, (0, 0 + bg_scroll))

class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(jumpy_image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False
    
    def move(self):
        scroll = 0
        dx = 0
        dy = 0


        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -10
            self.flip = True
        if key[pygame.K_d]:
            dx = 10
            self.flip = False

        self.vel_y += GRAVITY
        dy += self.vel_y
        
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20
        
        if self.rect.bottom + dy > SCREEN_HEIGHT:
            dy = 0
            self.vel_y = -20
        
        if self.rect.top <= SCROLL_THRESH:
            if self.vel_y < 0:
                scroll = -dy

          
        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x -12, self.rect.y -5))
        pygame.draw.rect(screen, WHITE, self.rect, 2)




class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):

        self.rect.y += scroll






jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

platform_group = pygame.sprite.Group()

for p in range(MAX_PLATFORMS):
    p_w = random.randint(40, 60)
    p_x = random.randint(0, SCREEN_WIDTH - p_w)
    p_y = p * random.randint(80, 120)
    platform = Platform(p_x, p_y, p_w)
    platform_group.add(platform)


run = True
while run:

    clock.tick(FPS)
    
    scroll = jumpy.move()

    print(scroll)

    bg_scroll += scroll
    draw_bg(bg_scroll)

    platform_group.update(scroll)

    platform_group.draw(screen)
    jumpy.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    



pygame.quit()


        
