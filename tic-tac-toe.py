import tkinter as tk
from tkinter import ttk
import random
from typing import List, Optional
import time

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe Pro")
        self.window.configure(bg='#1a2b3c')
        
        # تهيئة متغيرات اللعبة
        self.current_player = 'X'
        self.board = [''] * 9
        self.difficulty = tk.StringVar(value='easy')
        self.game_over = False
        self.scores = {'X': 0, 'O': 0, 'tie': 0}
        
        self.setup_ui()
        
    def setup_ui(self):
        # إنشاء الحاوية الرئيسية
        self.container = tk.Frame(self.window, bg='#1a2b3c', padx=25, pady=25)
        self.container.pack(expand=True)
        
        # العنوان
        title = tk.Label(self.container, text="Tic Tac Toe Pro", 
                        font=('Arial', 28, 'bold'), fg='white', bg='#1a2b3c')
        title.pack(pady=20)
        
        # اختيار مستوى الصعوبة
        difficulty_frame = tk.Frame(self.container, bg='#1a2b3c')
        difficulty_frame.pack(pady=15)
        
        style = ttk.Style()
        style.configure('Difficulty.TCombobox', 
                       background='#1a2b3c',
                       fieldbackground='rgba(255, 255, 255, 0.15)',
                       foreground='white')
        
        difficulty_selector = ttk.Combobox(difficulty_frame, 
                                         textvariable=self.difficulty,
                                         values=['easy', 'medium', 'hard'],
                                         state='readonly',
                                         style='Difficulty.TCombobox')
        difficulty_selector.pack()
        
        # لوحة النتائج
        self.create_scoreboard()
        
        # لوحة اللعب
        self.create_game_board()
        
        # أزرار التحكم
        self.create_control_buttons()
        
    def create_scoreboard(self):
        stats_frame = tk.Frame(self.container, bg='#1a2b3c', pady=15)
        stats_frame.pack(fill='x')
        
        # إنشاء صناديق النتائج
        self.score_labels = {}
        
        for i, (player, color) in enumerate([('X', '#ff6b6b'), ('tie', 'white'), ('O', '#ffd93d')]):
            stat_box = tk.Frame(stats_frame, bg='#1a2b3c')
            stat_box.grid(row=0, column=i, padx=10, sticky='nsew')
            
            label = tk.Label(stat_box, 
                           text=f"{'Player' if player == 'X' else 'Computer' if player == 'O' else 'Ties'} ({player})",
                           fg='white', bg='#1a2b3c')
            label.pack()
            
            score_label = tk.Label(stat_box, text='0',
                                 font=('Arial', 24, 'bold'),
                                 fg=color, bg='#1a2b3c')
            score_label.pack()
            
            self.score_labels[player] = score_label
        
        stats_frame.grid_columnconfigure(0, weight=1)
        stats_frame.grid_columnconfigure(1, weight=1)
        stats_frame.grid_columnconfigure(2, weight=1)
        
    def create_game_board(self):
        self.board_frame = tk.Frame(self.container, bg='#1a2b3c')
        self.board_frame.pack(pady=15)
        
        self.cells = []
        for i in range(9):
            cell = tk.Button(self.board_frame,
                           width=4, height=2,
                           font=('Arial', 24, 'bold'),
                           bg='#2a3b4c', fg='white',
                           relief='flat',
                           command=lambda x=i: self.handle_cell_click(x))
            cell.grid(row=i//3, column=i%3, padx=4, pady=4)
            self.cells.append(cell)
            
    def create_control_buttons(self):
        buttons_frame = tk.Frame(self.container, bg='#1a2b3c')
        buttons_frame.pack(pady=20)
        
        restart_btn = tk.Button(buttons_frame, text="Restart",
                              bg='#4CAF50', fg='white',
                              font=('Arial', 12, 'bold'),
                              command=self.reset_game)
        restart_btn.pack(side='left', padx=5)
        
        new_game_btn = tk.Button(buttons_frame, text="New Game",
                                bg='#2196F3', fg='white',
                                font=('Arial', 12, 'bold'),
                                command=self.start_new_game)
        new_game_btn.pack(side='left', padx=5)
        
    def handle_cell_click(self, index: int):
        if self.board[index] == '' and not self.game_over and self.current_player == 'X':
            self.make_move(index)
            
            if not self.game_over:
                self.window.after(500, self.make_computer_move)
                
    def make_move(self, index: int):
        self.board[index] = self.current_player
        self.update_cell(index)
        
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.scores[winner if winner != 'tie' else 'tie'] += 1
            self.update_score_display()
            self.show_winner_message(winner)
            return
            
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
    def update_cell(self, index: int):
        self.cells[index].configure(
            text=self.board[index],
            fg='#ff6b6b' if self.board[index] == 'X' else '#ffd93d'
        )
        
    def make_computer_move(self):
        if self.difficulty.get() == 'easy':
            move = self.make_random_move()
        elif self.difficulty.get() == 'medium':
            move = self.make_best_move() if random.random() < 0.5 else self.make_random_move()
        else:
            move = self.make_best_move()
            
        if move is not None:
            self.make_move(move)
            
    def make_random_move(self) -> Optional[int]:
        empty_cells = [i for i, cell in enumerate(self.board) if cell == '']
        return random.choice(empty_cells) if empty_cells else None
        
    def make_best_move(self) -> Optional[int]:
        best_score = float('-inf')
        best_move = None
        
        for i in range(9):
            if self.board[i] == '':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ''
                if score > best_score:
                    best_score = score
                    best_move = i
                    
        return best_move
        
    def minimax(self, board: List[str], depth: int, is_maximizing: bool) -> int:
        winner = self.check_winner()
        if winner == 'O':
            return 1
        if winner == 'X':
            return -1
        if winner == 'tie':
            return 0
            
        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == '':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ''
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == '':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ''
                    best_score = min(score, best_score)
            return best_score
            
    def check_winner(self) -> Optional[str]:
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # أفقي
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # عمودي
            [0, 4, 8], [2, 4, 6]  # قطري
        ]
        
        for pattern in win_patterns:
            a, b, c = pattern
            if (self.board[a] and 
                self.board[a] == self.board[b] and 
                self.board[a] == self.board[c]):
                return self.board[a]
                
        if '' not in self.board:
            return 'tie'
        return None
        
    def show_winner_message(self, winner: str):
        message = "تعادل!" if winner == 'tie' else f"الفائز هو {winner}!"
        # يمكنك إضافة نافذة منبثقة هنا لعرض الرسالة
        
    def update_score_display(self):
        for player, score in self.scores.items():
            self.score_labels[player].configure(text=str(score))
            
    def reset_game(self):
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_over = False
        for cell in self.cells:
            cell.configure(text='')
            
    def start_new_game(self):
        self.scores = {'X': 0, 'O': 0, 'tie': 0}
        self.update_score_display()
        self.reset_game()
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
