import pygame
import sys

# Initialise all Pygame modules
pygame.init()

# Window Setup
WIDTH, HEIGHT = 1000,800 # 1000px wide + 800px tall
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Spaceship Shooter") # window title

# Control game's frame rate
clock = pygame.time.Clock()

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Button Colours
BUTTON_COLOUR = (30,35,60)
BUTTON_HOVER = (50,60,100)
BUTTON_BORDER = (100,120,180)

# Font
FONT = pygame.font.SysFont(None, 30)

# Game States
MENU = "menu"
INSTRUCTIONS = "instructions"
LEADERBOARD = "leaderboard"
SETTINGS = "settings"
MODE_SELECT = "mode_select"
PLAYER_SETUP = "player_setup"
GAME = "game"
GAME_OVER = "game_over"

# Current Game State
game_state = MENU

# Sound Effects Setting
sound_enabled = True

# Create a Reusable Button
def draw_button(text, x, y, WIDTH, HEIGHT):
    mouse_pos = pygame.mouse.get_pos()
    # Create button rectangle
    button_rect = pygame.Rect(x, y, WIDTH, HEIGHT)

    # Check if mouse's hovering over button
    if button_rect.collidepoint(mouse_pos):
        colour = BUTTON_HOVER
    else:
        colour = BUTTON_COLOUR

    # Draw button & button border
    pygame.draw.rect(SCREEN, colour, button_rect)
    pygame.draw.rect(SCREEN, BUTTON_BORDER, button_rect, 2)

    # Create button text & centre inside button
    text_surface = FONT.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)

    # Draw text onto screen
    SCREEN.blit(text_surface, text_rect)

    return button_rect

# Game Loop
running = True
while running:
    SCREEN.fill(BLACK)

    # Create menu
    if game_state == MENU:
        SCREEN.fill(BLACK)

        # Draw menu buttons
        select_mode_button = draw_button(
            "SELECT MODE",
            350,
            250,
            300,
            60
        )

        instructions_button = draw_button(
            "INSTRUCTIONS",
            350,
            330,
            300,
            60
        )

        leaderboard_button = draw_button(
            "LEADERBOARD",
            350,
            410,
            300,
            60
        )

        settings_button = draw_button(
            "SETTINGS",
            350,
            490,
            300,
            60
        )

        exit_button = draw_button(
            "EXIT",
            350,
            570,
            300,
            60
        )


    # Create instructions screen
    elif game_state == INSTRUCTIONS:
        SCREEN.fill(BLUE)
        # Draw back button
        back_button = draw_button(
            "BACK",
            50,
            700,
            150,
            50
        )

    # Create leaderboard screen
    elif game_state == LEADERBOARD:
        SCREEN.fill(GREEN)

        # Draw back button
        back_button = draw_button(
            "BACK",
            50,
            700,
            150,
            50
        )

    # Create settings screen
    elif game_state == SETTINGS:
        SCREEN.fill(YELLOW)

        # Draw sound toggle button
        sound_button = draw_button(
            "SOUND: ON" if sound_enabled else "SOUND: OFF",
            350,
            300,
            300,
            60
        )

        # Draw back button
        back_button = draw_button(
            "BACK",
            50,
            700,
            150,
            50
        )

    # Check what every event was
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check menu buttons
            if game_state == MENU:
                if select_mode_button.collidepoint(event.pos):
                    game_state = MODE_SELECT

                elif instructions_button.collidepoint(event.pos):
                    game_state = INSTRUCTIONS

                elif leaderboard_button.collidepoint(event.pos):
                    game_state = LEADERBOARD

                elif settings_button.collidepoint(event.pos):
                    game_state = SETTINGS

                elif exit_button.collidepoint(event.pos):
                    running = False

            elif game_state == INSTRUCTIONS:
                if back_button.collidepoint(event.pos):
                    game_state = MENU

            elif game_state == LEADERBOARD:
                if back_button.collidepoint(event.pos):
                    game_state = MENU

            elif game_state == SETTINGS:

                # Toggle sound effects
                if sound_button.collidepoint(event.pos):
                    # "not" creates unlimited toggling
                    sound_enabled = not sound_enabled

                # Return to main menu
                elif back_button.collidepoint(event.pos):
                    game_state = MENU

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()