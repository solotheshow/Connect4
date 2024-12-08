import tkinter as tk
from tkinter import messagebox
import random

# Define cadets and their branches
cadets = [
    "CDT Wingate", "CDT Jimenez", "CDT Payne P.", "CDT Payne Y.", "CDT Singleton",
    "CDT Lunsford", "CDT Nikema", "CDT Rodriguez", "CDT Reynolds", "CDT Lilly", "CDT Thompson"
]
branches = [
    "Military Intelligence", "Cyber", "Infantry", "Armor", "Aviation",
    "Signal", "Medical Services", "Transportation", "Finance", "Logistics",
    "Engineer", "Field Artillery", "Chemical", "Ordinance"
]

# Explicit branch assignment
cadet_branch_map = {
    "CDT Wingate": "Military Intelligence",
    "CDT Jimenez": "Military Intelligence",
    "CDT Payne P.": "Signal",
    "CDT Payne Y.": "Chemical",
    "CDT Singleton": "Ordinance",
    "CDT Lunsford": "Field Artillery",
    "CDT Nikema": "Transportation",
    "CDT Rodriguez": "Medical Services",
    "CDT Reynolds": "Infantry",
    "CDT Lilly": "Adjutant General",
    "CDT Thompson": "Cyber"
}


class Connect4Tournament:
    def __init__(self, master):
        self.master = master
        self.master.title("Branch Night Connect 4 Tournament")
        self.master.configure(bg="black")
        self.master.state("zoomed")  # Full-screen mode
        self.players = cadets[:]
        self.queue = []
        self.random_num = None
        self.guesses = {cadet: 0 for cadet in cadets}
        self.main_menu()

    def main_menu(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        main_frame = tk.Frame(self.master, bg="black", padx=20, pady=20)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(main_frame, text="Enter a number (1-50) for each cadet:", font=("impact", 24), bg="black", fg="white").pack(pady=20)

        grid_frame = tk.Frame(main_frame, bg="blue")
        grid_frame.pack()

        self.entries = {}
        rows, cols = 4, 3
        for i, cadet in enumerate(self.players):
            row, col = divmod(i, cols)
            cadet_frame = tk.Frame(grid_frame, bg="white", bd=2, relief="solid", padx=10, pady=10)
            cadet_frame.grid(row=row, column=col, padx=15, pady=15)
            tk.Label(cadet_frame, text=cadet, font=("arial", 18), bg="white").pack(pady=5)
            entry = tk.Entry(cadet_frame, font=("impact", 16), justify="center")
            entry.pack(pady=5)
            self.entries[cadet] = entry

        tk.Button(main_frame, text="Submit", font=("impact", 18), command=self.collect_guesses).pack(pady=20)

    def collect_guesses(self):
        valid = True
        for cadet, entry in self.entries.items():
            try:
                guess = int(entry.get())
                if 1 <= guess <= 50:
                    self.guesses[cadet] = guess
                else:
                    valid = False
                    break
            except ValueError:
                valid = False
                break

        if not valid:
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 50.")
        else:
            self.reveal_random_number_and_queue()

    def reveal_random_number_and_queue(self):
        self.random_num = random.randint(1, 50)
        self.queue = sorted(
            self.players, key=lambda c: abs(self.guesses[c] - self.random_num)
        )

        for widget in self.master.winfo_children():
            widget.destroy()

        main_frame = tk.Frame(self.master, bg="blue", padx=20, pady=20)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(main_frame, text=f"Random Number: {self.random_num}", font=("impact", 16), bg="blue", fg="white").pack(pady=10)
        tk.Label(main_frame, text="Queue Order:", font=("impact", 16), bg="blue", fg="white").pack(pady=10)
        for i, player in enumerate(self.queue, start=1):
            tk.Label(main_frame, text=f"{i}. {player} (Guess: {self.guesses[player]})", font=("impact", 14), bg="blue", fg="white").pack()

        tk.Button(main_frame, text="Let's Play!", font=("impact", 14), command=self.start_game).pack(pady=20)

    def start_game(self):
        if len(self.queue) > 1:
            self.current_player = self.queue.pop(0)
            self.opponent = self.queue.pop(0)
            messagebox.showinfo("Game Start", f"{self.current_player} vs {self.opponent}")
            self.game = Connect4Game(self.master, self.current_player, self.opponent, self.end_game)
        else:
            self.display_branches()

    def end_game(self, winner):
        loser = self.opponent if winner == self.current_player else self.current_player
        branch = cadet_branch_map[winner]

        # Requeue the loser at the end of the queue
        self.queue.append(loser)

        # Reveal the winner's branch
        self.reveal_branch(winner, branch, lambda: self.start_game() if len(self.queue) > 0 else self.display_branches())

    def reveal_branch(self, winner, branch, callback):
        # Create a Canvas overlay to simulate blur effect
        overlay = tk.Canvas(self.master, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="gray", highlightthickness=0)
        overlay.place(x=0, y=0)
        overlay.attributes = {"-alpha": 0.6}  # Semi-transparent effect

        # Create a centered frame for the congratulatory message
        frame = tk.Frame(overlay, bg="white", padx=20, pady=20, bd=2, relief="ridge")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Add congratulatory message
        tk.Label(
            frame,
            text=f"Congratulations {winner}!",
            font=("impact", 20),
            bg="white",
            fg="black",
            wraplength=400
        ).pack(pady=10)

        tk.Label(
            frame,
            text=f"You have branched into {branch}!",
            font=("impact", 16),
            bg="white",
            fg="black",
            wraplength=400
        ).pack(pady=10)

        # Add an OK button to remove the overlay and return to the game
        tk.Button(
            frame,
            text="Next Game",
            font=("impact", 14),
            command=lambda: [overlay.destroy(), callback()]
        ).pack(pady=10)

    def display_branches(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        # Create the main frame for the branch display
        main_frame = tk.Frame(self.master, bg="black", padx=20, pady=20)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(main_frame, text="Branch Assignments", font=("impact", 24), bg="black", fg="white").pack(pady=20)

        # Create the grid layout similar to the main menu
        grid_frame = tk.Frame(main_frame, bg="blue")
        grid_frame.pack()

        rows, cols = 4, 3  # Same layout as the guessing menu
        for i, (cadet, branch) in enumerate(cadet_branch_map.items()):
            row, col = divmod(i, cols)

            # Create a bordered frame for each cadet and their branch
            cadet_frame = tk.Frame(grid_frame, bg="white", bd=2, relief="solid", padx=10, pady=10)
            cadet_frame.grid(row=row, column=col, padx=15, pady=15)

            # Display the cadet's name
            tk.Label(cadet_frame, text=cadet, font=("impact", 18), bg="white").pack(pady=5)

            # Display the cadet's branch
            tk.Label(cadet_frame, text=branch, font=("Arial", 16), bg="white", fg="blue").pack(pady=5)

        # Add an Exit button to allow the user to quit the program
        tk.Button(main_frame, text="Congratulations, good luck!", font=("impact", 18), command=self.master.quit).pack(pady=20)

class Connect4Game:
    def __init__(self, master, player1, player2, end_game_callback):
        self.master = master
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.opponent = player2
        self.grid = [["" for _ in range(7)] for _ in range(6)]
        self.end_game_callback = end_game_callback
        self.draw_board()

    def draw_board(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        main_frame = tk.Frame(self.master, bg="blue")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(main_frame, text=self.player1, font=("impact", 18, "bold" if self.current_player == self.player1 else "normal"), fg="red" if self.current_player == self.player1 else "white", bg="blue").grid(row=0, column=0, padx=20, sticky="w")
        tk.Label(main_frame, text=self.player2, font=("impact", 18, "bold" if self.current_player == self.player2 else "normal"), fg="red" if self.current_player == self.player2 else "white", bg="blue").grid(row=0, column=8, padx=20, sticky="e")

        for row in range(6):
            for col in range(7):
                frame = tk.Frame(main_frame, width=100, height=100, bg="blue")
                frame.grid(row=row + 1, column=col + 1)
                canvas = tk.Canvas(frame, width=100, height=100, bg="blue", highlightthickness=0)
                color = "white"
                if self.grid[row][col] == self.player1:
                    color = "red"
                elif self.grid[row][col] == self.player2:
                    color = "yellow"
                canvas.create_oval(10, 10, 90, 90, fill=color)
                canvas.grid()

        for col in range(7):
            tk.Button(main_frame, text=str(col + 1), font=("impact", 14), command=lambda c=col: self.drop_disc(c)).grid(row=7, column=col + 1)

    def drop_disc(self, column):
        for row in reversed(range(6)):
            if not self.grid[row][column]:
                self.grid[row][column] = self.current_player
                self.draw_board()
                if self.check_victory(row, column):
                    self.end_game_callback(self.current_player)
                elif self.check_tie():
                    self.handle_tie()
                else:
                    self.switch_player()
                return

    def switch_player(self):
        self.current_player, self.opponent = self.opponent, self.current_player
        self.draw_board()

    def check_victory(self, row, col):
        return any(
            self.count_consecutive(row, col, dr, dc) >= 4
            for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]
        )

    def check_tie(self):
        """Check if the board is full and no one has won."""
        return all(cell != "" for row in self.grid for cell in row)

    def handle_tie(self):
        """Handle the tie scenario."""
        messagebox.showinfo("Tie Game", "The game is a tie! Restarting the board with the same players.")
        self.grid = [["" for _ in range(7)] for _ in range(6)]  # Reset the board
        self.draw_board()  # Redraw the board for the same players

    def count_consecutive(self, row, col, dr, dc):
        count = 0
        player = self.grid[row][col]
        r, c = row, col

        while 0 <= r < 6 and 0 <= c < 7 and self.grid[r][c] == player:
            count += 1
            r += dr
            c += dc

        r, c = row - dr, col - dc
        while 0 <= r < 6 and 0 <= c < 7 and self.grid[r][c] == player:
            count += 1
            r -= dr
            c -= dc

        return count



if __name__ == "__main__":
    root = tk.Tk()
    tournament = Connect4Tournament(root)
    root.mainloop()
