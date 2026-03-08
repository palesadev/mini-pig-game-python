# 🐷 Mini Pig Dice Game - Python

A fun, interactive two-player dice game built with Python. Roll the dice, accumulate points, and be the first to reach 100 points to win!

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Game Rules](#game-rules)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Example Gameplay](#example-gameplay)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)

## 📖 Overview

This project is a Mini Pig Dice Game built using Python. It allows two players to take turns rolling a dice to earn points. The game demonstrates fundamental Python concepts including:
- **Functions**: Modular code organization
- **Classes**: Object-oriented programming
- **Loops**: Game loop and input validation
- **Conditionals**: Game logic and win conditions
- **User Input/Output**: Interactive gameplay

## ✨ Features

- ✅ **Two-player gameplay**: Play against a friend
- ✅ **Custom player names**: Enter your own names
- ✅ **Score tracking**: Real-time score updates
- ✅ **Replay functionality**: Play multiple rounds without restarting
- ✅ **Input validation**: Robust error handling for user input
- ✅ **User-friendly interface**: Clear, interactive command-line experience
- ✅ **Class-based design**: Clean, maintainable code structure

## 🎮 Game Rules

1. **Objective**: Be the first player to reach **100 points**
2. **Taking a turn**: 
   - Roll the dice to accumulate points
   - If you roll a **1**: You lose all points from that round and your turn ends
   - If you roll 2-6: The points are added to your round score
3. **Holding**: 
   - After each roll (except rolling a 1), you can choose to hold
   - Holding saves your round score to your total score and ends your turn
   - Or choose to roll again to try to earn more points
4. **Winning**: The first player to reach 100 points wins the game

## 🚀 Installation

### Requirements
- Python 3.x installed on your system

### Steps
1. Clone the repository:
bash
git clone https://github.com/palesadev/mini-pig-game-python.git
cd mini-pig-game-python


2. Run the game:
bash
python pig_dice_game.py


## 🎯 How to Play

1. **Start the game**:
   bash
   python pig_dice_game.py


2. **Enter player names**: When prompted, enter the names for both players

3. **Take turns**:
   - The game will tell you whose turn it is
   - Roll the dice to earn points
   - After each roll, decide whether to:
     - **Roll again**: Type yes or y to continue rolling
     - **Hold**: Type no or n to save your points and end your turn

4. **Win condition**: First to 100 points wins!

5. **Play again**: After a game ends, choose whether to play another round

## 📝 Example Gameplay

bash
Welcome to the Pig Dice Game!
Enter name for Player 1: Alice
Enter name for Player 2: Bob
Starting the game with players: Alice and Bob

Alice rolled a 4
Current round score: 4
Alice, do you want to roll again? (yes/no): yes
Alice rolled a 5
Current round score: 9
Alice, do you want to roll again? (yes/no): no
Alice ends turn with 9 points.

Bob rolled a 6
Current round score: 6
Bob, do you want to roll again? (yes/no): yes
Bob rolled a 1
Oops! Bob rolled a 1. No points this round.


## 🛠️ Technologies Used

- **Python 3.x**: Core language
- **Random module**: For dice rolling
- **Object-Oriented Programming**: Class-based game design

## 📁 Project Structure

mini-pig-game-python/
├── pig_dice_game.py      # Main game file (improved version)
├── import random.py      # Original game file
├── README.md             # This file
└── .gitignore            # Git ignore file


## 🌟 Code Highlights

### Class-Based Design
python
class PigDiceGame:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.scores = [0, 0]
        # ... initialization


### Input Validation
python
def ask_to_continue(self):
    while True:
        choice = input(...).strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


## 🔄 Future Enhancements

Potential improvements for future versions:

- [ ] **Difficulty levels**: Add AI opponent with different strategies
- [ ] **Statistics tracking**: Save and display win/loss records
- [ ] **Leaderboard**: Track high scores across multiple games
- [ ] **GUI interface**: Create a graphical user interface using Tkinter or Pygame
- [ ] **Sound effects**: Add audio feedback for rolls and wins
- [ ] **Customizable rules**: Allow players to set winning score and number of players
- [ ] **Game history**: Display move history during gameplay
- [ ] **Betting system**: Allow players to bet points between rounds

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

**Palesa** - GitHub Profile: https://github.com/palesadev

---

**Enjoy the game! 🎲🐷**