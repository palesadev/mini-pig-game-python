import random

class PigDiceGame:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.scores = [0, 0]
        self.current_player = 0
        self.round_score = 0

    def roll_dice(self):
        roll = random.randint(1, 6)
        print(f"{self.players[self.current_player]} rolled a {roll}")
        return roll

    def play_turn(self):
        while True:
            roll = self.roll_dice()
            if roll == 1:
                print(f"Oops! {self.players[self.current_player]} rolled a 1. No points this round.")
                self.round_score = 0
                break
            else:
                self.round_score += roll
                print(f"Current round score: {self.round_score}")
                if self.ask_to_continue():
                    continue
                else:
                    self.scores[self.current_player] += self.round_score
                    print(f"{self.players[self.current_player]} ends turn with {self.scores[self.current_player]} points.")
                    self.round_score = 0
                    break

    def ask_to_continue(self):
        while True:
            choice = input(f"{self.players[self.current_player]}, do you want to roll again? (yes/no): ").strip().lower()
            if choice in ['yes', 'y']:
                return True
            elif choice in ['no', 'n']:
                return False
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

    def check_winner(self):
        for idx, score in enumerate(self.scores):
            if score >= 100:
                print(f"{self.players[idx]} wins with {score} points!")
                return True
        return False

    def play_game(self):
        print(f"Starting the game with players: {self.players[0]} and {self.players[1]}")
        while True:
            self.play_turn()
            if self.check_winner():
                break
        if self.ask_to_play_again():
            return True
        return False

    def ask_to_play_again(self):
        while True:
            choice = input("Do you want to play again? (yes/no): ").strip().lower()
            if choice in ['yes', 'y']:
                return True
            elif choice in ['no', 'n']:
                return False
            else:
                print("Invalid input. Please type 'yes' or 'no'.")


if __name__ == '__main__':
    print("Welcome to the Pig Dice Game!")
    player1 = input("Enter name for Player 1: ").strip()
    player2 = input("Enter name for Player 2: ").strip()
    game = PigDiceGame(player1, player2)
    while game.play_game():
        game = PigDiceGame(player1, player2)
        
    print("Thank you for playing!")