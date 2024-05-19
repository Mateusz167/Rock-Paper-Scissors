# Importing the libraries and files I used when writing the programme
import symbols
import random
import sys

# Creation of a scoreboard
Score_board = {"Player points" : 0 , "Computer points" : 0}

def chosen_symbol_printing(symbol):
    """
       Prints the graphical representation of the chosen symbol.

       Parameters:
       symbol (str): A character representing the player's choice.
                     It should be one of the following:
                     - 'p' for paper
                     - 'r' for rock
                     - 's' for scissors

       Returns:
       None

       The function uses the input symbol to determine which graphical
       representation to print. It prints the corresponding symbol from
       the symbols module.
       """
    if symbol == 'p':
        print(symbols.paper)
    elif symbol == 'r':
        print(symbols.rock)
    elif symbol == 's':
        print(symbols.scissors)

def result_determination(player_choose, computer_choose, Score_board):
    """
     Determines the result of a Rock-Paper-Scissors game round and updates the score.

     Parameters:
     player_choose (str): The player's choice. It should be one of the following:
                          - 'p' for paper
                          - 'r' for rock
                          - 's' for scissors
     computer_choose (str): The computer's choice. It should be one of the following:
                            - 'p' for paper
                            - 'r' for rock
                            - 's' for scissors
     Score_board (dict): A dictionary tracking the scores. It should contain two keys:
                         - "Player points": An integer representing the player's score.
                         - "Computer points": An integer representing the computer's score.

     Returns:
     None

     The function compares the player's choice and the computer's choice to determine the
     result of the game round. It prints the result (draw, win, or loss) and updates the
     Score_board dictionary accordingly.
     """
    if player_choose == computer_choose:
        print("We have a draw")
    elif player_choose == 'p' and computer_choose == 'r' or player_choose == 'r' and computer_choose == 's' or player_choose == 's' and computer_choose == 'p':
        print("You won")
        Score_board["Player points"] += 1
    elif computer_choose == 'p' and player_choose == 'r' or computer_choose == 'r' and player_choose == 's' or computer_choose == 's' and player_choose == 'p':
        print("You losse")
        Score_board["Computer points"] += 1

def final_score_determination(Score_board):
    """
        Determines the final winner based on the scores in the Score_board.

        Parameters:
        Score_board (dict): A dictionary tracking the scores. It should contain two keys:
                            - "Player points": An integer representing the player's score.
                            - "Computer points": An integer representing the computer's score.

        Returns:
        None

        The function compares the total points of the player and the computer to determine
        the final winner. It prints 'You won' if the player has more points, 'You lose' if
        the computer has more points, and 'Draw' if the scores are equal.
        """
    if Score_board["Player points"] > Score_board["Computer points"]:
        print('You won')
    elif Score_board["Player points"] < Score_board["Computer points"]:
        print('You loss')
    else:
        print("Draw")

# Player welcome
print("Welcome to the game of Rock Paper Scissors. Have a good game and enjoy your victories.")

# Main program loop
while True:
    # Get player choice
    player_choose = input(
        "What do you want to choose? For paper choose 'p' for rock choose 'r' and for scissors choose 's'\n")
    #Validate player choice
    while player_choose != 'p' and player_choose != 'r' and player_choose != 's':
        player_choose = input("You have selected an unacceptable sign, please select again. For paper choose 'p' for rock choose 'r' and for scissors choose 's'\n")

    # Get computer choice
    computer_choose = random.choice(['p', 'r', 's'])

    # Print chosen symbols
    chosen_symbol_printing(player_choose)
    chosen_symbol_printing(computer_choose)

    # Determine and print result, update score
    result_determination(player_choose, computer_choose, Score_board)
    print(Score_board)

    # Prompt to continue or end game
    play_again = input("Do you want to continue? Type 'y' for yes and 'n' for no")
    if play_again == 'y':
        continue
    else:
        print("Thank you for your game")
        print(f"Your final score is: {Score_board}")
        final_score_determination(Score_board)
        sys.exit()

