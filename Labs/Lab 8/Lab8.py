# -*- coding: utf-8 -*-

'''
def drawBoard(lists):
    divider = "-+-+-"
    for i in range(len(lists)):
        row = lists[i] 
        nicerow = row[0] + "|" + row[1] + "|" + row[2]
        if i < 2:
            print(nicerow)
            print(divider)
        else:
            print(nicerow)
'''        
def drawBoard(board):
    rows = "\n-+-+-\n".join(["|".join(board[0]),
                        "|".join(board[1]),
                        "|".join(board[2]) ])
    
    print(rows)
    
            
def emptyBoard():
    empty = [[" ",  " ", " "], [" ",  " ", " "], [" ",  " ", " "]]
    return empty 

def play(board, char, space):
    
    space = space - 1
    r = space//3 
    c = space % 3

    board[r][c] = char
    
    
def isFull(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True 

def winner(board, char):
    for row in range(3):
        if board[row] == char:
            return True 
        elif 
        for col in range(3):
            if board[row][col] == "X":
                return False]
   