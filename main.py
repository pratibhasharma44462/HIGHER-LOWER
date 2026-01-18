from art import logo, vs
from game_data import data
import random

def account(data):
    data_name = data["name"]
    data_descr = data["description"]
    data_country = data["country"]
    return(f"{data_name}, a{data_descr} from {data_country}.")

def check_Answer(user_guess, a_follower, b_follower):
    if a_follower>b_follower:
        return user_guess == "A"
    else:
        return user_guess == "B"

print(logo)
score = 0
game_Should_continue = True
reandom_B = random.choice(data)


while game_Should_continue:
    random_A= reandom_B
    reandom_B = random.choice(data)


    if random_A == reandom_B:
        reandom_B = random.choice(data)

    print(f"Compare A: {account(random_A)}")
    print(vs)
    print(f"Compare B: {account(reandom_B)}")


    choice = input(f'who has more follower?? Type "A" or "B": ')    
    print("\n" * 20)
    print(logo)

    # - Get follower count of each account
    a_follower_count = random_A["follower_count"]
    b_follower_count = reandom_B["follower_count"]

    # Check if user is correct.
    is_correct = check_Answer(choice, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_Should_continue = False

        
        