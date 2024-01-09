initial_money=1000
while initial_money>0:
    print("<<<<<<GAME STARTS!>>>>>>>")
    def get_user_input():
        user_input = input("Big or Small: ")
        return user_input.strip().lower()

    user_input = get_user_input()
    answer_list = ["Big", "Small","big","small"]

    while True:
        if user_input not in answer_list:
         print("Invalid input, please input again!")
         user_input = get_user_input()
        else:
         break

    def get_bet_money():
       bet_money=input(f"You have {initial_money}. How much you wanna bet?")
       return bet_money
    bet_money=get_bet_money()

    while True:
        if float(bet_money)>float(initial_money):
          print(f"You don't have much money, please choose number under {initial_money}")
          bet_money=get_bet_money()
        else:
          break


    print("<<<<<ROLE THE DICE!>>>>>>")

    #random dice#
    import random

    point1 = random.randrange(1,6)
    point2 = random.randrange(1,6)
    point3 = random.randrange(1,6)

    total_p=int(point1)+int(point2)+int(point3)

    if total_p>9:
        answer_t="big" 
    else:
        answer_t="small"

    #compare answer with dice#
    if user_input==answer_t:
        initial_money=float(bet_money)+float(initial_money)
        print(f"The point are[{point1},{point2},{point3}] You win! You gained {bet_money}, you have {initial_money} now.")
    else:
        initial_money=float(initial_money)-float(bet_money)
        print(f"The point are[{point1},{point2},{point3}] You lose! You lost {bet_money}, you have {initial_money} now.")
print("GAME OVER")   
