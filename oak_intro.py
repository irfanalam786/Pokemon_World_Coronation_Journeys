#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys, os, string

DEFAULT_NAME = "ORANGE"
DEFAULT_RIVAL = "GARY"

# ---------- LOAD IMAGE ----------
def load_image(path, scale=None):
    if not os.path.exists(path):
        print(f"Missing image: {path}")
        pygame.quit(); sys.exit()
    img = pygame.image.load(path).convert_alpha()
    if scale:
        img = pygame.transform.smoothscale(img, scale)
    return img


# ---------- BACKGROUND ----------
def draw_background(screen, color=(10,30,80)):
    screen.fill(color)


# ---------- TEXTBOX (WHITE + BLACK TEXT) ----------
def textbox(screen, font, text):
    pygame.draw.rect(screen,(255,255,255),(40,380,720,170),border_radius=12)
    pygame.draw.rect(screen,(0,0,0),(40,380,720,170),3,border_radius=12)

    words = text.split(" ")
    lines = []
    current = ""

    for word in words:
        test = current + word + " "
        if font.size(test)[0] < 650:
            current = test
        else:
            lines.append(current)
            current = word + " "
    lines.append(current)

    y = 400
    for line in lines:
        txt = font.render(line.strip(), True, (0,0,0))
        screen.blit(txt, (60, y))
        y += 35


# ---------- FADE ----------
def fade_out(screen, img):
    alpha = 255
    clock = pygame.time.Clock()
    while alpha > 0:
        screen.fill((10,30,80))
        img.set_alpha(alpha)
        screen.blit(img,(310,100))
        pygame.display.update()
        alpha -= 8
        clock.tick(30)


# ---------- SIMPLE NAME INPUT ----------
def simple_name_input(screen,font,default):
    name=""
    clock=pygame.time.Clock()

    while True:
        screen.fill((20,120,130))
        textbox(screen,font,"Enter name (ENTER = OK)")

        display = name if name else default
        screen.blit(font.render(display,True,(0,0,0)),(300,250))

        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit(); sys.exit()

            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_RETURN:
                    return name if name else default
                if e.key==pygame.K_BACKSPACE:
                    name=name[:-1]
                else:
                    if len(name)<8 and e.unicode.isalpha():
                        name+=e.unicode.upper()

        pygame.display.update()
        clock.tick(30)


# ---------- CONFIRM PLAYER ----------
def confirm(screen,font,name,ash):
    selected=0
    alpha=0
    fade_in=True
    clock=pygame.time.Clock()

    while True:
        screen.fill((10,30,80))

        if fade_in:
            alpha+=5
            if alpha>=255:
                alpha=255; fade_in=False

        ash.set_alpha(alpha)
        screen.blit(ash,(310,100))

        textbox(screen,font,f"Right... So your name is {name}.")

        options=["YES","NO"]
        for i,opt in enumerate(options):
            y=420+i*40
            if i==selected:
                pygame.draw.rect(screen,(255,0,0),(500,y-5,80,35),2)
            screen.blit(font.render(opt,True,(0,0,0)),(510,y))

        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit(); sys.exit()

            if e.type==pygame.KEYDOWN:
                if e.key in [pygame.K_UP,pygame.K_DOWN]:
                    selected=1-selected
                if e.key==pygame.K_RETURN:
                    if selected==0:
                        fade_out(screen,ash)
                        return name
                    else:
                        return None

        pygame.display.update()
        clock.tick(30)


# ---------- RIVAL INTRO ----------
def rival_intro(screen,font):
    gary=load_image("image/gary.png",(180,220))

    options=["NEW NAME","GARY","SHIGERU","BLUE","GREEN"]
    selected=1
    clock=pygame.time.Clock()

    while True:
        draw_background(screen,(120,180,120))
        screen.blit(gary,(500,120))

        textbox(screen,font,"...Erm, what was his name now?")

        for i,opt in enumerate(options):
            y=150+i*40
            if i==selected:
                pygame.draw.rect(screen,(255,0,0),(60,y-5,200,35),2)
            screen.blit(font.render(opt,True,(0,0,0)),(70,y))

        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit(); sys.exit()

            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_DOWN: selected=(selected+1)%len(options)
                if e.key==pygame.K_UP: selected=(selected-1)%len(options)

                if e.key==pygame.K_RETURN:
                    if selected==0:
                        name=simple_name_input(screen,font,DEFAULT_RIVAL)
                    else:
                        name=options[selected]

                    return rival_confirm(screen,font,name,gary)

        pygame.display.update()
        clock.tick(30)


# ---------- RIVAL CONFIRM ----------
def rival_confirm(screen,font,name,gary):
    selected=0
    clock=pygame.time.Clock()

    while True:
        draw_background(screen,(120,180,120))
        screen.blit(gary,(500,120))

        textbox(screen,font,f"...era, was it {name}?")

        options=["YES","NO"]
        for i,opt in enumerate(options):
            y=420+i*40
            if i==selected:
                pygame.draw.rect(screen,(255,0,0),(500,y-5,80,35),2)
            screen.blit(font.render(opt,True,(0,0,0)),(510,y))

        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit(); sys.exit()

            if e.type==pygame.KEYDOWN:
                if e.key in [pygame.K_UP,pygame.K_DOWN]:
                    selected=1-selected
                if e.key==pygame.K_RETURN:
                    if selected==0:
                        return name
                    else:
                        return None

        pygame.display.update()
        clock.tick(30)


# ---------- FINAL ASH ----------
def final_ash(screen,font,player_name):
    ash=load_image("image/ash.png",(180,220))
    clock=pygame.time.Clock()
    timer=0

    while True:
        draw_background(screen)
        screen.blit(ash,(310,120))

        if timer<120:
            textbox(screen,font,f"{player_name}, your Pokémon legend is about to unfold!")
        else:
            textbox(screen,font,"A world of dreams and adventures awaits! Let's go!")

        timer+=1
        if timer>240:
            return

        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit(); sys.exit()

        pygame.display.update()
        clock.tick(30)


# ---------- MAIN ----------
def oak_intro_screen(screen,font):
    oak=load_image("image/oak.png",(180,220))
    ash=load_image("image/ash.png",(180,220))

    script=["Hello there!","Welcome to the world of Pokémon"]
    clock=pygame.time.Clock()

    for line in script:
        t=0
        while t<120:
            draw_background(screen)
            screen.blit(oak,(310,120))
            textbox(screen,font,line)
            pygame.display.update()
            t+=1
            clock.tick(30)

    # player name
    name=None
    while name is None:
        name=confirm(screen,font,
                     simple_name_input(screen,font,DEFAULT_NAME),
                     ash)

    # rival
    rival=None
    while rival is None:
        rival=rival_intro(screen,font)

    # final
    final_ash(screen,font,name)

    return name, rival