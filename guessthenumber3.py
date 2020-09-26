"""No of guesses 10
Print no of guesses left
No of guesses he took to finish
Game Over"""

n = 21
number_of_guesses = 1
print("Number of guesses is limited to only 10 times: ")
while (number_of_guesses<=10):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<21:
        print("you enter less number please input greater number. \n")
    elif guess_number>21:
        print("you enter greater number please input smaller number. \n")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
        print(10-number_of-guesses,"no. of guesses left")
        number_of_guesses = number_of_guesses + 1
        if(number_of_guesses>10):
            print("GAME OVER")
