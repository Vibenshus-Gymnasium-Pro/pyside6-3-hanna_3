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


class twoplayerview_tictactoe(QWidget):
    winner = None
    def __init__(self):
        super().__init__()
        # Her oprettes self.ui ud fra den klasse som er i den genererede pythonfil
        self.ui = Ui_Form()
        # Her sættes brugerfladen op.
        self.ui.setupUi(self)
        self.setFixedSize(QSize(470, 400))
        self.setWindowTitle("Tic Tac Toe - 2 Player")
        self.board = [self.ui.felt1, self.ui.felt2, self.ui.felt3,
                      self.ui.felt4, self.ui.felt5, self.ui.felt6,
                      self.ui.felt7, self.ui.felt8, self.ui.felt9]
        
        self.current_player = random.choice(['X', 'O'])
        self.ui.label.setText(f"Current Player: {self.current_player}")
        #self.__class__.winner

        self.x_score = 0
        self.y_score = 0

        
        for button in self.board: # for each element in list it checks if its clicked
            button.clicked.connect(lambda checked, b=button: self.make_move(b)) 
            # lambda checked is needed for clicked signal as it sends a bool argument that gets passed with the button
            # lambda b=button is used to create a new variable b that holds the current button in the loop
        
   
    def reset_game(self):
        for button in self.board:
            button.setText('')
        self.__class__.winner = None
        self.current_player = random.choice(['X', 'O'])
        self.ui.label.setText(f"Player: {self.current_player} begins")
        self.ui.dialog_buttons.hide()
        self.ui.dialog_label.hide()

    def make_move(self, b):
        if b.text()== "": 
            b.setText(self.current_player)
            self.current_player= self.switch_player()
            self.check_winner()
            if self.check_winner() == True:
                self.play_again()

    def play_again(self):
        self.ui.dialog_buttons.show()
        self.ui.dialog_label.show()
        self.ui.dialog_buttons.accepted.connect(lambda: (self.reset_game(), self.ui.dialog.accept()))
        self.ui.dialog_buttons.rejected.connect(lambda: (self.ui.dialog.reject(),self.close()))
       

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        
        self.ui.label.setText(f"Current Player: {self.current_player}")
        return self.current_player
    
    def check_horizontal(self):
        for i in range(0,9,3): #starts at 0 (default) ends at 9, steps by 3
            if self.board[i].text() == self.board[i+1].text() == self.board[i+2].text() and self.board[i+1].text() != "":
                self.__class__.winner = self.board[i].text()
                return True
                
            
            
    def check_vertical(self):
        for i in range(0,3,1): #starts at 0 stops at 3 and steps by 1
            if self.board[i].text() == self.board[i+3].text() == self.board[i+6].text() and self.board[i+3].text() != "":
                self.__class__.winner = self.board[i].text()
                return True
                
            
    def check_diagonal(self):
        if self.board[0].text() == self.board[4].text() == self.board[8].text() and self.board[4].text() != "":
            self.__class__.winner = self.board[0].text()
            return True  
        elif self.board[2].text() == self.board[4].text() == self.board[6].text() and self.board[4].text() != "":
            self.__class__.winner = self.board[2].text()
            return True
            
   
    def check_tie(self):
        if self.__class__.winner is None and all(b.text() != "" for b in self.board): # returns true for boolean in all variables in list
            print("It's a tie!")
            self.ui.label.setText("It's a tie!")

            self.x_score += 0
            self.y_score += 0
            return True
        
    def check_winner(self):
        if self.check_horizontal() or self.check_vertical() or self.check_diagonal(): #if they are ==true
            self.ui.label.setText(f"Winner is {self.__class__.winner}!")
            if self.__class__.winner == 'X' :
                self.x_score += 1
            elif self.__class__.winner == 'O' :
                self.y_score +=1
                """kunne bruge map function her?? tjek"""
            self.ui.label_2.setText(f"Score: X: {self.x_score} - O: {self.y_score}")
            return True
        elif self.check_tie():
            return True 
        else:
            return False


# Vores nye klasse, som starter med at nedarve fra almindeligt QMainWindow
class mainview_tictactoe(QMainWindow):
    def __init__(self):
        super().__init__()
        # Her oprettes self.ui ud fra den klasse som er i den genererede pythonfil
        self.ui = Ui_MainWindow()
        # Her sættes brugerfladen op.
        self.ui.setupUi(self)
        # Her sættes vinduestitlen til noget andet end i Designer.
        # Læg mærke til at self.ui IKKE anvendes men blot self.
        self.setWindowTitle("tic tac toe - main menu")
        self.setFixedSize(QSize(470, 400))
        self.ui.twoplayer_button.clicked.connect(self.show_new_window)
        self.ui.singleplayer_button.clicked.connect(self.show_new_window_minimax)

    
    def show_new_window(self):
        self.close()  # Close main window when opening new window
        self.window = twoplayerview_tictactoe()
        self.window.show()
    
        
    def show_new_window_minimax(self):
        self.close()  # Close main window when opening new window
        from minimax import single_player_view
        self.window = single_player_view()
        self.window.show()
    

program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
mainview_tictactoe = mainview_tictactoe()
mainview_tictactoe.show()
program.exec()