import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player1_score = 0
    player2_score = 0
    target = 20
    current_player = 1

    print("🐷 Welcome to the Mini Pig Dice Game!")

    while player1_score < target and player2_score < target:

        print("\nPlayer", current_player, "turn")

        turn_score = 0

        while True:
            choice = input("Roll or Hold? (r/h): ")

            if choice == "r":
                dice = roll_dice()
                print("You rolled:", dice)

                if dice == 1:
                    print("You rolled a 1! No points this turn.")
                    turn_score = 0
                    break
                else:
                    turn_score += dice
                    print("Turn score:", turn_score)

            elif choice == "h":
                break

            else:
                print("Invalid input")

        if current_player == 1:
            player1_score += turn_score
            print("Player 1 total score:", player1_score)
            current_player = 2
        else:
            player2_score += turn_score
            print("Player 2 total score:", player2_score)
            current_player = 1

    if player1_score >= target:
        print("\n🎉 Player 1 wins!")
    else:
        print("\n🎉 Player 2 wins!")

play_game()