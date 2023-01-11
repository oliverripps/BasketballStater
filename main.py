##TO DO FEATURE PLAN

# Calulcate Advanced Metrics
# WRONG BUTTON GO BACK(STore Last 5)
# Auto Save
# Live Feed
# Aggregate Stats Generator

import pygame
import pygame.locals 
from button import button, text
from datetime import date
import csv


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
global curr
def send_to_file(stats):    
    # need to add in advanced metrics
    today = date.today()
    file_name = "./" + str(today.month) + "-" + str(today.day) + "statsheet.csv"

    header = ["PLAYER","WINS","FGM","FGA","3PA","3PM","AST","ORB","DRB","REB","STL","BLK","TOV"]
    f = open(file_name, 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    for person in stats.keys():
        csv_string = [person]
        for i in stats[person]:
            csv_string.append(str(i))
        writer.writerow(csv_string)

# "WIN" ,"FGM", "FGA", "3PM", "3PA", "AST", "ORB", "DRB","STL","BLK","TOV"]
def WIN():
    global curr
    curr = "WIN"
def FGM():
    global curr
    curr = "FGM"
def FGA():
    global curr
    curr = "FGA"
def TPM():
    global curr
    curr = "3PM"
def TPA():
    global curr
    curr = "3PA"
def AST():
    global curr
    curr = "AST"
def ORB():
    global curr
    curr = "ORB"
def DRB():
    global curr
    curr = "DRB"
def STL():
    global curr
    curr = "STL"
def BLK():
    global curr
    curr = "BLK"
def TOV():
    global curr
    curr = "TOV"

def find(lst, num):
    for dictionary in lst:
        if dictionary["number"] == num:
            return dictionary
    return {}

def find_option(lst, name):
    for dictionary in lst:
        if dictionary["name"] == name:
            return dictionary
    return {}

stats = {}
global stat_records
stat_records = []
def Number(num):
    global stat_records
    new_stats = {}
    for i in stats.keys():
        new_stats[i] = stats[i].copy()
    stat_records.append(new_stats)
    print(stat_records)
    player_dict = find(players, num)
    name = player_dict["name"]
    stats_dict = find_option(options, curr)
    if name in stats:
        print(stats_dict["index"])
        stats[name][stats_dict["index"]] += 1
        if stats_dict["index"] == 1 or stats_dict["index"] == 3:
            stats[name][stats_dict["index"] + 1] += 1
        if stats_dict["index"] == 6 or stats_dict["index"] == 7:
            stats[name][8] += 1
    else:
        stats[name] = [0]*12
        stats[name][stats_dict["index"]] = 1
        if stats_dict["index"] == 1 or stats_dict["index"] == 3:
            stats[name][stats_dict["index"] + 1] = 1
        if stats_dict["index"] == 6 or stats_dict["index"] == 7:
            stats[name][8] = 1

    print(stats)
    save()


players = [
    { "number": "45",
    "function": Number,
    "name": "Cole Otley"},
    { "number": "44",
    "function": Number,
    "name": "Dorde Otastavic"},
    {"number": "35",
    "function": Number,
    "name": "Milun Micanovic"},
    { "number": "34",
    "function": Number,
    "name": "Jackson Reynolds"},
    { "number": "33",
    "function": Number,
    "name": "Anastasis Spyroglou"},
    { "number": "32",
    "function": Number,
    "name": "Shea Laursen"},
    { "number": "25",
    "function": Number,
    "name": "Chris Allen Jr."},
    { "number": "24",
    "function": Number,
    "name": "Aidan Miller"},
    { "number": "23",
    "function": Number,
    "name": "Dimitrije Radusinovic"},
    { "number": "21",
    "function": Number,
    "name": "Andrew Gannon"},
    { "number": "20",
    "function": Number,
    "name": "Adel Dibaei"},
    { "number": "14",
    "function": Number,
    "name": "Adam Navarre"},
    { "number": "13",
    "function": Number,
    "name": "Brian McGrath"},
    { "number": "12",
    "function": Number,
    "name": "Zach Smith"},
    { "number": "11",
    "function": Number,
    "name": "Yuuki Okubo"},
    { "number": "5",
    "function": Number,
    "name": "Asaan Snipes-Rea"},
     { "number": "3",
    "function": Number,
    "name": "Will Bousquette III"},
     { "number": "2",
    "function": Number,
    "name": "Henry Lieber"},
]
options = [
    { "name" : "WIN",
      "function": WIN,
      "index": 0
    },
    { "name" : "FGM",
      "function": FGM,
      "index": 1
    },
    { "name" : "FGA",
      "function": FGA,
      "index": 2
    },
    { "name" : "3PM",
      "function": TPM,
      "index": 3
    },
    { "name" : "3PA",
      "function": TPA,
      "index": 4
    },
    { "name" : "AST",
      "function": AST,
      "index": 5
    },
    { "name" : "ORB",
      "function": ORB,
      "index": 6
    },
    { "name" : "DRB",
      "function": DRB,
      "index": 7
    },
    #total rebounds is index 8
    { "name" : "STL",
      "function": STL,
      "index": 9
    },
    { "name" : "BLK",
      "function": BLK,
      "index": 10
    },
    { "name" : "TOV",
      "function": TOV,
      "index": 11
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
    if stats == {}:
        print("No Stats To Save")
    else:
        send_to_file(stats)

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
                if event.key == pygame.K_z:
                    print("Undo")
                    if len(stat_records) > 0:
                        stats = stat_records[len(stat_records)-1].copy()
                        stat_records = stat_records[0:-1]
                        print(stats)
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