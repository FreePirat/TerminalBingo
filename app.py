import random
import os
import keyboard
from colorama import init, Fore, Style
import time
init()  # Needed for Windows

bList = random.sample(range(1, 16), 5)
iList = random.sample(range(16, 31), 5)
nList = random.sample(range(31, 46), 5)
gList = random.sample(range(46, 61), 5)
oList = random.sample(range(61, 76), 5)

# Make the board a dictionnary the player can interact with
board = [
    [
        {"value": bList[i], "marked": False}, 
        {"value": iList[i], "marked": False},
        {"value": nList[i], "marked": False},
        {"value": gList[i], "marked": False},
        {"value": oList[i], "marked": False}
    ]
    for i in range(5)
]

# Cursor position
cursor_row, cursor_col = 0, 0

# Clear the console when updating the board
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    clear()
    print("   B   I   N   G   O")
    print("*" * 23)
    for r in range(5):
        row = ""
        for c in range(5):
            num = board[r][c]["value"]
            if r == cursor_row and c == cursor_col:
                # Highlight the selected number
                if( board[r][c]["marked"]):
                    row += f"{Fore.GREEN}[{str(num).rjust(2)}]{Style.RESET_ALL} " # Green (Selected and Marked)
                else:
                    row += f"[{str(num).rjust(2)}] " # Not green (Selected but not Marked)
            else:
                if board[r][c]["marked"]:
                    row += f" {Fore.GREEN}{str(num).rjust(2)}{Style.RESET_ALL}  " # Green (Marked)
                else:
                    row += f" {str(num).rjust(2)}  "  # Display the number normally
        print(row)
    print("*" * 23)
    print("Use the arrow keys to move, Enter to select, ESC to quit")

# Game Start!
    
print_board()

# Main gameplay loop

while True:

    if keyboard.is_pressed('up') and cursor_row > 0:
        cursor_row -= 1
        print_board()
        time.sleep(0.1)
    elif keyboard.is_pressed('down') and cursor_row < 4:
        cursor_row += 1
        print_board()
        time.sleep(0.1)
    elif keyboard.is_pressed('left') and cursor_col > 0:
        cursor_col -= 1
        print_board()
        time.sleep(0.1)
    elif keyboard.is_pressed('right') and cursor_col < 4:
        cursor_col += 1
        print_board()
        time.sleep(0.1)
    elif keyboard.is_pressed('enter'):
        board[cursor_row][cursor_col]['marked'] = not board[cursor_row][cursor_col]['marked']
        print_board()
        time.sleep(0.1)
    elif keyboard.is_pressed('esc'):
        break