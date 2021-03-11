import random
import shelve

#d = shelve.open('score.txt')
#score = d['score']  # the score is read from disk
#d.close()

user_score = 0
computer_score = 0

player_name = input("Enter Player Name:")

while True:
    user_action = input("Hi, Pick rock, paper or scissors: ").lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_score = user_score + 1
            computer_score = computer_score
        else:
            print("Paper covers rock! You lose.")
            user_score = user_score
            computer_score = computer_score + 1
            
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_score = user_score + 1
            computer_score = computer_score
            
        else:
            print("Scissors cuts paper! You lose.")
            user_score = user_score
            computer_score = computer_score + 1
            
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_score = user_score + 1
            computer_score = computer_score
            
        else:
            print("Rock smashes scissors! You lose.")
            user_score = user_score
            computer_score = computer_score + 1

    print("Scores:", player_name, ": ",  str(user_score), " ", "Computer:", str(computer_score))
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        if user_score == computer_score:
            print("Match Tied: GG", player_name)
            scores = (player_name, str(user_score), "vs. COM", str(computer_score))
            print("Final Scores: ",player_name, str(user_score), "vs. COM", str(computer_score))            
        elif user_score > computer_score:
            print("You Win The Match: Congratulations", player_name, "the Champion")
            scores = (player_name, str(user_score), "vs. COM", str(computer_score))
            print("Final Scores: ",player_name, str(user_score), "vs. COM", str(computer_score))            
        else:
            print("Computer Wins the Match: Good Luck Next Time", player_name)
            scores = (player_name, str(user_score), "vs. COM", str(computer_score))
            print("Final Scores: ",player_name, str(user_score), "vs. COM", str(computer_score))
            d = shelve.open('score.txt')  # here you will save the score variable   
            d['scores'] = scores            # thats all, now it is saved on disk.
            d.close()
        break