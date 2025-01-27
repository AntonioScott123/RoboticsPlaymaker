import pygame

pygame.init()

#Setting up everything like the varibles and screen
width, height = 400, 400
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Robotics Playmaker")

clock = pygame.time.Clock()
run = True
allscrns = [1, 2]
prevscrn = 1
curscrn = 1
scrnChange = True
darkgray = (51, 51, 51)

#Making a button class so it is easy to make multiple buttons
class Button:
    def __init__(self, x, y, width, height, color, textColor, scrnID, text="", font_size=16, border_radius=10, font="Bubble.ttf"):
        self.rect = pygame.Rect(x - fNum(width, 50), y - fNum(height, 50), width, height)
        self.color = color
        self.textColor = textColor
        self.scrnID = scrnID
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.text_surface = self.font.render(self.text, True, textColor)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.border_radius = border_radius

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=self.border_radius)
        screen.blit(self.text_surface, self.text_rect)

#fnum so i can format and round the number so i can draw something on the screen where i want it
def fNum(x, num):
    return int(round(x * (num / 100)))

def homeScreen(screen):
    global Buttons, darkgray
    screen.fill((0,0,0))
    Buttons = [
        Button(fNum(width, 50), fNum(height, 50), fNum(width, 15), fNum(width, 15), darkgray, "white", 1, "Start Play", fNum(width, 3), fNum(width, 4)),
        Button(fNum(width, 66), fNum(height, 50), fNum(width, 10), fNum(width, 10), darkgray, "white", 1, "Load Play", fNum(width, 2), fNum(width, 3)),
        Button(fNum(width, 34), fNum(height, 50), fNum(width, 10), fNum(width, 10), darkgray, "white", 1, "Quit", fNum(width, 3), fNum(width, 3))
    ]

while run:
    width, height = screen.get_size()
    print(width, height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if curscrn == 1:
        homeScreen(screen)

    for butt in Buttons:
        if butt.scrnID == curscrn:
            if event.type == pygame.MOUSEBUTTONDOWN and butt.rect.colliderect(pygame.Rect(pygame.mouse.get_pos(), (1, 1))):
                butt.color = (81,81,81)
                mouseup = True
            else:
                butt.color = darkgray
        
            butt.draw(screen)

    if prevscrn != curscrn:
        scrnChange = True
    else:
        scrnChange = False

    #Button Handling

    clock.tick(60)

    pygame.display.flip()
pygame.quit()
