# Connect4 Tournament Game

## Overview

Welcome to the **Connect4 Tournament**! This game is a competitive, multiplayer version of the classic Connect 4 game, designed with a fun twist: players are cadets who compete not only to win the game but also to secure their spot in a tournament and reveal their military branch assignments. The game is powered by a random guessing challenge to determine the order of players, and each round provides a unique, interactive experience.

---

## Features

- **Interactive Guessing Challenge:** Players begin by guessing a random number to determine their position in the queue.
- **Dynamic Queue System:** Players are queued based on the accuracy of their guesses, ensuring a fair match-up.
- **Classic Connect 4 Gameplay:** The traditional Connect 4 game where players aim to align four discs in a row, either horizontally, vertically, or diagonally.
- **Branch Reveal:** The winner of each round has their military branch revealed, adding a layer of competition and excitement to the game.
- **Requeuing System:** The losing player is automatically placed at the end of the queue for the next round, maintaining a continuous flow of matches.
- **Tie Handling:** If the game board is full without a winner, a tie is declared, and the board is reset for a new round.
- **User Interface:** Built with **Tkinter**, the game features an intuitive, easy-to-use interface with clear instructions and smooth transitions between stages.

---

## Requirements

To run this game, you need the following:

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/connect4-tournament.git
   ```

2. **Navigate to the Project Folder:**

   ```bash
   cd connect4-tournament
   ```

3. **Run the Game:**

   Simply run the Python script to start the game:

   ```bash
   python Connect4_Final.py
   ```

---

## How to Play

1. When the game starts, each player must enter a number between 1 and 50.
2. The players are queued based on how close their guesses are to the randomly generated number.
3. Players are paired up to play against each other in a **Connect 4** match.
4. The objective of the game is to align four discs of your color (red or yellow) in a row.
5. The winner of the match has their military branch revealed and continues in the tournament.
6. The losing player is requeued at the end for the next round.
7. The game continues until all cadets have participated in at least one match.![Connect4GUI](https://github.com/user-attachments/assets/8b91db8d-6a5d-4f32-b5a7-bd5030aa2af1)
![QueueScreen](https://github.com/user-attachments/assets/bc6c025f-bdb1-46ad-b843-f9c5d4a5d7ee)
![MainScreenGuess](https://github.com/user-attachments/assets/90512d48-e29b-4be3-9144-f8630fb43a5f)


---

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you'd like to add!

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgements

- **Tkinter:** For the user interface.
- **Python:** The programming language used to create this game.
