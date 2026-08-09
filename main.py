import pygame
import sys

# -- Initialise all Pygame modules --
pygame.init()

# -- Window Setup --
WIDTH, HEIGHT = 1000,800 # 1000px wide + 800px tall
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Spaceship Shooter") # window title

# -- Control game's frame rate --
clock = pygame.time.Clock()

# -- Colours --
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# -- Button Colours --
BUTTON_COLOUR = (30,35,60)
BUTTON_HOVER = (50,60,100)
BUTTON_BORDER = (100,120,180)

# -- Font --
FONT = pygame.font.SysFont(None, 30)

# -- Game States --
MENU = "menu"
INSTRUCTIONS = "instructions"
LEADERBOARD = "leaderboard"
SETTINGS = "settings"
MODE_SELECT = "mode_select"
PLAYER_SETUP = "player_setup"
GAME = "game"
GAME_OVER = "game_over"

# -- Current Game State --
game_state = MENU
game_mode = None
sound_enabled = True

# -- Player Setup --
player_1_name = ""
player_2_name = ""
difficulty = "Easy"
player_1_crosshair = RED
player_2_crosshair = BLUE
current_input = None

# -- Create a Reusable Button --
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

# -- Game Loop --
running = True
while running:
    SCREEN.fill(BLACK)

    # -- Create menu --
    if game_state == MENU:
        SCREEN.fill(BLACK)

        # -- Draw main menu buttons --
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


    # -- Create instructions screen --
    elif game_state == INSTRUCTIONS:
        SCREEN.fill(BLACK)
        # Draw back button
        back_button = draw_button(
            "BACK",
            50,
            700,
            150,
            50
        )

    # -- Create leaderboard screen --
    elif game_state == LEADERBOARD:
        SCREEN.fill(BLACK)

        # Draw back button
        back_button = draw_button(
            "BACK",
            50,
            700,
            150,
            50
        )

    # -- Create settings screen --
    elif game_state == SETTINGS:
        SCREEN.fill(BLACK)

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

    # -- Mode Selection Screen --
    elif game_state == MODE_SELECT:
        SCREEN.fill(BLACK)

        # -- Draw mode selection buttons --
        single_player_button = draw_button(
            "SINGLE PLAYER",
            350,
            300,
            300,
            60
        )

        two_player_button = draw_button(
            "2 PLAYERS",
            350,
            380,
            300,
            60
        )

        back_button = draw_button(
            "BACK",
            50,
            700,
            150,
            50
        )

    # -- Player Setup Screen --
    elif game_state == PLAYER_SETUP:
        SCREEN.fill((20,20,40))

        # -- Draw screen title --
        title_text = FONT.render("PLAYER SETUP", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 80))
        SCREEN.blit(title_text, title_rect)

        # -- Draw player setup buttons --

        # Player 1 name button
        if game_mode == "single":
            # Create Player 1 name input box
            player_1_input = pygame.Rect(350, 180, 300, 60)

            # Change border when input is active
            if current_input == "player_1":
                border_colour = WHITE
            else:
                border_colour = BUTTON_BORDER

            # Draw input box
            pygame.draw.rect(SCREEN, BUTTON_COLOUR, player_1_input)
            # Draw input box border
            pygame.draw.rect(SCREEN, border_colour, player_1_input, 2)

            # Display Player 1's name
            name_text = FONT.render(player_1_name, True, WHITE)
            name_rect = name_text.get_rect(center=player_1_input.center)
            SCREEN.blit(name_text, name_rect)

            # Difficulty button
            difficulty_button = draw_button(
                "DIFFICULTY: " + difficulty.upper(),
                350,
                280,
                300,
                60
            )

            # Crosshair button
            crosshair_button = draw_button(
                "CROSSHAIR",
                350,
                380,
                300,
                60
            )

        elif game_mode == "two_player":
            # -- Create Player 1 name input box --
            player_1_input = pygame.Rect(350, 180, 300, 60)

            # Change border when input is active
            if current_input == "player_1":
                border_colour = WHITE
            else:
                border_colour = BUTTON_BORDER

            # Draw input box
            pygame.draw.rect(SCREEN, BUTTON_COLOUR, player_1_input)
            # Draw input box border
            pygame.draw.rect(SCREEN, border_colour, player_1_input, 2)

            # Display Player 1's name
            name_text = FONT.render(player_1_name, True, WHITE)
            name_rect = name_text.get_rect(center=player_1_input.center)
            SCREEN.blit(name_text, name_rect)

            # -- Create Player 2 name input box --
            player_2_input = pygame.Rect(550, 200, 300, 60)

            # Change border when input is active
            if current_input == "player_2":
                border_colour = WHITE
            else:
                border_colour = BUTTON_BORDER

            # Draw input box
            pygame.draw.rect(SCREEN, BUTTON_COLOUR, player_2_input)

            # Draw input box border
            pygame.draw.rect(SCREEN, border_colour, player_2_input, 2)

            # Display Player 2's name
            name_text = FONT.render(player_2_name, True, WHITE)
            name_rect = name_text.get_rect(center=player_2_input.center)
            SCREEN.blit(name_text, name_rect)

            # -- Player 1 crosshair button --
            player_1_crosshair_button = draw_button(
                "P1 CROSSHAIR",
                150,
                300,
                300,
                60
            )

            # -- Player 2 crosshair button --
            player_2_crosshair_button = draw_button(
                "P2 CROSSHAIR",
                550,
                300,
                300,
                60
            )

            # Difficulty button
            difficulty_button = draw_button(
                "DIFFICULTY: " + difficulty.upper(),
                350,
                400,
                300,
                60
            )

        # Start game button
        start_game_button = draw_button(
            "START GAME",
            350,
            500,
            300,
            60
        )

        # Back button
        back_button = draw_button(
            "BACK",
            50,
            700,
            150,
            50
        )

    # -- Check what every event was --
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: # mouse clicks
            # -- Main Menu buttons --
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

            # -- Instructions buttons --
            elif game_state == INSTRUCTIONS:
                if back_button.collidepoint(event.pos):
                    game_state = MENU

            # -- Leaderboard buttons --
            elif game_state == LEADERBOARD:
                if back_button.collidepoint(event.pos):
                    game_state = MENU

            # -- Settings buttons --
            elif game_state == SETTINGS:
                # Toggle sound effects
                if sound_button.collidepoint(event.pos):
                    # "not" creates unlimited toggling
                    sound_enabled = not sound_enabled
                # Return to main menu
                elif back_button.collidepoint(event.pos):
                    game_state = MENU

            # -- Mode selection buttons --
            elif game_state == MODE_SELECT:
                # Select single player mode
                if single_player_button.collidepoint(event.pos):
                    game_mode = "single"
                    game_state = PLAYER_SETUP
                # Select 2-player mode
                elif two_player_button.collidepoint(event.pos):
                    game_mode = "two_player"
                    game_state = PLAYER_SETUP
                elif back_button.collidepoint(event.pos):
                    game_state = MENU

            # -- Player Setup buttons --
            elif game_state == PLAYER_SETUP:
                # Activate Player 1 name input
                if player_1_input.collidepoint(event.pos):
                    current_input = "player_1"
                # Activate Player 2 name input
                # to ensure we're only using Player 2 box when in 2-player mode
                elif game_mode == "two-player" and player_2_input.collidepoint(event.pos):
                    current_input = "player_2"
                # Return to mode selection
                elif back_button.collidepoint(event.pos):
                    game_state = MODE_SELECT

        # -- Keyboard Input --
        if event.type == pygame.KEYDOWN:
            # -- Player 1's typing --
            if current_input == "player_1":
                # Remove the last character
                if event.key == pygame.K_BACKSPACE:
                    player_1_name = player_1_name[:-1]
                # Add typed character
                else:
                    player_1_name += event.unicode
            # -- Player 2's typing
            elif current_input == "player_2":
                if event.key == pygame.K_BACKSPACE:
                    player_2_name = player_2_name[:-1]
                else:
                    player_2_name += event.unicode

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()