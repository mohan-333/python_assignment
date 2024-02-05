def solve(board):
    if not board or not board[0]:
        return
    rows, cols = len(board), len(board[0])

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'O':
            return
        board[row][col] = 'S'
        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col-1)
        dfs(row, col+1)
    for i in range(rows):
        dfs(i, 0)
        dfs(i, cols-1)
    for i in range(cols):
        dfs(0, i)
        dfs(rows-1, i)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == 'S':
                board[i][j] = 'O'


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

board = []

print("Enter the board elements row-wise:")
for _ in range(rows):
    row = list(input().split())
    board.append(row)

solve(board)

# Print the modified board
print("Modified Board:")
for row in board:
    print(" ".join(row))


