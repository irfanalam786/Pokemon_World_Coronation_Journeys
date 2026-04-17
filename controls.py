import pygame
import sys

def controls_screen(screen, data, font):
    selected = 0
    controls = data["controls"]

    while True:
        screen.fill((0, 0, 50))

        title = font.render("Controls", True, (255, 255, 0))
        screen.blit(title, (320, 50))

        for i, text in enumerate(controls):
            color = (255, 255, 255)

            if i == selected:
                color = (0, 255, 0)  # highlight
                pygame.draw.rect(screen, (255, 255, 255), (80, 140 + i*50, 640, 40), 2)

            rendered = font.render(text, True, color)
            screen.blit(rendered, (100, 150 + i * 50))

        info = font.render("UP/DOWN to navigate | ESC to continue", True, (200, 200, 200))
        screen.blit(info, (120, 520))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(controls)

                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(controls)

                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()