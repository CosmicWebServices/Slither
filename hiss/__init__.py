import pygame, time, random
# time is for the timer.
# random is for random numbers.

sprites = [] # List of sprites
    
class Stage():
    def __init__(self):
        self.costumes = []
        self.costumeNumber = 0
        self.currentCostume = False
        self.bgColor = (255, 255, 255)

    def addCostume(self, costumePath):
        costume = pygame.image.load(costumePath)
        self.costumes.append(costume)

    def setColor(self, r, g, b):
        self.bgColor = (r, g, b)

    def setCostumeByNumber(self, number):
        if number < len(self.costumes):
            self.currentCostume = self.costumes[number]


hissStage = Stage()
                                       

class Sprite(Stage):
    def __init__(self, name="Default Name"):
        Stage.__init__(self)
        self.name = name # Why is this here?
        self.xpos = 0
        self.ypos = 0
        self.direction = 0 # Default is 0, not 90 - it makes more sense
        self.showing = True
        sprites.append(self)
        
    def show(self):
        self.show = True
        
    def hide(self):
        self.show = False

    def changeXBy(self, amount):
        self.xpos += amount

    def changeYBy(self, amount):
        self.ypos += amount

    def goTo(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def setXTo(self, xpos):
        self.xpos = xpos

    def setYTo(self, ypos):
        self.ypos = ypos

pygame.init()
screen = pygame.display.set_mode((800, 600)) # Add customizable dimensions later on?
caption = pygame.display.set_caption("Hiss Project")
time.clock()

def blit():
    screen.fill(hissStage.bgColor)
    
    for obj in sprites:
        if obj.showing:
            screen.blit(obj.currentCostume, (obj.xpos, obj.ypos))

    pygame.display.flip()
    
