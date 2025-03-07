import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Braxbuistin')

jumpy_image = pygame.image.load('Assets/pixil-frame-0.png').convert_alpha()
bg_image = pygame.image.load('Assets/PygameBG.webp').convert_alpha()

class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(jumpy_image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)




      
jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

run = True
while run:

    screen.blit(bg_image, (0, 0))

    jumpy.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    



pygame.quit()


        
