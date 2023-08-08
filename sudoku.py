import pygame,sys
from sudoku_generator import*

bg_color = (255,255,255) # white

def row_check(board,num, row):

    count = 0
    for i in range(0,9):
        if board[row][i] == num:
            count+= 1
    if count >= 2:
        return False
    return True

def col_check(board,num,col):
    count = 0
    for i in range(0,9):
        if board[i][col] == num:
            count += 1
    if count >= 2:
        return False
    return True

def check_box(board,num,row,col):
    # Looks for row,col of top left corner
    # of each 3 x 3 box
    count = 0
    local_box_row = row - row % 3
    local_box_col = col - col % 3
    # loops through 3 x 3 grid
    for i in range(local_box_row,local_box_row + 3):
        for j in range(local_box_col,local_box_col + 3):
            if board[i][j] == num:
                count += 1
    if count >= 2:
        return False
    return True

def check_if_full(board):
    # Checks if the board is full
    for i in range(0,9):
        for j in range(0,9):
            if not str(board[i][j]).isdigit():
                return False
    return True

def check_if_winner(board):
    # Checks each row of completed board to see whether it is win or lose
    for i in range(0, 9):
        for j in range(1, 10):
            if row_check(board, j, i) == False:
                return False
    # Checks each column of completed board to see whether it is win or lose
    for i in range(0, 9):
        for j in range(1, 10):
            if col_check(board, j, i) == False:
                return False
    # Checks each box of completed board to see whether it is win or lose
    for i in range(0, 9):
        if check_box(board, i, 1, 1) == False:
            return False
        if check_box(board, i, 4, 1) == False:
            return False
        if check_box(board, i, 7, 1) == False:
            return False
        if check_box(board, i, 1, 4) == False:
            return False
        if check_box(board, i, 4, 4) == False:
            return False
        if check_box(board, i, 7, 4) == False:
            return False
        if check_box(board, i, 1, 7) == False:
            return False
        if check_box(board, i, 4, 7) == False:
            return False
        if check_box(board, i, 7, 7) == False:
            return False
    return True

def set_board(screen,board,font):
 # placing digits on the Sudoku board
    for x in range(0, len(board[0])):
        for y in range(0, len(board[0])):
            # digit is between 1 and 9
            if (board[x][y] > 0 and board[x][y] < 10):
                # text rendering
                value = font.render(str(board[x][y]), True, (100, 100, 200))
                # print the digit on Sudoku Board
                screen.blit(value, ((y + 1) * 50 + 15, (x + 1) * 50 + 5))

def set_button(screen,screen_width,screen_height):
    rect_list = []
    button_font = pygame.font.SysFont('Helvetica', 15, bold=True)
    # In Game Button Text
    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    # In Game Button Background Color and Text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill((0, 0, 0))
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill((0, 0, 0))
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((0, 0, 0))
    exit_surface.blit(exit_text, (10, 10))

    # In Game Button Rectangles
    reset_rectangle = reset_surface.get_rect(center=(screen_width // 2 - 198, screen_height - 20))
    restart_rectangle = restart_surface.get_rect(center=(screen_width // 2, screen_height - 20))
    exit_rectangle = exit_surface.get_rect(center=(screen_width // 2 + 198, screen_height - 20))
    rect_list.extend([reset_rectangle,restart_rectangle,exit_rectangle])

    # Draws In Game Buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    return rect_list

def place(window, pos,board,original,screen,screen_width,screen_height):
    # Places numbers on the board
    font = pygame.font.SysFont('Helvetica', 30)
    x, y = pos[1], pos[0]

    while True:

        for event in pygame.event.get():
            # if user has pressed quit button, quit the window
            if (event.type == pygame.QUIT):
                pygame.quit()
                return

            # if user wants to enter a value
            if event.type == pygame.KEYDOWN:
                # Modifying original value
                if original[x - 1][y - 1] != 0:  # since the blank values are zeros
                    return

                # edit previously entered digit
                # 0 is mapped to 48 ASCII
                if (event.key == 48):
                    # erasing previosly entered value in backend
                    board[x - 1][y - 1] = event.key - 48
                    # erasing previosly entered value on the screen
                    pygame.draw.rect(window, bg_color, (y * 50 + 5, x * 50 + 5, 50 - 10, 50 - 10))

                    # again displaying updated window
                    pygame.display.update()
                    return

                # enter a value in a blank cell
                if (0 < event.key - 48 < 10):
                    # erasing previosly entered value on the screen
                    pygame.draw.rect(window, bg_color, (y * 50 + 5, x * 50 + 5, 50 - 10, 50 - 10))

                    val = font.render(str(event.key - 48), True, (0,0,0))
                    window.blit(val, (y * 50 + 15, x * 50 + 5))

                    board[x - 1][y - 1] = event.key - 48

                    # updated window
                    pygame.display.update()
                    pygame.event.pump()
                    return

def draw_start_screen(screen,screen_width,screen_height):
        # initialize fonts
        #title_font = pygame.font.Font(None, 70)
        title_font = pygame.font.SysFont('Helvetica', 50,italic=True)
        button_font = pygame.font.SysFont('Helvetica',30,)
        #button_font = pygame.font.Font(None, 40)

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

        # button rectangle
        easy_rectangle = easy_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 25))
        medium_rectangle = medium_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
        hard_rectangle = hard_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 175))

        # draw buttons
        screen.blit(easy_surface, easy_rectangle)
        screen.blit(medium_surface, medium_rectangle)
        screen.blit(hard_surface, hard_rectangle)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_rectangle.collidepoint(event.pos):
                        return "easy"
                    elif medium_rectangle.collidepoint(event.pos):
                        return "medium"
                    elif hard_rectangle.collidepoint(event.pos):
                        return "hard"

            pygame.display.update()

def draw_grid(screen):
    # Draws the Grid to the screen
    for i in range(0, 10):
        if i % 3 == 0:
            # every third line is bold to
            pygame.draw.line(screen, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(screen, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        else:
            # draw.line(window, color, start coodinate, end coodinate, width)
            # vertical lines
            pygame.draw.line(screen, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            # horizontal lines
            pygame.draw.line(screen, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

def draw_lose_screen(screen,screen_width,screen_height):

        screen.fill((125, 199, 52))

        # game over text
        lose_font = pygame.font.Font(None, 70)
        lose_surface = lose_font.render('Game Over', 0, (0, 0, 0))
        lose_rectangle = lose_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 150))
        screen.blit(lose_surface, lose_rectangle)

        # restart button
        button_font = pygame.font.Font(None, 40)
        restart_text = button_font.render("Exit", 0, (255, 255, 255))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill((0, 0, 0))
        restart_surface.blit(restart_text, (10, 10))
        restart_rectangle = restart_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 25))
        screen.blit(restart_surface, restart_rectangle)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rectangle.collidepoint(event.pos):
                      draw_start_screen(screen,screen_width,screen_height)

            pygame.event.pump()

def draw_win_screen(screen,screen_width,screen_height):
        screen.fill((125, 199, 52))

        #game won text
        win_font = pygame.font.Font(None, 70)
        win_surface = win_font.render('You Win!', 0, (0, 0, 0))
        win_rectangle = win_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 150))
        screen.blit(win_surface, win_rectangle)

        #exit button
        button_font = pygame.font.Font(None, 40)
        exit_text = button_font.render("Exit", 0, (255, 255, 255))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill((0, 0, 0))
        exit_surface.blit(exit_text, (10, 10))
        exit_rectangle = exit_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 25))
        screen.blit(exit_surface, exit_rectangle)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_rectangle.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            pygame.event.pump()
