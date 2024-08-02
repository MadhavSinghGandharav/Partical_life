import pygame
import sys
import random
import numpy




# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 120

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("LIFE")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()




# Partical class
class Partical():
    def __init__(self,color):
        self.color = color
        self.position = numpy.array([random.randint(0,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT)]).astype("float")
        self.velocity = numpy.array([0.0,0.0])

    def draw(self):
        pygame.draw.circle(screen,colors[self.color],self.position,2)
    
    def update_position(self):
        self.position += self.velocity


# Helper Functions

def Render(particals):
    for i in particals:
        i.draw()

def create_particals(color,quantity):
    p=[]
    for _ in range(quantity):
        a=Partical(color)
        p.append(a)
        particals.append(a)
    return p


def simulate(p1):
    for i in p1:
        vec=0.0
        for j in p1:
            if i is not j:

                dxy = i.position - j.position
                distance = numpy.linalg.norm(dxy)
                attraction = relation[i.color][j.color]
                if (distance > 200):
                    continue
                elif (distance <= 10):
                    force = -(0.05 * distance - 1)
                else:
                    force = attraction/distance
                vec += force*dxy/distance
        i.velocity += vec

        if i.position[0] <=0 or i.position[0]>=SCREEN_WIDTH:
            i.velocity[0] *=-1 
        if i.position[1] <=0 or i.position[1]>=SCREEN_HEIGHT:
            i.velocity[1] *=-1 
        i.velocity = numpy.clip(i.velocity,-3,3)
        i.update_position()


def display_fps(screen, clock):
    # Calculate FPS
    fps = str(int(clock.get_fps()))
    
    # Render the FPS text
    fps_text = font.render(fps, True, pygame.Color('white'))
    
    # Blit the FPS text onto the screen
    screen.blit(fps_text, (10, 10))
          
# Variables
colors = [(43, 207, 255) ,(179, 251, 50),(255, 50, 155)] # blue green pink
font = pygame.font.SysFont(None, 30)
particals=[]
relation = [[-1,0,0],[-0,-1,0],[0,0,-1]]

# creating particals
create_particals(0,50)
create_particals(1,50)
create_particals(2,50)
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state

   
    screen.fill(BLACK)
    simulate(particals)
    
    Render(particals)
   # display_fps(screen,clock)
    pygame.display.update()

    
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()
