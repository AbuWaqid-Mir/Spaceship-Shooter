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
TITLE_FONT = pygame.font.SysFont(None,60)
SCREEN_TITLE = pygame.font.SysFont(None, 50)
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

# -- Game Variables --
player_1_score = 0
player_2_score = 0
player_1_misses = 0
player_2_misses = 0
game_time = 60
start_time = 0

# -- Enemy Variables --
enemy_x = 400
enemy_y = 300
enemy_velocity_x = 3
enemy_velocity_y = 2
enemy_size = 50

# -- Available difficulty levels --
difficulty_levels = ["Easy", "Medium", "Hard"]

# -- Available Crosshair Colours --
crosshair_colours = [RED, BLUE, GREEN, YELLOW]

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

# -- Get next crosshair colour --
def next_crosshair_colour(current_colour):
    # Find current colour in list
    current_index = crosshair_colours.index(current_colour)
    # Move to next colour
    current_index += 1
    # Go back to 1st colour after the last one
    if current_index >= len(crosshair_colours):
        current_index = 0
    # Return the new colour
    return crosshair_colours[current_index]

# -- Get crosshair colour name --
def get_colour_name(colour):
    if colour == RED:
        return "RED"
    elif colour == BLUE:
        return "BLUE"
    elif colour == GREEN:
        return "GREEN"
    elif colour == YELLOW:
        return "YELLOW"

