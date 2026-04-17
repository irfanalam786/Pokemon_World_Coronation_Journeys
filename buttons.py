import pygame
import sys

def buttons_screen(screen, data, font):
    buttons = list(data["buttons"].items())
    selected = 0

    while True:
        screen.fill((50, 0, 0))

        title = font.render("Button Functions", True, (255, 255, 0))
        screen.blit(title, (250, 50))

        for i, (btn, action) in enumerate(buttons):
            color = (255, 255, 255)

            if i == selected:
                color = (0, 255, 0)
                pygame.draw.rect(screen, (255, 255, 255), (80, 140 + i*60, 640, 50), 2)

            text = f"{btn}: {action}"
            rendered = font.render(text, True, color)
            screen.blit(rendered, (100, 150 + i * 60))

        info = font.render("UP/DOWN | ENTER = select | ESC = continue", True, (200, 200, 200))
        screen.blit(info, (120, 520))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(buttons)

                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(buttons)

                if event.key == pygame.K_RETURN:
                    show_popup(screen, font, buttons[selected])

                # ✅ FIX: go to next screen (DON'T EXIT GAME)
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()


def show_popup(screen, font, button_data):
    btn, action = button_data

    while True:
        pygame.draw.rect(screen, (0, 0, 0), (150, 200, 500, 200))
        pygame.draw.rect(screen, (255, 255, 255), (150, 200, 500, 200), 2)

        text1 = font.render(btn, True, (255, 255, 0))
        text2 = font.render(action, True, (255, 255, 255))
        text3 = font.render("Press any key...", True, (180, 180, 180))

        screen.blit(text1, (350, 230))
        screen.blit(text2, (200, 280))
        screen.blit(text3, (280, 350))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()