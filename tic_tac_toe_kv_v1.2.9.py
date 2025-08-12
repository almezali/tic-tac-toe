#!/usr/bin/env python3
"""
Tic Tac Toe v1.2.9
Developer: almezali
Modern Android-like interface with clear colored buttons, effects, transparency, and organized layout
Fixed window size: 600x400 pixels
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
from typing import List, Optional
import time

class ModernTicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe v1.2.9 - by almezali")
        
        # Fixed window size as requested: 600x400
        self.window.geometry("600x400")
        self.window.resizable(False, False)
        
        # Center window on screen
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - 600) // 2
        y = (screen_height - 400) // 2
        self.window.geometry(f"600x400+{x}+{y}")
        
        # Game variables
        self.current_player = 'X'
        self.board = [''] * 9
        self.difficulty = tk.StringVar(value='Medium')
        self.game_over = False
        self.scores = {'X': 0, 'O': 0, 'tie': 0}
        
        # Modern Android-like color scheme with Kvantum-inspired styling
        self.colors = {
            'bg_primary': '#1E1E2E',        # Dark background (Kvantum-like)
            'bg_secondary': '#2A2A3E',      # Secondary background
            'bg_card': '#313244',           # Card background with subtle transparency
            'surface': '#45475A',           # Surface color
            'primary': '#89B4FA',           # Primary blue (Kvantum accent)
            'secondary': '#F38BA8',         # Secondary pink
            'accent': '#A6E3A1',            # Accent green
            'warning': '#FAB387',           # Warning orange
            'error': '#F38BA8',             # Error red
            'success': '#A6E3A1',           # Success green
            'text_primary': '#CDD6F4',      # Primary text (high contrast)
            'text_secondary': '#BAC2DE',    # Secondary text
            'text_muted': '#6C7086',        # Muted text
            'border': '#585B70',            # Border color (Kvantum-style)
            'hover': '#6C7086',             # Hover color
            'shadow': '#11111B',            # Shadow color (deep)
            'transparent': '#00000000',     # Transparent
            'glass_bg': '#313244CC',        # Glass background (with transparency)
            'glass_border': '#585B7080',    # Glass border (with transparency)
            'kvantum_highlight': '#7C3AED', # Kvantum-style highlight
            'kvantum_shadow': '#0F0F23',    # Kvantum-style shadow
            'kvantum_border': '#4C4F69'     # Kvantum-style border
        }
        
        self.setup_ui()
        self.bind_events()
        
    def setup_ui(self):
        """Setup the modern Android-like UI"""
        # Main container with modern background
        self.main_frame = tk.Frame(
            self.window,
            bg=self.colors['bg_primary'],
            relief='flat'
        )
        self.main_frame.pack(fill='both', expand=True)
        
        # Create header
        self.create_header()
        
        # Create main content area
        self.create_main_content()
        
        # Create bottom controls
        self.create_bottom_controls()
        
    def create_header(self):
        """Create modern header with title and version"""
        header_frame = tk.Frame(
            self.main_frame,
            bg=self.colors['bg_secondary'],
            height=60,
            relief='flat'
        )
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="Tic Tac Toe",
            font=('Segoe UI', 20, 'bold'),
            fg=self.colors['text_primary'],
            bg=self.colors['bg_secondary']
        )
        title_label.pack(side='left', padx=20, pady=15)
        
        # Version and developer info
        version_label = tk.Label(
            header_frame,
            text="v1.2.9 • by almezali",
            font=('Segoe UI', 10),
            fg=self.colors['text_muted'],
            bg=self.colors['bg_secondary']
        )
        version_label.pack(side='right', padx=20, pady=15)
        
    def create_main_content(self):
        """Create main content area with game board and sidebar"""
        content_frame = tk.Frame(
            self.main_frame,
            bg=self.colors['bg_primary']
        )
        content_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Left sidebar for game info
        self.create_sidebar(content_frame)
        
        # Game board in center
        self.create_game_board(content_frame)
        
    def create_sidebar(self, parent):
        """Create modern sidebar with game information"""
        sidebar_frame = tk.Frame(
            parent,
            bg=self.colors['bg_primary'],
            width=180
        )
        sidebar_frame.pack(side='left', fill='y', padx=(0, 10))
        sidebar_frame.pack_propagate(False)
        
        # Current Player Card
        self.create_info_card(
            sidebar_frame, 
            "Current Player", 
            "✗", 
            self.colors['primary'],
            0, 10
        )
        
        # Difficulty Card
        self.create_difficulty_card(sidebar_frame, 80)
        
        # Scoreboard Card
        self.create_scoreboard_card(sidebar_frame, 160)
        
        # Control buttons below scoreboard
        self.create_sidebar_controls(sidebar_frame, 290)
        
    def create_info_card(self, parent, title, content, color, x, y):
        """Create a modern info card with Kvantum-like glass morphism effect"""
        # Card background with Kvantum-style rounded corners effect
        card_frame = tk.Frame(
            parent,
            bg=self.colors['bg_card'],
            relief='flat',
            bd=2,
            highlightbackground=self.colors['kvantum_border'],
            highlightthickness=1
        )
        card_frame.place(x=x, y=y, width=170, height=60)
        
        # Add Kvantum-style shadow effect (simulated with additional frame)
        shadow_frame = tk.Frame(
            parent,
            bg=self.colors['kvantum_shadow'],
            relief='flat'
        )
        shadow_frame.place(x=x+2, y=y+2, width=170, height=60)
        shadow_frame.lower()  # Put shadow behind main frame
        
        # Title with Kvantum styling
        title_label = tk.Label(
            card_frame,
            text=title,
            font=('Segoe UI', 9, 'bold'),
            fg=self.colors['text_muted'],
            bg=self.colors['bg_card']
        )
        title_label.pack(pady=(8, 0))
        
        # Content with Kvantum highlight
        self.current_player_label = tk.Label(
            card_frame,
            text=content,
            font=('Segoe UI', 16, 'bold'),
            fg=color,
            bg=self.colors['bg_card']
        )
        self.current_player_label.pack()
        
    def create_difficulty_card(self, parent, y):
        """Create difficulty selector card with Kvantum styling"""
        # Add Kvantum-style shadow effect
        shadow_frame = tk.Frame(
            parent,
            bg=self.colors['kvantum_shadow'],
            relief='flat'
        )
        shadow_frame.place(x=2, y=y+2, width=170, height=60)
        
        card_frame = tk.Frame(
            parent,
            bg=self.colors['bg_card'],
            relief='flat',
            bd=2,
            highlightbackground=self.colors['kvantum_border'],
            highlightthickness=1
        )
        card_frame.place(x=0, y=y, width=170, height=60)
        
        # Title
        title_label = tk.Label(
            card_frame,
            text="Difficulty",
            font=('Segoe UI', 9, 'bold'),
            fg=self.colors['text_muted'],
            bg=self.colors['bg_card']
        )
        title_label.pack(pady=(8, 0))
        
        # Custom styled combobox with Kvantum colors
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            'Kvantum.TCombobox',
            fieldbackground=self.colors['surface'],
            background=self.colors['surface'],
            foreground=self.colors['text_primary'],
            arrowcolor=self.colors['kvantum_highlight'],
            bordercolor=self.colors['kvantum_border'],
            lightcolor=self.colors['surface'],
            darkcolor=self.colors['surface'],
            selectbackground=self.colors['kvantum_highlight'],
            selectforeground=self.colors['bg_primary']
        )
        
        self.difficulty_combo = ttk.Combobox(
            card_frame,
            textvariable=self.difficulty,
            values=['Easy', 'Medium', 'Hard'],
            state='readonly',
            style='Kvantum.TCombobox',
            width=15,
            font=('Segoe UI', 10)
        )
        self.difficulty_combo.pack(pady=(0, 8))
        
    def create_scoreboard_card(self, parent, y):
        """Create modern scoreboard with Kvantum styling"""
        # Add Kvantum-style shadow effect
        shadow_frame = tk.Frame(
            parent,
            bg=self.colors['kvantum_shadow'],
            relief='flat'
        )
        shadow_frame.place(x=2, y=y+2, width=170, height=120)
        
        card_frame = tk.Frame(
            parent,
            bg=self.colors['bg_card'],
            relief='flat',
            bd=2,
            highlightbackground=self.colors['kvantum_border'],
            highlightthickness=1
        )
        card_frame.place(x=0, y=y, width=170, height=120)
        
        # Title
        title_label = tk.Label(
            card_frame,
            text="Scoreboard",
            font=('Segoe UI', 9, 'bold'),
            fg=self.colors['text_muted'],
            bg=self.colors['bg_card']
        )
        title_label.pack(pady=(8, 5))
        
        # Score entries
        self.score_labels = {}
        score_data = [
            ('Player X', 'X', self.colors['primary']),
            ('Ties', 'tie', self.colors['warning']),
            ('Player O', 'O', self.colors['secondary'])
        ]
        
        scores_frame = tk.Frame(card_frame, bg=self.colors['bg_card'])
        scores_frame.pack(fill='both', expand=True, padx=10, pady=(0, 8))
        
        for i, (label_text, key, color) in enumerate(score_data):
            # Score row
            row_frame = tk.Frame(scores_frame, bg=self.colors['bg_card'])
            row_frame.pack(fill='x', pady=2)
            
            # Label
            label = tk.Label(
                row_frame,
                text=label_text,
                font=('Segoe UI', 8),
                fg=self.colors['text_secondary'],
                bg=self.colors['bg_card']
            )
            label.pack(side='left')
            
            # Score with Kvantum highlight
            score_label = tk.Label(
                row_frame,
                text='0',
                font=('Segoe UI', 10, 'bold'),
                fg=color,
                bg=self.colors['bg_card']
            )
            score_label.pack(side='right')
            
            self.score_labels[key] = score_label
            
    def create_sidebar_controls(self, parent, y):
        """Create smaller control buttons side-by-side below scoreboard"""
        # Control buttons container
        controls_container = tk.Frame(
            parent,
            bg=self.colors['bg_primary']
        )
        controls_container.place(x=0, y=y, width=170, height=50)
        
        # Buttons frame for side-by-side layout
        buttons_frame = tk.Frame(
            controls_container,
            bg=self.colors['bg_primary']
        )
        buttons_frame.pack(fill='both', expand=True, pady=5)
        
        # New Game button (smaller, left side)
        new_game_btn = tk.Button(
            buttons_frame,
            text="New Game",
            font=('Segoe UI', 8, 'bold'),
            bg=self.colors['success'],
            fg=self.colors['bg_primary'],
            relief='flat',
            bd=0,
            padx=8,
            pady=4,
            cursor='hand2',
            activebackground=self.lighten_color(self.colors['success']),
            activeforeground=self.colors['bg_primary'],
            command=self.start_new_game
        )
        new_game_btn.pack(side='left', fill='x', expand=True, padx=(0, 2))
        
        # Restart button (smaller, right side)
        restart_btn = tk.Button(
            buttons_frame,
            text="Restart",
            font=('Segoe UI', 8, 'bold'),
            bg=self.colors['warning'],
            fg=self.colors['bg_primary'],
            relief='flat',
            bd=0,
            padx=8,
            pady=4,
            cursor='hand2',
            activebackground=self.lighten_color(self.colors['warning']),
            activeforeground=self.colors['bg_primary'],
            command=self.reset_game
        )
        restart_btn.pack(side='right', fill='x', expand=True, padx=(2, 0))
        
        # Add hover effects
        new_game_btn.bind('<Enter>', lambda e: self.on_button_hover(new_game_btn, self.colors['success'], True))
        new_game_btn.bind('<Leave>', lambda e: self.on_button_hover(new_game_btn, self.colors['success'], False))
        restart_btn.bind('<Enter>', lambda e: self.on_button_hover(restart_btn, self.colors['warning'], True))
        restart_btn.bind('<Leave>', lambda e: self.on_button_hover(restart_btn, self.colors['warning'], False))
            
    def create_game_board(self, parent):
        """Create the modern game board"""
        board_container = tk.Frame(
            parent,
            bg=self.colors['bg_primary']
        )
        board_container.pack(side='right', fill='both', expand=True)
        
        # Board frame with modern styling
        self.board_frame = tk.Frame(
            board_container,
            bg=self.colors['bg_card'],
            relief='flat',
            bd=2,
            highlightbackground=self.colors['border'],
            highlightthickness=1
        )
        self.board_frame.pack(expand=True, padx=20, pady=20)
        
        # Create 3x3 grid of modern buttons
        self.cells = []
        cell_size = 80
        
        for i in range(9):
            row = i // 3
            col = i % 3
            
            # Create modern button with Material Design styling
            cell = tk.Button(
                self.board_frame,
                text='',
                width=6,
                height=3,
                font=('Segoe UI', 20, 'bold'),
                bg=self.colors['surface'],
                fg=self.colors['text_primary'],
                relief='flat',
                bd=0,
                cursor='hand2',
                activebackground=self.colors['hover'],
                activeforeground=self.colors['text_primary'],
                command=lambda x=i: self.handle_cell_click(x)
            )
            
            cell.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
            
            # Configure grid weights for responsive design
            self.board_frame.grid_rowconfigure(row, weight=1)
            self.board_frame.grid_columnconfigure(col, weight=1)
            
            # Add modern hover effects
            cell.bind('<Enter>', lambda e, btn=cell: self.on_cell_hover(btn, True))
            cell.bind('<Leave>', lambda e, btn=cell: self.on_cell_hover(btn, False))
            
            self.cells.append(cell)
            
    def create_bottom_controls(self):
        """Create modern control buttons - only Exit button"""
        controls_frame = tk.Frame(
            self.main_frame,
            bg=self.colors['bg_secondary'],
            height=50
        )
        controls_frame.pack(fill='x', side='bottom')
        controls_frame.pack_propagate(False)
        
        # Button container
        button_container = tk.Frame(controls_frame, bg=self.colors['bg_secondary'])
        button_container.pack(expand=True)
        
        # Only Exit button in bottom controls
        exit_btn = tk.Button(
            button_container,
            text="Exit",
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['error'],
            fg=self.colors['bg_primary'],
            relief='flat',
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2',
            activebackground=self.lighten_color(self.colors['error']),
            activeforeground=self.colors['bg_primary'],
            command=self.exit_game
        )
        exit_btn.pack(pady=10)
        
        # Add modern button hover effects
        exit_btn.bind('<Enter>', lambda e: self.on_button_hover(exit_btn, self.colors['error'], True))
        exit_btn.bind('<Leave>', lambda e: self.on_button_hover(exit_btn, self.colors['error'], False))
            
    def lighten_color(self, color):
        """Lighten a hex color for hover effects"""
        # Simple color lightening (increase brightness)
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        lightened = tuple(min(255, int(c * 1.2)) for c in rgb)
        return f"#{lightened[0]:02x}{lightened[1]:02x}{lightened[2]:02x}"
        
    def bind_events(self):
        """Bind keyboard events"""
        self.window.bind('<Escape>', lambda e: self.exit_game())
        self.window.bind('<F5>', lambda e: self.reset_game())
        self.window.bind('<F2>', lambda e: self.start_new_game())
        
    def on_cell_hover(self, button, entering):
        """Handle modern cell hover effects"""
        cell_index = self.cells.index(button)
        if self.board[cell_index] == '' and not self.game_over:
            if entering:
                button.configure(
                    bg=self.colors['hover'],
                    relief='raised'
                )
                # Show preview of current player's symbol only on hover
                preview_color = self.colors['primary'] if self.current_player == 'X' else self.colors['secondary']
                preview_symbol = '✗' if self.current_player == 'X' else '◯'
                button.configure(text=preview_symbol, fg=preview_color)
            else:
                button.configure(
                    bg=self.colors['surface'],
                    relief='flat'
                )
                # Clear preview when not hovering and cell is empty
                button.configure(text="", fg=self.colors['text_primary'])
                    
    def on_button_hover(self, button, original_color, entering):
        """Handle modern button hover effects"""
        if entering:
            button.configure(bg=self.lighten_color(original_color))
        else:
            button.configure(bg=original_color)
            
    def handle_cell_click(self, index: int):
        """Handle cell click with modern animations"""
        if self.board[index] == '' and not self.game_over and self.current_player == 'X':
            self.animate_cell_click(index)
            self.make_move(index)
            
            if not self.game_over:
                self.window.after(500, self.make_computer_move)
                
    def animate_cell_click(self, index: int):
        """Create modern click animation"""
        cell = self.cells[index]
        
        # Modern pulse effect
        original_bg = cell['bg']
        pulse_color = self.colors['primary'] if self.current_player == 'X' else self.colors['secondary']
        
        cell.configure(bg=pulse_color)
        self.window.after(100, lambda: cell.configure(bg=original_bg))
        
    def make_move(self, index: int):
        """Make a move and update the board"""
        self.board[index] = self.current_player
        self.update_cell(index)
        
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.scores[winner if winner != 'tie' else 'tie'] += 1
            self.update_score_display()
            self.animate_winner(winner)
            self.window.after(1000, lambda: self.show_winner_message(winner))
            return
            
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.update_current_player_display()
        
    def update_cell(self, index: int):
        """Update cell with modern styling and futuristic symbols"""
        cell = self.cells[index]
        player = self.board[index]
        
        if player == 'X':
            cell.configure(
                text='✗',
                fg=self.colors['primary'],
                font=('Segoe UI', 24, 'bold'),
                bg=self.colors['surface']
            )
        elif player == 'O':
            cell.configure(
                text='◯',
                fg=self.colors['secondary'],
                font=('Segoe UI', 24, 'bold'),
                bg=self.colors['surface']
            )
            
        # Modern scale animation
        self.scale_cell(cell)
        
    def scale_cell(self, cell):
        """Create modern scale animation"""
        original_font = cell['font']
        
        def animate_scale(step=0):
            if step < 4:
                size = 24 + (step % 2) * 2
                cell.configure(font=('Segoe UI', size, 'bold'))
                self.window.after(50, lambda: animate_scale(step + 1))
            else:
                cell.configure(font=original_font)
                
        animate_scale()
        
    def update_current_player_display(self):
        """Update current player with modern colors and futuristic symbols"""
        color = self.colors['primary'] if self.current_player == 'X' else self.colors['secondary']
        symbol = '✗' if self.current_player == 'X' else '◯'
        self.current_player_label.configure(
            text=symbol,
            fg=color
        )
        
    def make_computer_move(self):
        """Make computer move with modern thinking animation"""
        if self.game_over:
            return
            
        # Show modern thinking animation
        self.animate_computer_thinking()
        
        difficulty = self.difficulty.get().lower()
        
        if difficulty == 'easy':
            move = self.make_random_move()
        elif difficulty == 'medium':
            move = self.make_best_move() if random.random() < 0.7 else self.make_random_move()
        else:  # hard
            move = self.make_best_move()
            
        if move is not None:
            self.window.after(800, lambda: self.make_move(move))
            
    def animate_computer_thinking(self):
        """Show modern thinking animation"""
        thinking_symbols = ["●", "●●", "●●●"]
        
        def cycle_thinking(step=0):
            if step < len(thinking_symbols) * 2:
                symbol = thinking_symbols[step % len(thinking_symbols)]
                self.current_player_label.configure(text=symbol, fg=self.colors['text_muted'])
                self.window.after(200, lambda: cycle_thinking(step + 1))
            else:
                self.current_player_label.configure(text="◯", fg=self.colors['secondary'])
                
        cycle_thinking()
        
    def make_random_move(self) -> Optional[int]:
        """Make a random move"""
        empty_cells = [i for i, cell in enumerate(self.board) if cell == '']
        return random.choice(empty_cells) if empty_cells else None
        
    def make_best_move(self) -> Optional[int]:
        """Make the best possible move using minimax"""
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
        """Minimax algorithm for AI"""
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
        """Check for winner"""
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
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
        
    def animate_winner(self, winner: str):
        """Create modern winner animation"""
        if winner == 'tie':
            # Modern tie animation - pulse all cells
            for cell in self.cells:
                self.pulse_cell_modern(cell, self.colors['warning'])
            return
            
        # Find winning pattern and highlight
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        for pattern in win_patterns:
            a, b, c = pattern
            if (self.board[a] == winner and 
                self.board[b] == winner and 
                self.board[c] == winner):
                color = self.colors['primary'] if winner == 'X' else self.colors['secondary']
                for index in pattern:
                    self.pulse_cell_modern(self.cells[index], color)
                break
                
    def pulse_cell_modern(self, cell, color):
        """Create modern pulse animation"""
        original_bg = cell['bg']
        
        def pulse(step=0):
            if step < 6:
                if step % 2 == 0:
                    cell.configure(bg=color, relief='raised')
                else:
                    cell.configure(bg=original_bg, relief='flat')
                self.window.after(150, lambda: pulse(step + 1))
            else:
                cell.configure(bg=original_bg, relief='flat')
                
        pulse()
        
    def show_winner_message(self, winner: str):
        """Show modern winner message"""
        if winner == 'tie':
            title = "It's a Tie!"
            message = "Great game! Nobody wins this round."
        else:
            player_name = "You" if winner == 'X' else "Computer"
            title = f"{player_name} Wins!"
            message = f"Congratulations! {player_name} ({winner}) is the winner!"
            
        # Create modern message dialog
        self.show_modern_message(title, message)
        
    def show_modern_message(self, title, message):
        """Show modern styled message dialog"""
        dialog = tk.Toplevel(self.window)
        dialog.title(title)
        dialog.geometry("300x150")
        dialog.configure(bg=self.colors['bg_card'])
        dialog.resizable(False, False)
        
        # Center the dialog
        dialog.transient(self.window)
        dialog.grab_set()
        
        # Position dialog
        x = self.window.winfo_x() + (self.window.winfo_width() // 2) - 150
        y = self.window.winfo_y() + (self.window.winfo_height() // 2) - 75
        dialog.geometry(f"300x150+{x}+{y}")
        
        # Title
        title_label = tk.Label(
            dialog,
            text=title,
            font=('Segoe UI', 14, 'bold'),
            fg=self.colors['text_primary'],
            bg=self.colors['bg_card']
        )
        title_label.pack(pady=(20, 10))
        
        # Message
        message_label = tk.Label(
            dialog,
            text=message,
            font=('Segoe UI', 10),
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_card'],
            justify='center'
        )
        message_label.pack(pady=(0, 20))
        
        # OK button
        ok_button = tk.Button(
            dialog,
            text="OK",
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['primary'],
            fg=self.colors['bg_primary'],
            relief='flat',
            bd=0,
            padx=30,
            pady=8,
            cursor='hand2',
            command=dialog.destroy
        )
        ok_button.pack()
        
    def update_score_display(self):
        """Update score display with modern animation"""
        for player, score in self.scores.items():
            label = self.score_labels[player]
            label.configure(text=str(score))
            
            # Modern pulse effect for updated score
            self.pulse_score_modern(label)
            
    def pulse_score_modern(self, label):
        """Create modern pulse effect for score update"""
        original_font = label['font']
        
        def pulse(step=0):
            if step < 4:
                size = 10 + (step % 2) * 2
                label.configure(font=('Segoe UI', size, 'bold'))
                self.window.after(100, lambda: pulse(step + 1))
            else:
                label.configure(font=original_font)
                
        pulse()
        
    def reset_game(self):
        """Reset current game with modern transition"""
        # Modern flash effect
        self.window.configure(bg=self.colors['primary'])
        self.window.after(50, lambda: self.window.configure(bg=self.colors['bg_primary']))
        
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_over = False
        
        for cell in self.cells:
            cell.configure(
                text="",
                bg=self.colors['surface'],
                fg=self.colors['text_primary'],
                relief='flat'
            )
            
        self.update_current_player_display()
        
    def start_new_game(self):
        """Start completely new game"""
        self.scores = {'X': 0, 'O': 0, 'tie': 0}
        self.update_score_display()
        self.reset_game()
        
    def exit_game(self):
        """Exit the game"""
        self.window.quit()
        
    def run(self):
        """Start the game"""
        self.window.mainloop()

def main():
    """Main function to run the modern game"""
    try:
        game = ModernTicTacToe()
        game.run()
    except Exception as e:
        print(f"Error starting game: {e}")
        try:
            messagebox.showerror("Error", f"Failed to start game: {e}")
        except:
            print("Could not show error dialog")

if __name__ == "__main__":
    main()

