board = [" " for _ in range(9)]

def view_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def is_winner(b, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any([all([b[i] == player for i in pos]) for pos in win_positions])

def check_tie(b):
    return " " not in b

def minimax(b, is_maximizing):
    if is_winner(b, "O"):
        return 1
    if is_winner(b, "X"):
        return -1
    if check_tie(b):
        return 0

    if is_maximizing:
        best = -100
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = " "
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = " "
                best = min(best, score)
        return best

def next_move():
    best_score = -100
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def start_game():
    print("Tic-Tac-Toe AI  (You = X, AI = O)")

    while True:
        view_board()

        # User move
        user = int(input("Enter position (0-8): "))
        if board[user] != " ":
            print("Invalid move!")
            continue
        board[user] = "X"

        if is_winner(board, "X"):
            print_board()
            print("You win!")
            break

        if check_tie(board):
            print_board()
            print("It's a draw!")
            break

        # bot move
        bot = next_move()
        board[bot] = "O"

        if is_winner(board, "O"):
            view_board()
            print("AI wins!")
            break

        if check_tie(board):
            view_board()
            print("It's a draw!")
            break

start_game()
