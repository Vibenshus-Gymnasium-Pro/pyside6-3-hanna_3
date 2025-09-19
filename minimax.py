# A simple Python3 program to find
# maximum score that
# maximizing player can get

import sys 
import string
import re, random
from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import QWidget, QDialogButtonBox
#Import af filen/modulet roeversprog.py -
# Læg mærke til at .py ikke er taget med.
from twoplayerview_tictactoe_gui import Ui_Form
# Import af de almindelige elementer i pyside6
from PySide6.QtWidgets import QApplication, QMainWindow
# Import af brugerfladen fra pythonfilen, som er generet vha pyside6-uic
from mainview_tictactoe__gui import Ui_MainWindow
import math
from tictactoe import twoplayerview_tictactoe






class single_player_view(QWidget):
    winner = None
    def __init__(self):
        super().__init__()
        # Her oprettes self.ui ud fra den klasse som er i den genererede pythonfil
        self.ui = Ui_Form()
        # Her sættes brugerfladen op.
        self.ui.setupUi(self)
        self.setFixedSize(QSize(470, 400))
        self.setWindowTitle("Tic Tac Toe - single Player")
        self.board = [self.ui.felt1, self.ui.felt2, self.ui.felt3,
                      self.ui.felt4, self.ui.felt5, self.ui.felt6,
                      self.ui.felt7, self.ui.felt8, self.ui.felt9]
        
        self.player = 'X'
        self.turn = self.player
        self.ui.label.setText(f"Current Player: {self.turn}")
        
        #self.__class__.winner
        self.minimax_player = 'O' # if self.current_player == 'X' else 'X'
        self.x_score = 0
        self.y_score = 0
        self.minimizer =''
        self.maximizer =''

        
        for button in self.board: # for each element in list it checks if its clicked
            button.clicked.connect(lambda checked, b=button: self.make_move(b)) 
            # lambda checked is needed for clicked signal as it sends a bool argument that gets passed with the button
            # lambda b=button is used to create a new variable b that holds the current button in the loop
        
   
    def reset_game(self):
        for b in self.board:
            b.setText('')
        self.__class__.winner = None
        self.player = 'X'
        self.minimax_player = 'O' #if self.player == 'X' else 'X'
        self.turn = self.player
        self.ui.label.setText(f"Player: {self.player} begins")
        self.ui.dialog_buttons.hide()
        self.ui.dialog_label.hide()

    def make_move(self, b):
        if b.text()== "" and self.turn == self.player: 
            b.setText(self.player)
            self.check_winner()
            self.switch_turn()
            self.ui.label.setText(f"Current Player: {self.turn}")
            if self.check_winner() == True:
                self.play_again()
        else:
            self.computer_move()
    
    def computer_move(self):
        if self.turn == self.minimax_player:
            bestmove = self.best_move()
            #for button in self.board:
                #if button.text() == '' and self.board.index(button) == bestmove:
                
            #        print( "computer's turn 2")
            #        button.setText(self.minimax_player)
            m = [self.board.index(x) for x in self.board if x.text() == '']
            for i in m:
                if i == bestmove:
                    print( "computer's turn")
                    self.board[i].setText(self.minimax_player)
            #self.board[best_move].setText(self.minimax_player)
            self.switch_turn()
            self.check_winner(board=self.board)
            if self.check_winner(board=self.board) == True:
                self.play_again()

#create a minimizer (oponent) that choses the worst possible move for us(the computer)
# make so that when current player changes the minimax turn stars - singleplayer.clicked.connect(minimax) checked
# assing randomly x / o to minimax - cheked
#the score of the avialable moves need to be define by the minimizer moves and the maximizer respond (def moveValue():)
# order: if gameover: retunt players score from final state, else get a list of new game states for posible moves
# create score list form game states
# for state in list return minimax result and maximax result
# if is player turn return maximun score of the list

#create a list of the empty board fields and chose the maximum scoring move (the maximizer)
    def minimax(self):
        winner = self.check_winner()
        if winner == self.minimizer:
            return -10
        elif winner == self.maximizer:
             return 10
        elif winner == 'tie':
            return 0    
        scores = []
        for i in self.board:
            if i.text() == '':
                if self.minimizer != self.maximizer:
                    i.setText(self.maximizer) 
                else:
                    i.setText(self.minimizer) 

                score = self.minimax() # switch players betwen moves
                scores.append(score) # add the score of the move to the list
                i.setText('') # undo the move
                    
        return max(scores) if self.maximizer != self.minimizer else min(scores)
            # when all moves have been evaluated,break the loop and choose the move with the highest score
 
    def best_move(self):
        best_score = -float('inf')# means negative infinity
        move = [0]
        #m = [self.board.index(x) for x in self.board if x.text() == '']
        #turn = lambda# switch between players
        for i in self.board:
                if self.minimizer != self.maximizer:
                    i.setText(self.maximizer) 
                else:
                    i.setText(self.minimizer) 
                score = self.minimax()
                
                 #self.board, 'O' if self.minimizer == 'X' else 'X', self.maximizer
        # this represents the score from the minimax function for the maximizer
                i.setText('')
                if score > best_score:
                    best_score = score
                    move = [self.board.index(i)] # get the index of the button in the board list
        return move


    def play_again(self):
        self.ui.dialog_buttons.show()
        self.ui.dialog_label.show()
        self.ui.dialog_buttons.accepted.connect(lambda: (self.reset_game(), self.ui.dialog.accept()))
        self.ui.dialog_buttons.rejected.connect(lambda: (self.ui.dialog.reject(),self.close()))
       

    def switch_turn(self):
        if self.turn == self.player:
            self.turn = self.minimax_player
            self.computer_move()
        else:
            self.turn = self.player
        
    def check_winner(self):
        wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontals
                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticals
                (0, 4, 8), (2, 4, 6)]  # diagonals
        
        self.board_matrix = [[self.button.text() for self.button in self.board]]
        for i in wins:
            if self.board_matrix[0] == self.board_matrix[1] == self.board_matrix[2] and self.board_matrix[1] != '':
                self.play_again()
                self.__class__.winner = self.board[line[0]]
                if self.__class__.winner == 'X' :
                    self.x_score += 1
                elif self.__class__.winner == 'O' :
                    self.y_score +=1
                """kunne bruge map function her?? tjek"""
                self.ui.label_2.setText(f"Score: X: {self.x_score} - O: {self.y_score}")
                return True  
            return self.board[line[0]]
            
            
        if all(cell != "" for cell in self.board): # returns true for boolean in all variables in list
            return 'tie'
        return True
    
"""def minimax (curDepth, nodeIndex,
             maxTurn, scores, 
             targetDepth):

    # base case : targetDepth reached
    if (curDepth == targetDepth): 
        return scores[nodeIndex]
    
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2, 
                    False, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                    False, scores, targetDepth))
    
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, 
                     True, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, 
                     True, scores, targetDepth))
    
# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))"""

# This code is contributed
# by rootshadow