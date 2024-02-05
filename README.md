
## Code Structure:

### `solve` Function:
- The `solve` function takes a 2D list (`board`) as input and modifies it according to the problem requirements.
- It uses Depth-First Search (DFS) to mark connected 'O's as safe.
- The function traverses the borders of the board, marking 'O's and their connected cells as safe ('S').
- After marking, it iterates through the entire board, flipping 'O' to 'X', and 'S' back to 'O'.

### `dfs` Helper Function:
- The `dfs` function is a recursive helper function used by the `solve` function.
- It explores the neighboring cells in all four directions, marking connected 'O's as safe.

### User Input:
- The code takes user input for the number of rows and columns in the board.
- Users are then prompted to input the board elements row-wise as an array of strings.
- Each input string is split into a list of characters, and the resulting lists are added to the `board` list.

### Example Usage:
- The example usage section demonstrates how to use the code with user input.
- After calling the `solve` function, the modified board is printed.

## Usage:
1. Run the script.
2. Enter the number of rows and columns for the board.
3. Input the board elements row-wise.
4. View the modified board after executing the `solve` function.

This Python code provides a solution to the "Surrounded Regions" problem on LeetCode, using Depth-First Search to efficiently mark and flip the surrounded regions.

