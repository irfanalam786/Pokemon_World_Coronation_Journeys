#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import json
import sys
import os

from controls import controls_screen
from buttons import buttons_screen
from start_select_lr import start_select_lr_screen
from intro_story import intro_story_screen
from oak_intro import oak_intro_screen

pygame.init()

# ---------- SCREEN ----------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokémon Masters Journey")

# ---------- FONT ----------
font = pygame.font.Font(None, 32)

# ---------- LOAD JSON ----------
def load_data():
    try:
        with open("game_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"title": "Pokémon Masters Journey"}

# ---------- LOAD IMAGE ----------
def load_image(path):
    if not os.path.exists(path):
        print(f"Missing image: {path}")
        pygame.quit()
        sys.exit()
    return pygame.image.load(path)

# ---------- DRAW TEXT ----------
def draw_text(text, x, y):
    txt = font.render(text, True, (255, 255, 255))
    screen.blit(txt, (x, y))

# ---------- TITLE SCREEN ----------
def title_screen(data):
    bg = load_image("image/front.png")
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    while True:
        screen.blit(bg, (0, 0))

        draw_text(data.get("title", "Pokémon Game"), 200, 50)
        draw_text("Press ENTER to Start", 250, 520)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        pygame.display.update()

# ---------- MAIN ----------
def main():
    data = load_data()

    # 🎬 FLOW
    title_screen(data)
    controls_screen(screen, data, font)
    buttons_screen(screen, data, font)
    start_select_lr_screen(screen, data, font)
    intro_story_screen(screen, font)

    # 🔥 MAIN INTRO SYSTEM
    player_name, rival_name = oak_intro_screen(screen, font)

    print("Player:", player_name)
    print("Rival:", rival_name)

    # ---------- END SCREEN ----------
    while True:
        screen.fill((0, 0, 0))
        draw_text(f"Welcome {player_name}!", 250, 250)
        draw_text(f"Your rival is {rival_name}", 220, 300)
        draw_text("Next: Pokémon Selection...", 200, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# ---------- RUN ----------
if __name__ == "__main__":
    main()