def main():

    pygame.init()
    screen_width = 550
    screen_height = 550
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Sudoku')
    screen.fill(bg_color)
    font = pygame.font.SysFont('Helvetica', 50)

    # Enter start screen and select difficulty
    selected_difficulty = draw_start_screen(screen,screen_width,screen_height)

    if selected_difficulty == "easy":
        pygame.display.set_caption("Sudoku - Easy")
        board = generate_sudoku(81,30) # Generates Easy Sudoku Board

    elif selected_difficulty == "medium":
        pygame.display.set_caption("Sudoku - Medium")
        board = generate_sudoku(81,40) # Generates Medium Sudoku Board

    elif selected_difficulty == "hard":
        pygame.display.set_caption("Sudoku - Hard")
        board = generate_sudoku(81,50) # Generates Hard Sudoku board
    screen.fill(bg_color) # Clear Screen
    draw_grid(screen) # Draw the grid to place the Sudoku board on


    # making a copy of the board for later use

    original = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]


    set_board(screen,board,font)
    rectangle_list = set_button(screen,screen_width,screen_height) # List to store rectangle objects for comparison
    pygame.display.update()


    while True:

        for event in pygame.event.get():

            # Mouse button click on cell
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # obtaining the coordinate from Mouse button click
                coord = pygame.mouse.get_pos()
                # floor division by 50 to place digit in cell
                place(screen, (coord[0] // 50, coord[1] // 50),board,original,screen,screen_width,screen_height)


            if event.type == pygame.MOUSEBUTTONDOWN:
                # Resets the board using the copy created at initiation
                if rectangle_list[0].collidepoint(event.pos):
                    board = original
                    screen.fill(bg_color)
                    draw_grid(screen)
                if rectangle_list[1].collidepoint(event.pos):
                    # Returns to the Start Screen to select a different difficulty level
                    selected_difficulty = draw_start_screen(screen, screen_width, screen_height)

                    if selected_difficulty == "easy":
                        pygame.display.set_caption("Sudoku - Easy")
                        board = generate_sudoku(81, 30)
                        screen.fill(bg_color)
                        draw_grid(screen)
                        set_board(screen, board, font)
                        set_button(screen, screen_width, screen_height)
                        pygame.display.update()
                    elif selected_difficulty == "medium":
                        pygame.display.set_caption("Sudoku - Medium")
                        board = generate_sudoku(81, 40)
                        screen.fill(bg_color)
                        draw_grid(screen)
                        set_board(screen, board, font)
                        set_button(screen, screen_width, screen_height)
                        pygame.display.update()
                    elif selected_difficulty == "hard":
                        pygame.display.set_caption("Sudoku - Hard")
                        board = generate_sudoku(81, 50)
                        screen.fill(bg_color)
                        draw_grid(screen)
                        set_board(screen, board, font)
                        set_button(screen, screen_width, screen_height)

                if rectangle_list[2].collidepoint(event.pos):
                    # Quits the game when player pushes the exit button
                    pygame.quit()

            # allows user to quit
            if (event.type == pygame.QUIT):
                pygame.quit()
                return


            pygame.event.pump()
if __name__ == '__main__':
    main()