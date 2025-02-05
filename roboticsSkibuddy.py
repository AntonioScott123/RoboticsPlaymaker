import pygame
import math

pygame.init()

#Setting up everything like the varibles and screen
w, h = 400, 400
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption("Robotics Playmaker")

clock = pygame.time.Clock()
run = True
allscrns = [1, 2]
Pieces = []
prevscrn = 1
curscrn = 1
scrnChange = True
darkgray = (51, 51, 51)
mouseup = False
openWind = False
followPiece = None
follow = False
fieldLimit = None

#Making a button class so it is easy to make multiple buttons
class Button:
    def __init__(self, x, y, w, h, color, textColor, scrnID, text="", font_size=16, border_radius=10, font="Bubble.ttf"):
        self.rect = pygame.Rect(x - fNum(w, 50), y - fNum(h, 50), w, h)
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

class gamePieces:
    def __init__(self, typeOfPiece, x, y):
        self.type = typeOfPiece
        self.hit = pygame.Rect(0, 0 , 1, 1)
        self.x = x
        self.y = y

    def followMouse(self, xBool, yBool):
        if xBool:
            self.x = pygame.mouse.get_pos()[0]
        if yBool:
            self.y = pygame.mouse.get_pos()[1]

    def draw(self,screen):
        if self.type == "coral":
            self.hit = pygame.Rect(self.x - fNum(w, 1.5), self.y - fNum(w, 1.5), fNum(w, 3), fNum(w, 3))
            pygame.draw.circle(screen, (241, 241, 241), (self.x, self.y), fNum(w, 1.5))
            pygame.draw.circle(screen, (190, 190, 190), (self.x, self.y), fNum(w, 1))

        elif self.type == "algae":
            self.hit = pygame.Rect(self.x - fNum(w, 2), self.y - fNum(w, 2), fNum(w, 4), fNum(w, 4))
            pygame.draw.circle(screen, (0, 220, 180), (self.x, self.y), fNum(w, 2))
            pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), fNum(w, 2), fNum(w, .25))

#fnum so i can format and round the number so i can draw something on the screen where i want it
def fNum(x, num):
    return int(round(x * (num / 100)))

def homeScreen(screen):
    global Buttons, darkgray
    screen.fill((0,0,0))
    Buttons = [
        Button(fNum(w, 50), fNum(h, 50), fNum(w, 15), fNum(w, 15), darkgray, "white", 1, "Start Play", fNum(w, 3), fNum(w, 4)),
        Button(fNum(w, 66), fNum(h, 50), fNum(w, 10), fNum(w, 10), darkgray, "white", 1, "Load Play", fNum(w, 2), fNum(w, 3)),
        Button(fNum(w, 34), fNum(h, 50), fNum(w, 10), fNum(w, 10), darkgray, "white", 1, "Quit", fNum(w, 3), fNum(w, 3))
    ]

