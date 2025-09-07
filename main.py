from random import randint
from sys import exit


def roll_dice():
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    score = die1 + die2
    return die1, die2, score


def announce_roll(player, die1, die2, score):
    print(f"{player} rolled a {die1} 🎲 and a {die2} 🎲 (Total: {score})")


def take_turn(player):
    while True:
        action = input(
            (
                f"{player}: (type `roll dice` to roll the dice "
                "or `quit` to exit): "
            )
        )
        if action == "quit":
            print("Game exited.")
            exit()
        elif action == "roll dice":
            die1, die2, score = roll_dice()
            announce_roll(player, die1, die2, score)
            return score
        else:
            print(f"Invalid input for {player}. Please try again.")


def determine_winners(scores):
    max_score = max(scores.values())
    winners = [
        player for player, score in scores.items()
        if score == max_score
    ]
    if len(winners) == 1:
        print(f"{winners[0]} wins with a score of {max_score}!")
    else:
        print(
            f"It's a tie between: {', '.join(winners)} "
            f"with a score of {max_score}!"
        )


players = ["Player 1", "Player 2", "Player 3"]
scores = {}
for player in players:
    scores[player] = take_turn(player)


determine_winners(scores)
