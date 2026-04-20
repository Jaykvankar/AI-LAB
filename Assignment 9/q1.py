import math

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], board[i+1], board[i+2])
    print()

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != '.':
            return board[a]
    return None

def is_full(board):
    return '.' not in board

def minimax(board, is_max, depth=0):
    winner = check_winner(board)
    if winner == 'O': return 10 - depth
    if winner == 'X': return depth - 10
    if is_full(board): return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == '.':
                board[i] = 'O'
                best = max(best, minimax(board, False, depth+1))
                board[i] = '.'
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == '.':
                board[i] = 'X'
                best = min(best, minimax(board, True, depth+1))
                board[i] = '.'
        return best

def best_move(board):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == '.':
            board[i] = 'O'
            print("search tree")
            print_board(board)
            val = minimax(board, False)
            board[i] = '.'
            if val > best_val:
                best_val = val
                move = i
    return move

def play():
    board = ['.'] * 9
    print("You are X, AI is O")
    print("Positions:")
    print("0 1 2\n3 4 5\n6 7 8\n")
    print_board(board)

    while True:
        # Human move (X) - plays first
        while True:
            try:
                pos = int(input("Your move (0-8): "))
                if 0 <= pos <= 8 and board[pos] == '.':
                    board[pos] = 'X'
                    break
                else:
                    print("Cell taken or invalid.")
            except (ValueError, IndexError):
                print("Invalid input.")
        
        print_board(board)

        if check_winner(board):
            print("You win!")
            break
        if is_full(board):
            print("Draw!")
            break

        # AI move (O)
        move = best_move(board)
        board[move] = 'O'
        print(f"AI plays at position {move}")
        print_board(board)

        if check_winner(board):
            print("AI wins!")
            break
        if is_full(board):
            print("Draw!")
            break

if __name__ == "__main__":
    play()