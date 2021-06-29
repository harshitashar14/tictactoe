import pygame

pygame.init()
# board
board = [' ' for x in range(10)]  # we want 0th empty

# icons and title
screen = pygame.display.set_mode((350, 450))
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)

# which screen
scr = 'first'
# first screen
cover = pygame.image.load('cover2.png')
cover = pygame.transform.scale(cover, (250, 250))

# first screen message
first_msg_font = pygame.font.Font('freesansbold.ttf', 32)
start_msg_font = pygame.font.Font('freesansbold.ttf', 17)

# update score and instructions
score_font = pygame.font.Font('freesansbold.ttf', 20)

# x and o
xo = pygame.image.load('close.png')
o = pygame.image.load('o.png')


def firstMsg():
    msg = first_msg_font.render("Tic Tac Toe", True, (0, 0, 0))
    screen.blit(msg, (85, 30))
    start_msg = start_msg_font.render("Press space to start the game", True, (0, 0, 0))
    screen.blit(start_msg, (40, 380))
    screen.blit(cover, (50, 80))


# game screen
def update_score(st):
    screen.fill((0, 0, 0), (0, 350, 350, 450))
    if not st == '' and not st == " ":
        text = score_font.render(st, True, (225, 225, 225))

        text_rect = text.get_rect(**center)

        screen.blit(text, text_rect)



def isWinner(bo, le):
    return horizontal(bo, le, 1) or horizontal(bo, le, 4) or horizontal(bo, le, 7) or vertical(bo, le, 1) or vertical(
        bo, le, 2) or vertical(bo, le, 3) or diagonal(bo, le, 1) or diagonal(bo, le, 3)


def horizontal(bo, le, i):
    return (bo[i] == le and bo[i + 1] == le and bo[i + 2] == le)


def vertical(bo, le, i):
    return (bo[i] == le and bo[i + 3] == le and bo[i + 6] == le)


def diagonal(bo, le, i):
    if i == 1:
        return bo[1] == le and bo[5] == le and bo[9] == le
    return bo[3] == le and bo[5] == le and bo[7] == le


def gameScrn():
    pygame.draw.line(screen, (0, 0, 0), (350 / 3, 0), (350 / 3, 350), 5)
    pygame.draw.line(screen, (0, 0, 0), (700 / 3, 0), (700 / 3, 350), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 350 / 3), (350, 350 / 3), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 700 / 3), (350, 700 / 3), 5)
    if board[1] == board[2] == board[3] == board[4] == board[5] == board[6] == board[7] == board[8] == board[9] == ' ':
        update_score("Welcome.X's move.")
    if isWinner(board, 'X') or isWinner(board, 'O'):
        if horizontal(board, 'X', 1) or horizontal(board, "O", 1):
            pygame.draw.line(screen, (225, 0, 0), (0+24, 350 / 6), (350-20, 350 / 6), 5)
        elif horizontal(board, 'X', 4) or horizontal(board, "O", 4):
            pygame.draw.line(screen, (225, 0, 0), (0+24, 350 / 2), (350-20,350 / 2), 5)
        elif horizontal(board, 'X', 7) or horizontal(board, "O", 7):
            pygame.draw.line(screen, (225, 0, 0), (0+24, (350 * 5) / 6), (350-20, (350 * 5) / 6), 5)
        elif vertical(board, 'X', 1) or vertical(board, "O", 1):
            pygame.draw.line(screen, (225, 0, 0), (350 / 6,0+24), (350 / 6,350-20), 5)
        elif vertical(board, 'X', 2) or vertical(board, "O", 2):
            pygame.draw.line(screen, (225, 0, 0), (350 / 2,0+24), (350 / 2,350-20), 5)
        elif vertical(board, 'X', 3) or vertical(board, "O", 3):
            pygame.draw.line(screen, (225, 0, 0), ((350 * 5) / 6,0+24), ((350 * 5) / 6,350-20), 5)
        elif diagonal(board,'X',1) or diagonal(board,'O',1):
            pygame.draw.line(screen, (225, 0, 0), (24,24), (350-24,350-24),5)
        elif diagonal(board,'X',1) or diagonal(board,'O',3):
            pygame.draw.line(screen, (225, 0, 0), (350-24,24), (24,350-24),5)

