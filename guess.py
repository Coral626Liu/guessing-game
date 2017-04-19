from random import randint

def judge_eq(num, num_guess):
    if num_guess > num:
         print "That's too high. Try again!"
    elif num_guess < num:
         print "That's too low. Try again!"
    elif num_guess == num:
         print"You got it! Thanks for playing!"
         return True
    else:
         print"Sorry, those two things can't be compared"
    
def main():
    print "Welcome to the number guessing game!"
    while True:
        game_switch = raw_input("press enter to start our game,or q to quit: ")
        if game_switch == 'q':
            break
        else:
            num = randint(1, 10)
            print "I have my number..."
            for i in range(5):
                num_guess =int( raw_input("What is your guess[1-10]?"))
                switch = False 
                switch = judge_eq(num, num_guess)
                if switch == True:
                    break

if __name__ == "__main__":
    main()

