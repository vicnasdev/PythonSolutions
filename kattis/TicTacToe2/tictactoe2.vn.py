
grid = ["" for _ in range(9)]


lines = [
    # Horizontal
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    
    # Vertical
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),

    # Diags    
    (0, 4, 8),
    (2, 4, 6)
]

for case in range(int(input())):
    i = 0
    for _ in range(3):
        for cell in input():
            grid[i] = cell
            i += 1
            
    try: input()
    except: pass # No empty line after test case
    
    wins = {
        "O": False,
        "X": False,
    }
    
    for i, j, k in lines:
        if grid[i]==grid[j]==grid[k] and grid[i] in "X0":
            wins[grid[i]] = True
    
    # X wins
    if wins["X"] and not wins["O"] and grid.count("X")==grid.count("O")+1:
        print("yes")
        
    # X loses
    elif not wins["X"] and wins["O"] and grid.count("X")==grid.count("O"):
        print("yes")

    # Undecided
    elif wins["X"]==wins["O"]==False and 0<=grid.count("X")-grid.count("O")<=1:
        print("yes")
    
    # Anything else is impossible
    else:
        print("no")