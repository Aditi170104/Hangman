import pygame
from pygame.locals import *
from pygame import mixer
import math
import random
import sys

# setup display
pygame.init()
WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANGMAN GAME")
#logo
Icon = pygame.image.load('logo.png')
pygame.display.set_icon(Icon)

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    #setting the starting gaps and the ending gaps
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.Font('2.ttf', 40)
WORD_FONT = pygame.font.SysFont('calibri', 60)
TITLE_FONT = pygame.font.Font('HANGU.ttf', 80)
HINT_FONT=pygame.font.Font('HINTU.ttf',30)
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('quit', True,'red')

# load images.
images = []
for i in range(8):
    image = pygame.image.load("Hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = ["AIR","BELL","STAR","PIE","HAT",'HEART','FLAG','CARPET','POPCORN','COWBOY','FOOTBALL','STRAWBERRY','BACKGROUND','BOOKWORM','FIREFIGHTER','SOUNDPROOF','THUNDERSTORM','LOUDSPEAKER','SUPERHUMAN','FINGERPRINT','CORONA']
word = random.choice(words)
guessed = []
#loss

# colors
CYAN = (177,162,202)
BLACK = (0, 0, 0)
purple=(48, 25, 52)
color = (255, 255, 255)
color_light = (170, 170, 170)
#Background music
mixer.init()
mixer.music.load('back.mp3')
mixer.music.play()
FPS = 100
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(CYAN)

    # draw title
    text = TITLE_FONT.render("Hangman Game", 1, BLACK)
    win.blit(text, (352, 40))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

   # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text,
                     (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (110,80))  # drawing images
    pygame.display.update()
#lossbackground
def loss():
    image1=pygame.image.load("game.jpg")
    win.blit(image1,(0,0))
    pygame.display.update()
#winbackground
def winn():
    image2=pygame.image.load("WIIN.png")
    win.blit(image2,(0,0))
    pygame.display.update()
#hints
def gint():
    if word=="AIR":
         text=HINT_FONT.render("HINT- the thing we breathe",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="BELL":
         text=HINT_FONT.render("HINT- DING DONG",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="STAR":
         text=HINT_FONT.render("HINT- TWINKLE TWINKLE",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="PIE":
         text=HINT_FONT.render("HINT- A SWEET MEAL",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="HAT":
         text=HINT_FONT.render("HINT- COVERS THE HAIR",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="HEART":
         text=HINT_FONT.render("HINT- THAT BEATS",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="FLAG":
         text=HINT_FONT.render("HINT- REPRESENTS A NATION",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="CARPET":
         text=HINT_FONT.render("HINT- COVERS THE FLOOR",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="POPCORN":
         text=HINT_FONT.render("HINT- MOVIE TIME ",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="COWBOY":
         text=HINT_FONT.render("HINT- DO YOU REMEMBER WOODY ?",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="FOOTBALL":
         text=HINT_FONT.render("HINT- MESSI FANS ?",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="STRAWBERRY":
         text=HINT_FONT.render("HINT- WANNA DRINK PINK SHAKE ?",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="BACKGROUND":
         text=HINT_FONT.render("HINT-  OPPOSITE OF FOREGROUND",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="BOOKWORM":
         text=HINT_FONT.render("HINT- ANOTHER WAY TO CALL A TOPPER",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="FIREFIGHTER":
         text=HINT_FONT.render("HINT- A REAL HERO ",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="SOUNDPROOF":
         text=HINT_FONT.render("HINT- YOU CANT HEAR ME!",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="THUNDERSTORM":
         text=HINT_FONT.render("HINT- YOUR EVERYTIME FAVOURITE HORROR SOUND",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="LOUDSPEAKER":
         text=HINT_FONT.render("HINT- IRRITATION FOR SOME AND FUN FOR SOME",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="SUPERHUMAN":
         text=HINT_FONT.render("HE CAN LIFT A CAR ",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="FINGERPRINT":
         text=HINT_FONT.render("UNIQUE FOR EVERY HUMAN",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()
    elif word=="CORONA":
         text=HINT_FONT.render("CAUSED A PANDEMIC  ",1,BLACK)
         win.blit(text,(WIDTH / 2 - text.get_width() / 2, 600))
         pygame.display.update()  
#mainrunning


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #quiting the game
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            mixer.music.load('mouse click.wav')
            mixer.music.play() 
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 +
                                    (y - m_y)**2)  #applying pythagorous theorm
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

            draw()
            gint()

            won = True
            for letter in word:
                if letter not in guessed:
                    won = False
                    break

            if won:
                pygame.mixer.pause()
                mixer.music.load('win.wav')
                mixer.music.play()
                pygame.mixer.music.play(-1,0.0)
                winn()
                break

            if hangman_status==6:
                pygame.mixer.pause()
                mixer.music.load('loss.wav')
                mixer.music.play()
                pygame.mixer.music.play(-1,0.0)
                loss()
                break
pygame.quit()