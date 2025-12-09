"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays against a computer that randomly selects its move,
with the game showing who won each round.
Add a score counter that tracks player and computer wins,
and allow the game to continue until the player types "quit".
"""

import random
import sys

VALID_CHOICES = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return 'tie'
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')
    ):
        return 'player'
    else:
        return 'computer'

class Scoreboard:
    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0
        self.rounds = []
        self.max_rounds = 100  # Limit history to last 100 rounds
    def record_round(self, player_choice, computer_choice, outcome):
        """
        Records the outcome of a round, updates win/tie counters, and stores round details.

        Args:
            player_choice (str): The player's move ('rock', 'paper', or 'scissors').
            computer_choice (str): The computer's move ('rock', 'paper', or 'scissors').
            outcome (str): The result of the round ('player', 'computer', or 'tie').
        """
        if outcome == 'player':
            self.player_wins += 1
        elif outcome == 'computer':
            self.computer_wins += 1
        elif outcome == 'tie':
            self.ties += 1
        else:
            raise ValueError(f"Invalid outcome value: {outcome}")
        # Append round details
        self.rounds.append({
            'player_choice': player_choice,
            'computer_choice': computer_choice,
            'outcome': outcome
        })
        if len(self.rounds) > self.max_rounds:
            self.rounds.pop(0)  # Remove oldest round if over limit
    
    def get_score_text(self):
        return "Score - You: {player}, Computer: {computer}, Ties: {ties}".format(
            player=self.player_wins, computer=self.computer_wins, ties=self.ties
        )
    
    def get_detailed_stats(self):
        total_rounds = len(self.rounds)
        if total_rounds == 0:
            return "No rounds played yet."
        stats = f"=== SCOREBOARD ===\n"
        stats += f"Player Wins: {self.player_wins}\n"
        stats += f"Computer Wins: {self.computer_wins}\n"
        stats += f"Ties: {self.ties}\n"
        stats += f"Total Rounds: {total_rounds}\n"
        if self.player_wins > self.computer_wins:
            stats += f"Status: You're winning by {self.player_wins - self.computer_wins}!\n"
        elif self.computer_wins > self.player_wins:
            stats += f"Status: You're losing by {self.computer_wins - self.player_wins}.\n"
        else:
            stats += "Status: Tied!\n"
        return stats
    
    def reset(self):
        """
        Resets all win/tie counters and clears the round history.
        """
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0
        self.rounds = []
def main():
    """
    Runs the command-line Rock Paper Scissors game loop, handling user input and score tracking.
    """
    scoreboard = Scoreboard()
    while True:
        try:
            player_choice = input("Enter rock, paper, scissors or quit to exit: ").strip().lower()
            if player_choice in ('r', 'p', 's'):
                player_choice = {'r': 'rock', 'p': 'paper', 's': 'scissors'}[player_choice]
            elif player_choice in ('scissor', 'scissors'):
                player_choice = 'scissors'
            elif player_choice == 'scissor':
                player_choice = 'scissors'
        except (EOFError, KeyboardInterrupt):
            print("\nThanks for playing!")
            break

        if player_choice == 'quit':
            print(scoreboard.get_detailed_stats())
            print("Thanks for playing!")
            break

        # Normalize singular/plural forms for consistency
        if player_choice == 'scissor':
            player_choice = 'scissors'

        if player_choice not in VALID_CHOICES:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        scoreboard.record_round(player_choice, computer_choice, winner)
        
        if winner == 'player':
            print("You win this round!")
        elif winner == 'computer':
            print("Computer wins this round!")
        else:
            print("It's a tie!")

        print(scoreboard.get_score_text() + "\n")

def run_gui(window_geometry=None):
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import ttk

    class RPSApp(ttk.Frame):
        def __init__(self, master):
            super().__init__(master, padding=12)
            self.master = master
            self.master.title("Rock Paper Scissors")
            self.master.resizable(False, False)
            self.pack(fill='both', expand=True)

            style = ttk.Style()
            try:
                style.theme_use('clam')
            except Exception as e:
                print("Warning: Unable to set 'clam' theme for Tkinter. Using default theme.")
            style.configure('TButton', padding=6)

            self.scoreboard = Scoreboard()

            # Large, colored heading
            self.status_label = tk.Label(self, text="Choose rock, paper, or scissors", 
                                         anchor='center', font=("Arial", 16, "bold"), 
                                         fg="#2E86AB", bg=self.cget('bg'))
            self.status_label.grid(row=0, column=0, columnspan=3, pady=(0,15), sticky='ew')

            btn_rock = ttk.Button(self, text="Rock", command=lambda: self.play('rock'))
            btn_paper = ttk.Button(self, text="Paper", command=lambda: self.play('paper'))
            btn_scissors = ttk.Button(self, text="Scissors", command=lambda: self.play('scissors'))
            btn_rock.grid(row=1, column=0, padx=8, pady=10, sticky='ew')
            btn_paper.grid(row=1, column=1, padx=8, pady=10, sticky='ew')
            self._wraplength_after_id = None
            self.master.bind('<Configure>', self.debounced_update_wraplength)
    
            self.result_label = tk.Label(self, text="", wraplength=self.master.winfo_width(), anchor='center', 
                                         font=("Arial", 11, "bold"), fg="#F18F01", 
                                         bg=self.master.cget('bg'), justify='center')
            self.result_label.grid(row=2, column=0, columnspan=3, pady=(15,15), sticky='ew')
            self.master.bind('<Configure>', self.update_wraplength)

            # Styled scoreboard label
            self.score_label = tk.Label(self, text=self.scoreboard.get_score_text(), 
                                        anchor='center', font=("Arial", 13, "bold"), 
                                        fg="#A23B72", bg=self.cget('bg'))
            self.score_label.grid(row=3, column=0, columnspan=3, pady=(10,20), sticky='ew')

            stats_btn = ttk.Button(self, text="Stats", command=self.show_stats)
            stats_btn.grid(row=4, column=0, padx=6, pady=10, sticky='ew')

            reset_btn = ttk.Button(self, text="Reset Scores", command=self.reset_scores)
            reset_btn.grid(row=4, column=2, padx=6, pady=10, sticky='ew')

            # Set equal weight for columns
            for c in range(3):
                self.columnconfigure(c, weight=1)
    
            # Configure all 5 rows to expand equally for better layout
            for r in range(5):
                self.rowconfigure(r, weight=1)
    
            self.bind_all('<r>', lambda e: self.play('rock'))
            self.bind_all('<p>', lambda e: self.play('paper'))
            self.bind_all('<s>', lambda e: self.play('scissors'))
            self.bind_all('<q>', lambda e: self.master.destroy())
            self._wraplength_after_id = self.after(100, self.update_wraplength)

        def update_wraplength(self):
            # Set wraplength to 80% of window width for responsiveness
            new_wraplength = int(self.master.winfo_width() * 0.8)
            self.result_label.config(wraplength=new_wraplength)
            self._wraplength_after_id = None
            self.master.bind('<q>', lambda e: self.master.destroy())

        def update_wraplength(self, event=None):
            # Set wraplength to 80% of window width for responsiveness
            new_wraplength = int(self.master.winfo_width() * 0.8)
            self.result_label.config(wraplength=new_wraplength)


        def reset_scores(self):
            self.scoreboard.reset()
            self.score_label.config(text=self.scoreboard.get_score_text())
            self.result_label.config(text="Scores reset.")

        def show_stats(self):
            messagebox.showinfo("Game Statistics", self.scoreboard.get_detailed_stats())

        def play(self, player_choice):
            computer_choice = get_computer_choice()
            winner = determine_winner(player_choice, computer_choice)
            self.scoreboard.record_round(player_choice, computer_choice, winner)
            
            if winner == 'player':
                result_text = f"You win! {player_choice} beats {computer_choice}."
            elif winner == 'computer':
                result_text = f"Computer wins! {computer_choice} beats {player_choice}."
            else:
                result_text = f"It's a tie. Both chose {player_choice}."

            self.result_label.config(text=f"Computer chose: {computer_choice}\n{result_text}")
            self.score_label.config(text=self.scoreboard.get_score_text())

    root = tk.Tk()
    # Responsive window geometry
    if window_geometry:
        # Try to set requested geometry (e.g. "800x600")
        try:
            root.geometry(window_geometry)
        except Exception:
            print("Warning: Failed to apply requested geometry; continuing with default size.")
        # Try to center the window (may be ignored on some platforms)
        # NOTE FOR MAINTAINERS: The following line uses Tcl/Tk's 'PlaceWindow' command,
        # which may not work on all platforms or Tkinter versions. If centering fails,
        # the window will simply use the default placement.
        try:
            root.eval('tk::PlaceWindow . center')
        except Exception:
            pass

    app = RPSApp(master=root)
    app.mainloop()


if __name__ == "__main__":
    if '--gui' in sys.argv or '-g' in sys.argv:
        # Allow geometry to be passed as '--geometry=WIDTHxHEIGHT'
        geometry = None
        for arg in sys.argv:
            if arg.startswith('--geometry='):
                geometry = arg.split('=', 1)[1]
        run_gui(window_geometry=geometry)
    else:
        main()