def fieldScreen(screen, win):
    global darkgray, Buttons, fieldLimit
    screen.fill((255,255,255))
    fieldLimit = pygame.Rect(0,0,fNum(w, 99),fNum(w, 99) // 2.25)
    fieldLimit.center = (fNum(w, 50), fNum(h, 50))
    pygame.draw.rect(screen, (31,31,31), fieldLimit, int(math.ceil((w + h) *.00277)))
    pygame.draw.line(screen,(31,31,31), (fNum(w, 45), fieldLimit.top), (fNum(w, 45), fieldLimit.bottom), int(math.ceil((w + h) *.00277)))
    pygame.draw.line(screen,(31,31,31), (fNum(w, 55), fieldLimit.top), (fNum(w, 55), fieldLimit.bottom), int(math.ceil((w + h) *.00277)))
    Buttons = [
        Button(fNum(w, 9), fNum(h, 95.9), fNum(w, 12), fNum(w, 4), darkgray, "white", 2, "Game Element", fNum(w, 1), fNum(w, 2)),
        Button(fNum(w, 7), fNum(h, 4.1), fNum(w, 10), fNum(w, 4), darkgray, "white", 2, "Quit", fNum(w, 1), fNum(w, 2))
    ]
    if win:
        Buttons.append(Button(fNum(w, 6), fNum(h, 75), fNum(w, 6), fNum(h, 8), darkgray, "white", 2, "A", fNum(w, 1), fNum(h, 4)))
        Buttons.append(Button(fNum(w, 14), fNum(h, 75), fNum(w, 6), fNum(h, 6), darkgray, "white", 2, "C", fNum(w, 1), fNum(h, 4)))

def openWin(screen):
    screen.blit(window, (fNum(w, -2), h // 1.7))
    pygame.draw.circle(screen, (0, 220, 180), (fNum(w, 6), fNum(h, 75)), fNum(w, 2))
    pygame.draw.circle(screen, (0, 0, 0), (fNum(w, 6), fNum(h, 75)), fNum(w, 2), fNum(w, .25))

    pygame.draw.circle(screen, (241, 241, 241), (fNum(w, 14), fNum(h, 75)), fNum(w, 1.5))
    pygame.draw.circle(screen, (190, 190, 190), (fNum(w, 14), fNum(h, 75)), fNum(w, 1))

while run:
    w, h = screen.get_size()
    window = pygame.transform.scale(pygame.image.load("window.png").convert_alpha(), (fNum(w, 23), fNum(h, 40)))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if curscrn == 1:
        homeScreen(screen)
    elif curscrn == 2:
        fieldScreen(screen, openWind)

        
    if prevscrn != curscrn:
        scrnChange = True
        if curscrn == 2:
            Pieces.append(gamePieces("algae", fNum(fieldLimit.width, 90) + fieldLimit.left, fNum(fieldLimit.height, 50) + fieldLimit.top))
            Pieces.append(gamePieces("algae", fNum(fieldLimit.width, 90) + fieldLimit.left, fNum(fieldLimit.height, 75) + fieldLimit.top))
            Pieces.append(gamePieces("algae", fNum(fieldLimit.width, 90) + fieldLimit.left, fNum(fieldLimit.height, 25) + fieldLimit.top))
            Pieces.append(gamePieces("coral", fNum(fieldLimit.width, 90) + fieldLimit.left, fNum(fieldLimit.height, 50) + fieldLimit.top))
            Pieces.append(gamePieces("coral", fNum(fieldLimit.width, 90) + fieldLimit.left, fNum(fieldLimit.height, 75) + fieldLimit.top))
            Pieces.append(gamePieces("coral", fNum(fieldLimit.width, 90) + fieldLimit.left, fNum(fieldLimit.height, 25) + fieldLimit.top))

            Pieces.append(gamePieces("algae", fNum(fieldLimit.width, 10) + fieldLimit.left, fNum(fieldLimit.height, 50) + fieldLimit.top))
            Pieces.append(gamePieces("algae", fNum(fieldLimit.width, 10) + fieldLimit.left, fNum(fieldLimit.height, 75) + fieldLimit.top))
            Pieces.append(gamePieces("algae", fNum(fieldLimit.width, 10) + fieldLimit.left, fNum(fieldLimit.height, 25) + fieldLimit.top))
            Pieces.append(gamePieces("coral", fNum(fieldLimit.width, 10) + fieldLimit.left, fNum(fieldLimit.height, 50) + fieldLimit.top))
            Pieces.append(gamePieces("coral", fNum(fieldLimit.width, 10) + fieldLimit.left, fNum(fieldLimit.height, 75) + fieldLimit.top))
            Pieces.append(gamePieces("coral", fNum(fieldLimit.width, 10) + fieldLimit.left, fNum(fieldLimit.height, 25) + fieldLimit.top))
            
            
        print("change")
    else:
        scrnChange = False

    for butt in Buttons:
        if butt.scrnID == curscrn:
            if pygame.mouse.get_pressed()[0] and butt.rect.colliderect(pygame.Rect(pygame.mouse.get_pos(), (1, 1))):
                butt.color = (81,81,81)
                mouseup = True
            else:
                butt.color = darkgray

            prevscrn = curscrn
        
            butt.draw(screen)
            if mouseup:
                if not pygame.mouse.get_pressed()[0]:
                    openWind = False
                    if butt.rect.colliderect(pygame.Rect(pygame.mouse.get_pos(), (1, 1))):
                        if butt.text == "Start Play":
                            curscrn = 2
                        elif butt.text == "Quit":
                            run = False
                        elif butt.text == "Game Element":
                            openWind = True
                        elif butt.text == "A":
                            Pieces.append(gamePieces("algae", fNum(w, 50), fNum(h, 50)))
                        elif butt.text == "C":
                            Pieces.append(gamePieces("coral", fNum(w, 50), fNum(h, 50)))
                        mouseup = False
        

    if openWind:
        openWin(screen)

    for piece in Pieces:
        Pieces[len(Pieces) - (Pieces.index(piece) + 1)].draw(screen)
        if not follow:
            if piece.hit.colliderect(pygame.Rect(pygame.mouse.get_pos(), (1, 1))) and pygame.mouse.get_pressed()[0]:
                followPiece = piece
                follow = True
    
    if follow:
        Pieces.remove(followPiece)
        Pieces.insert(0, followPiece)
        xFollow = True
        yFollow = True
        if pygame.mouse.get_pos()[1] < fieldLimit.top:
            followPiece.y = fieldLimit.top
            yFollow = False
        elif pygame.mouse.get_pos()[1] > fieldLimit.bottom:
            followPiece.y = fieldLimit.bottom
            yFollow = False
        if pygame.mouse.get_pos()[0] < fieldLimit.left:
            followPiece.x = fieldLimit.left
            xFollow = False
        if pygame.mouse.get_pos()[0] > fieldLimit.right:
            followPiece.x = fieldLimit.right
            xFollow = False

        followPiece.followMouse(xFollow, yFollow)

    
    if not pygame.mouse.get_pressed()[0]:
            follow = False
            followPiece = None

    

    clock.tick(60)

    pygame.display.flip()
pygame.quit()