# -- Game Loop --
running = True
while running:
    SCREEN.fill(BLACK)

    # -- Create menu --
    if game_state == MENU:
        SCREEN.fill(BLACK)

        # -- Draw main menu --
        TITLE = TITLE_FONT.render(
            "SPACESHIP SHOOTER",
            True,
            WHITE
        )
        title_rect = TITLE.get_rect(
            center=(WIDTH // 2, 150)
        )
        SCREEN.blit(TITLE, title_rect)

        select_mode_button = draw_button(
            "SELECT MODE",
            350,
            250,
            300,
            60
        )

        instructions_button = draw_button(
            "HOW TO PLAY",
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

        # Draw title
        TITLE = SCREEN_TITLE.render(
            "HOW TO PLAY",
            True,
            WHITE
        )
        title_rect = TITLE.get_rect(
            center=(WIDTH // 2, 150)
        )
        SCREEN.blit(TITLE, title_rect)

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

        # Draw title
        TITLE = SCREEN_TITLE.render(
            "LEADERBOARD",
            True,
            WHITE
        )
        title_rect = TITLE.get_rect(
            center=(WIDTH // 2, 150)
        )
        SCREEN.blit(TITLE, title_rect)

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

        # Draw title
        TITLE = SCREEN_TITLE.render(
            "SETTINGS",
            True,
            WHITE
        )
        title_rect = TITLE.get_rect(
            center=(WIDTH // 2, 200)
        )
        SCREEN.blit(TITLE, title_rect)

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

        # Draw title
        TITLE = SCREEN_TITLE.render(
            "SELECT A MODE",
            True,
            WHITE
        )
        title_rect = TITLE.get_rect(
            center=(WIDTH // 2, 150)
        )
        SCREEN.blit(TITLE, title_rect)

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

        # -- Draw player setup buttons --

        # Player 1 name button
        if game_mode == "single":

            # Draw title
            TITLE = SCREEN_TITLE.render(
                "SINGLE PLAYER - SETUP",
                True,
                WHITE
            )
            title_rect = TITLE.get_rect(
                center=(WIDTH // 2, 100)
            )
            SCREEN.blit(TITLE, title_rect)

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
                "CROSSHAIR: " + get_colour_name(player_1_crosshair),
                350,
                380,
                300,
                60
            )

        elif game_mode == "two_player":

            # Draw title
            TITLE = SCREEN_TITLE.render(
                "2 PLAYERS - SETUP",
                True,
                WHITE
            )
            title_rect = TITLE.get_rect(
                center=(WIDTH // 2, 120)
            )
            SCREEN.blit(TITLE, title_rect)

            # -- Create Player 1 name input box --
            player_1_input = pygame.Rect(150, 200, 300, 60)

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
                "P1 CROSSHAIR: " + get_colour_name(player_1_crosshair),
                150,
                300,
                300,
                60
            )

            # -- Player 2 crosshair button --
            player_2_crosshair_button = draw_button(
                "P2 CROSSHAIR: " + get_colour_name(player_2_crosshair),
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

    # -- Game Screen --
    elif game_state == GAME:
        SCREEN.fill(BLACK)

        # -- Draw enemy --
        enemy_rect = pygame.Rect(
            enemy_x,
            enemy_y,
            enemy_size,
            enemy_size
        )

        pygame.draw.rect(
            SCREEN,
            RED,
            enemy_rect
        )

        # -- Move enemy --
        enemy_x += enemy_velocity_x
        enemy_y += enemy_velocity_y

        # -- Bounce off the screen's sides --
        if enemy_x <= 0 or enemy_x + enemy_size >= WIDTH:
            enemy_velocity_x *= -1
        if enemy_y <= 0 or enemy_y + enemy_size >= HEIGHT:
            enemy_velocity_y *= -1

        # -- Single-player game --
        if game_mode == "single":
            # Player 1 score
            score_text = FONT.render(
                player_1_name.upper() + " - SCORE: " + str(player_1_score),
                True,
                WHITE
            )
            SCREEN.blit(score_text, (30,30))

            # Calculate remaining game time
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
            # Calculate remaining game time
            game_time = 60 - elapsed_time
            # Prevent timer going below 0
            if game_time < 0:
                game_time = 0
            # Change timer colour depending on remaining time
            if game_time > 10:
                timer_colour = GREEN
            elif game_time > 5:
                timer_colour = YELLOW
            else:
                timer_colour = RED
            # End game when timer reaches 0
            if game_time == 0:
                game_state = GAME_OVER

            # Timer
            timer_text = FONT.render(
                str(game_time),
                True,
                timer_colour
            )
            timer_rect = timer_text.get_rect(
                center=(WIDTH // 2, 40)
            )
            SCREEN.blit(timer_text, timer_rect)

        # -- 2-player game --
        elif game_mode == "two_player":
            # Player 1 score
            player_1_score_text = FONT.render(
                player_1_name.upper() + " - SCORE: " + str(player_1_score),
                True,
                WHITE
            )
            SCREEN.blit(player_1_score_text, (30,30))

            # Player 2 score
            player_2_score_text = FONT.render(
                player_2_name.upper() + " - SCORE: " + str(player_2_score),
                True,
                WHITE
            )
            player_2_score_rect = player_2_score_text.get_rect(
                top=(30)
            )
            player_2_score_rect.right = WIDTH - 30
            SCREEN.blit(player_2_score_text, player_2_score_rect)

            # Calculate remaining game time
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
            # Calculate remaining game time
            game_time = 60 - elapsed_time
            # Prevent timer going below 0
            if game_time < 0:
                game_time = 0
            # Change timer colour depending on remaining time
            if game_time > 10:
                timer_colour = GREEN
            elif game_time > 5:
                timer_colour = YELLOW
            else:
                timer_colour = RED
            # End game when timer reaches 0
            if game_time == 0:
                game_state = GAME_OVER

            # Timer
            timer_text = FONT.render(
                str(game_time),
                True,
                timer_colour
            )
            timer_rect = timer_text.get_rect(
                center=(WIDTH // 2, 40)
            )
            SCREEN.blit(timer_text, timer_rect)

    # -- Game Over Screen --
    elif game_state == GAME_OVER:
        SCREEN.fill(BLACK)

        # Draw Game Over title
        game_over_text = FONT.render(
            "GAME OVER",
            True,
            RED
        )
        game_over_rect = game_over_text.get_rect(
            center=(WIDTH // 2, 100)
        )
        SCREEN.blit(game_over_text, game_over_rect)

        # Display difficulty
        difficulty_text = FONT.render(
            "DIFFICULTY: " + difficulty.upper(),
            True,
            WHITE
        )
        difficulty_rect = difficulty_text.get_rect(
            center=(WIDTH // 2, 180)
        )
        SCREEN.blit(difficulty_text, difficulty_rect)

        # Display Player 1 Score
        player_1_score_text = FONT.render(
            player_1_name + " - SCORE: " + str(player_1_score),
            True,
            WHITE
        )
        player_1_score_rect = player_1_score_text.get_rect(
            center=(WIDTH // 2, 250)
        )
        SCREEN.blit(player_1_score_text, player_1_score_rect)

        # Display Player 1 misses
        player_1_misses_text = FONT.render(
            "MISSES: " + str(player_1_misses),
            True,
            WHITE
        )
        player_1_misses_rect = player_1_misses_text.get_rect(
            center=(WIDTH // 2, 300)
        )
        SCREEN.blit(player_1_misses_text, player_1_misses_rect)

        # Display Player 2 information
        if game_mode == "two_player":
            player_2_score_text = FONT.render(
                player_2_name + " - SCORE: " + str(player_2_score),
                True,
                WHITE
            )
            player_2_score_rect = player_2_score_text.get_rect(
                center=(WIDTH // 2, 370)
            )
            SCREEN.blit(player_2_score_text, player_2_score_rect)
            player_2_misses_text = FONT.render(
                "MISSES: " + str(player_2_misses),
                True,
                WHITE
            )
            player_2_misses_rect = player_2_misses_text.get_rect(
                center=(WIDTH // 2, 420)
            )
            SCREEN.blit(player_2_misses_text, player_2_misses_rect)

        # Back to menu button
        back_to_menu_button = draw_button(
            "BACK TO MAIN MENU",
            350,
            600,
            300,
            60
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

                    # Reset player setup
                    player_1_name = ""
                    player_2_name = ""
                    current_input = None
                    difficulty = "Easy"

                    game_state = PLAYER_SETUP

                # Select 2-player mode
                elif two_player_button.collidepoint(event.pos):
                    game_mode = "two_player"

                    # Reset player setup
                    player_1_name = ""
                    player_2_name = ""
                    current_input = None
                    difficulty = "Easy"

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
                elif game_mode == "two_player" and player_2_input.collidepoint(event.pos):
                    current_input = "player_2"

                # -- Change difficulty --
                elif difficulty_button.collidepoint(event.pos):
                    # Find current difficulty
                    current_index = difficulty_levels.index(difficulty)
                    # Move to next difficulty
                    current_index += 1
                    # Loop back to easy after hard
                    if current_index >= len(difficulty_levels):
                        current_index = 0
                    # Update difficulty
                    difficulty = difficulty_levels[current_index]

                elif game_mode == "single" and crosshair_button.collidepoint(event.pos):
                    player_1_crosshair = next_crosshair_colour(player_1_crosshair)

                # Change Player 1's crosshair colour
                elif game_mode == "two_player" and player_1_crosshair_button.collidepoint(event.pos):
                    new_colour = next_crosshair_colour(player_1_crosshair)
                    # Only change colour if Player 2 isn't already using it
                    if new_colour != player_2_crosshair:
                        player_1_crosshair = new_colour

                # Change Player 2's crosshair colour
                elif game_mode == "two_player" and player_2_crosshair_button.collidepoint(event.pos):
                    new_colour = next_crosshair_colour(player_2_crosshair)
                    # Only change colour if Player 1 isn't already using it
                    if new_colour != player_1_crosshair:
                        player_2_crosshair = new_colour

                # Start the game
                elif start_game_button.collidepoint(event.pos):
                    # Deactivate name input
                    current_input = None
                    # Reset scores
                    player_1_score = 0
                    player_2_score = 0
                    # Reset misses
                    player_1_misses = 0
                    player_2_misses = 0
                    # Reset timer
                    game_time = 60
                    # Record when game started
                    start_time = pygame.time.get_ticks()
                    # Change to Game Screen
                    game_state = GAME

                # Return to mode selection
                elif back_button.collidepoint(event.pos):
                    current_input = None
                    game_state = MODE_SELECT

            # -- Game Over Screen Buttons --
            elif game_state == GAME_OVER:
                if back_to_menu_button.collidepoint(event.pos):
                    game_state = MENU


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