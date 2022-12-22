import pygame
import pygame.locals 
from button import button, text

#initializing pygame
pygame.init()

#setting screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#creating game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stat Tracker")

#creating text for title

screen.fill((0,0,0))
pygame.font.init()
textfont = pygame.font.SysFont("monospace", 50)

textTBR = textfont.render("STAT TRACKER", 1, (255,255,255))
screen.blit(textTBR, (220, 10))

# create a surface object, image is drawn on it.
imp = pygame.image.load("court.png").convert()
 
# Using blit to copy content from one surface to other
screen.blit(imp, (240, 70))
 
# paint screen one time
pygame.display.flip()

run = True
selected = False

# "WIN" ,"FGM", "FGA", "3PM", "3PA", "AST", "ORB", "DRB","STL","BLK","TOV"]
def WIN():
    print('FGA')
def FGM():
    print('FGM')
    curr = "FGM"
    print(selected)
def FGA():
    print('FGA')
def TPM():
    print('FGA')
def TPA():
    print('FGM')
def AST():
    print('FGA')
def ORB():
    print('FGM')
def DRB():
    print('FGA')
def STL():
    print('FGM')
def BLK():
    print('FGA')
def TOV():
    print('FGM')

def Number(num):
    print(num)

stats = {}
players = [
    { "number": "45",
    "function": Number,
    "name": "Dorde"}
]
options = [
    { "name" : "FGM",
      "function": FGM
    },
    { "name" : "FGA",
      "function": FGA
    },
    { "name" : "3PM",
      "function": TPM
    },
    { "name" : "3PA",
      "function": TPA
    },
    { "name" : "AST",
      "function": AST
    },
    { "name" : "ORB",
      "function": ORB
    },
    { "name" : "DRB",
      "function": TPA
    },
    { "name" : "STL",
      "function": AST
    },
    { "name" : "BLK",
      "function": ORB
    },
    { "name" : "TOV",
      "function": TPA
    },
    { "name" : "WIN",
      "function": AST
    }
    ]

button_list = []
x = 80
x_increment = 125
y = 425
row = 0
y_increment = 75
count = 0
for option in options:
    curr_button = button(position = (x+(count*x_increment),y+(row*y_increment)), size=(100, 50), clr=(220, 220, 220), cngclr=(255, 0, 0), func=option["function"], text=option["name"])
    count+=1
    if x+(count*x_increment) > 725:
        count = 0
        row += 1
    button_list.append(curr_button)

player_list = []
x = 80
x_increment = 125
y = 425
row = 0
y_increment = 75
count = 0

for option in players:
    curr_button = button(position = (x+(count*x_increment),y+(row*y_increment)), size=(100, 50), clr=(220, 220, 220), cngclr=(255, 0, 0), func=option["function"], text=option["number"])
    count+=1
    if x+(count*x_increment) > 725:
        count = 0
        row += 1
    player_list.append(curr_button)

def save():
    print(stats)
    print("Save")

def new_game():
    stats = {}
    players = []


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_mods() & pygame.KMOD_META:
                if event.key == pygame.K_s:
                    save()  
                if event.key == pygame.K_n:
                    new_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if not selected and not press:
                        for b in button_list:
                            if b.rect.collidepoint(pos):
                                selected = True
                                press = True
                                pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 400, 800, 200))
                                pygame.display.flip()
                                b.call_back()
                    if selected and not press:
                         for b in player_list:
                            if b.rect.collidepoint(pos):
                                selected = False
                                press = True
                                pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 400, 800, 200))
                                pygame.display.flip()
                                b.call_back(b.txt)
        else:
            press = False
                
    if not selected:
        for b in button_list:
            b.draw(screen)
    if selected:
        for b in player_list:
            b.draw(screen)

    pygame.display.update()

pygame.quit()