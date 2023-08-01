import pygame, sys
from sudoku_generator import SudokuGenerator

class Main:

    def __init__(self):
        pass

    def draw_start_screen(screen):

        menu_mouse_pos = pygame.mouse.get_pos()

        # initialize fonts
        title_font = pygame.font.Font(None, 70)
        button_font = pygame.font.Font(None, 40)

        # BG color
        screen.fill((125, 199, 52))

        # title
        title_surface = title_font.render('Sudoku', 0, (0, 0, 0))
        title_rectangle = title_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 150))
        screen.blit(title_surface, title_rectangle)

        # subtitle
        subtitle_surface = button_font.render('Choose Your Puzzle:', 0, (0, 0, 0))
        subtitle_rectangle = subtitle_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        screen.blit(subtitle_surface, subtitle_rectangle)

        # button text
        easy_text = button_font.render("Easy", 0, (255, 255, 255))
        medium_text = button_font.render("Medium", 0, (255, 255, 255))
        hard_text = button_font.render("Hard", 0, (255, 255, 255))
        # quit_text = button_font.render("Quit", 0, (255, 255, 255))

        # button BG color and text
        easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
        easy_surface.fill((0, 0, 0))
        easy_surface.blit(easy_text, (10, 10))

        medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
        medium_surface.fill((0, 0, 0))
        medium_surface.blit(medium_text, (10, 10))

        hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
        hard_surface.fill((0, 0, 0))
        hard_surface.blit(hard_text, (10, 10))

        # quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
        # quit_surface.fill((0, 0, 0))
        # quit_surface.blit(quit_text, (10, 10))

        # button rectangle
        easy_rectangle = easy_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 25))
        medium_rectangle = medium_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
        hard_rectangle = hard_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 175))
        # quit_rectangle = quit_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 200))

        # draw buttons
        screen.blit(easy_surface, easy_rectangle)
        screen.blit(medium_surface, medium_rectangle)
        screen.blit(hard_surface, hard_rectangle)
        # screen.blit(quit_surface, quit_rectangle)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                # if quit_rectangle.collidepoint(event.pos):
                # pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_rectangle.collidepoint(event.pos):
                        return "easy"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if medium_rectangle.collidepoint(event.pos):
                        return "medium"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if hard_rectangle.collidepoint(event.pos):
                        return "hard"

            pygame.display.update()

    def draw_easy_screen(screen):
        screen.fill((255, 255, 255))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def draw_medium_screen(screen):
        screen.fill((255, 255, 255))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def draw_hard_screen(screen):
        screen.fill((255, 255, 255))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    pygame.init()

    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Sudoku")

    #Main.draw_start_screen(screen)

    selected_difficulty = Main.draw_start_screen(screen)

    if selected_difficulty == "easy":
        pygame.display.set_caption("Sudoku - Easy")
        Main.draw_easy_screen(screen)

    elif selected_difficulty == "medium":
        pygame.display.set_caption("Sudoku - Medium")
        Main.draw_medium_screen(screen)

    elif selected_difficulty == "hard":
        pygame.display.set_caption("Sudoku - Hard")
        Main.draw_hard_screen(screen)