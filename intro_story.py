#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys

# ---------- TEXTBOX ----------
def textbox(screen, font, text):
    # white box
    pygame.draw.rect(screen, (255, 255, 255), (40, 380, 720, 170), border_radius=12)
    # black border
    pygame.draw.rect(screen, (0, 0, 0), (40, 380, 720, 170), 3, border_radius=12)

    # text wrap
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

    # draw text
    y = 400
    for line in lines:
        txt = font.render(line.strip(), True, (0, 0, 0))  # black text
        screen.blit(txt, (60, y))
        y += 35


# ---------- BACKGROUND ----------
def draw_background(screen):
    screen.fill((10, 30, 80))  # dark blue


# ---------- MAIN STORY ----------
def intro_story_screen(screen, font):
    story_lines = [
        "You are a boy from PALLET TOWN!",
        "Now that you are 10 you can get your POKÉMON licence.",

        "Ten year olds can get a beginner POKÉMON",
        "from PROFESSOR OAK,",
        "the town's POKÉMON expert.",

        "This is just the beginning of your amazing adventures!",

        "Your journey is destined to be packed with nonstop action,",
        "millions of laughs, heartpounding perils,",
        "and endless excitement!",

        "You’ll encounter fantastic friends, evil enemies,",
        "and meet creatures beyond your wildest imagination!",

        "And as your story unfolds you’ll unlock the magic",
        "and mystery of the world POKÉMON!"
    ]

    page = 0
    lines_per_page = 2
    char_index = 0
    speed = 2

    clock = pygame.time.Clock()

    wait_timer = 0
    wait_limit = 90  # auto speed

    while True:
        draw_background(screen)

        start = page * lines_per_page
        lines = story_lines[start:start + lines_per_page]

        display_text = ""

        for i, line in enumerate(lines):
            if i == len(lines) - 1:
                if char_index < len(line):
                    char_index += speed
                    display_text += line[:char_index]
                else:
                    display_text += line
            else:
                display_text += line + " "

        textbox(screen, font, display_text)

        # auto next
        if char_index >= len(lines[-1]):
            wait_timer += 1
            if wait_timer >= wait_limit:
                page += 1
                char_index = 0
                wait_timer = 0

                if page > len(story_lines) // lines_per_page:
                    return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(30)