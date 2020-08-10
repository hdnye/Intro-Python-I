# UPER
# Client wants a r/p/s game
# Understand
    # What are the rules/wiinning conditions
     # - each player chooses rock, player or scissors
     # - rock beats scissors
     # - scissors beats paper
     # - paper beats rock
    # How many players:
     # - the user and the computer
    # For how long? 
     # - until user quits
    # How to keep score? 
     # - keep track of the user wins, ties, and losses
    # How many hand signs? 3
    # When does it being? 
     # - when we run pthyon rps.py
    # Who goes first? 
     # - both go at the same time
    # Should the computer try to learn & beat the player? 
     # - computer chooses randomly for now
    # How does the user indicate their choice? 
     # - get user input from command line
     # - we can input r = rock, p = paper, s = scissors
    # What is the final program look like? 
     # We play until user decides to quit: 
#      # B for begin
#     import random 
#     import time

#      user_input = input("Enter 'B'' to begin the game\n")
#      while True:
#         if user_input.lower() == 'b':
#             wins = 0
#             losses = 0
#             ties = 0
#             user_choice = input("Choose your pick: r for rock, p for paper, s for scissors")
#             if user_choice.lower() == 'q':
#                 # if Q: quit
#                 break
#         # Get user input from command line
#         # Computer makes its choice randomly
#         computer_choice = random.choice(['r', 'p', 's'])
#         # decide who wins
#         if user_choice.lower() == 'r':
#             if computer_choice == 'r':
#                 ties += 1
#                 winner = "Tie"
#            elif computer_choice == 'p':
#                 # Computer wins
#                 losses += 1
#                 winner = "Computer"
#             elife computer_choice == 's':
#                 # User wins   
#                wins += 1
#                winner = "User"
#         # Countdown before showing who won
#         for i in range(3, 0, -1):
#             time.sleep(1)
#             print(f"{i}...")
#         print(f"The winner is: {winner}")    
#         # Show how many wins and losses
#         if winner == "User":
#             print("You won!")
#         elif winner == "Computer":
#             print("You Lost :(")
#         else: 
#             print("It's a tie!")       
#         print(f"Wins: {wins}, Ties: {ties}, Losses: {losses}"")
#         # Repeat

# # Plan