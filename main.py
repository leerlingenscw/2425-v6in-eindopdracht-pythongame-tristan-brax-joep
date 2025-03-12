import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Braxbuistin')

clock = pygame.time.Clock()
FPS = 60


WHITE = (255, 255, 255)


jumpy_image = pygame.image.load('Assets/pixil-frame-0.png').convert_alpha()
bg_image = pygame.image.load('Assets/PygameBG.webp').convert_alpha()

class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(jumpy_image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.flip = False
    
    def move(self):
        dx = 0
        dy = 0


        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -10
            self.flip = True
        if key[pygame.K_d]:
            dx = 10
            self.flip = False
        
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

          
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x -12, self.rect.y -5))
        pygame.draw.rect(screen, WHITE, self.rect, 2)




      
jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

run = True
while run:

    clock.tick(FPS)
    
    jumpy.move()

    screen.blit(bg_image, (0, 0))

    jumpy.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    



pygame.quit()


        