center = {'center': (350 / 2, 400)}


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def playerMove(x, y):
    run = True
    move = 0
    while run:

        if x < 350 / 3 and 0 < y and 350 > y:
            if y < 350 / 3:
                move = 1
            elif y > 350 / 3 and y < 700 / 3:
                move = 4
            else:
                move = 7
        if x > 350 / 3 and x < 700 / 3 and 0 < y and 350 > y:
            if y < 350 / 3:
                move = 2
            elif y > 350 / 3 and y < 700 / 3:
                move = 5
            else:
                move = 8

        if x < 350 and x > 700 / 3 and 0 < y and 350 > y:
            if y < 350 / 3:
                move = 3
            elif y > 350 / 3 and y < 700 / 3:
                move = 6
            else:
                move = 9

        if move != 0:
            if spaceIsFree(move):
                run = False
                insertLetter('X', move)

    return move


def compMove():
    boardC = board[:]

    freeMoves = list(filter(lambda x: boardC[x] == ' ', range(1, 10)))

    # moves=i
    t = [-800, 10]
    for i in freeMoves:
        boardC[i] = 'O'
        m = selMove(boardC, 'X', 2)
        if t[0] == m[0] and t[1] > m[1]:
            t = m[:]
            moves = i
        elif t[0] < m[0]:
            t = m[:]  # t=[1,1]
            moves = i

        boardC[i] = ' '
    return moves


def selMove(boardC, c, dep):
    boardp = boardC[:]
    freeMoves = list(filter(lambda x: boardp[x] == ' ', range(1, 10)))

    if isWinner(boardp, 'O') == 1:
        return [1, dep-1]
    if isWinner(boardp, 'X') == 1:
        return [-1, dep-1]
    if isBoardFull(boardp) == 1:
        return [0, dep-1]

    if c == 'X':
        minMove = [800, 20]
        for i in range(len(freeMoves)):
            boardp[freeMoves[i]] = 'X'

            ret = selMove(boardp, 'O', dep + 1)
            if minMove[0] > ret[0]:
                minMove = ret[:]
            elif minMove[0] == ret[0] and ret[1] < minMove[1]:
                minMove = ret[:]

            boardp[freeMoves[i]] = ' '
        return minMove

    if c == 'O':
        maxMove = [-800, 20]
        for i in range(len(freeMoves)):
            boardp[freeMoves[i]] = 'O'
            ret = selMove(boardp, 'X', dep + 1)
            if maxMove[0] == ret[0] and ret[1]<maxMove[1]:
                maxMove = ret[:]
            elif maxMove[0]<ret[0]:
                maxMove = ret[:]
            boardp[freeMoves[i]] = ' '
        return maxMove


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    return True


def update_board():
    for m in range(1, len(board)):
        if m <= 3:
            y = 30
            x = (m - 1) * 350 / 3 + 30
        elif m <= 6:
            y = 350 / 3 + 30
            x = (m - 4) * 350 / 3 + 30
        else:
            y = 700 / 3 + 30
            x = (m - 7) * 350 / 3 + 30

        if board[m] == 'X':
            screen.blit(xo, (x, y))
        elif board[m] == 'O':
            screen.blit(o, (x, y))


def main(xx, yy, p):
    if p == 'p':
        if not (isWinner(board, 'O')):

            move = playerMove(xx, yy)

        else:
            return 'You lose.'
        # pygame.time.wait(1000)
    else:
        if not (isWinner(board, 'X')):
            move = 0
            if not isBoardFull(board):
                move = compMove()
            if move == 0:
                return 'Tie Game.'

            else:
                insertLetter('O', move)
                if isWinner(board, 'O'):
                    return 'You lose.'

        else:
            return 'You won.Good job!'

        if isBoardFull(board):
            return "Tie Game"
    update_board()
    if p == 'p' and not isBoardFull(board):
        update_score("O's move.")
    else:
        return "X's move."
    pygame.display.update()
    return ""


res = ''
p = 'p'
# main loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and scr == 'first' and event.key == pygame.K_SPACE:
            scr = 'game'
        if event.type == pygame.MOUSEBUTTONDOWN and not isBoardFull(board) and not isWinner(board,
                                                                                            'X') and not isWinner(board,
                                                                                                                  'O'):
            xx, yy = pygame.mouse.get_pos()
            res = main(xx, yy, 'p')
            p = 'c'

            pygame.time.wait(500)
            res = main(xx, yy, 'c')
    screen.fill((225, 170, 170))
    if scr == 'first':
        firstMsg()

    else:

        gameScrn()

        update_board()
        if not res == "" and not res == " ":
            update_score(res)

    pygame.display.update()
