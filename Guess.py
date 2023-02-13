import random
name = input('please enter your name:')
print("Difficulty Level:")
print('1, Easy')
print("2, Hard")
choice = input("Enter your choice:")
number_of_guesses = 0
if choice=='1':
    number = random.randint(1,10)
    print("I am going to guess a number between 1 to 10")
    while number_of_guesses <5:
        guess = int(input("Enter here"))
        number_of_guesses+=1
        if guess < number:
            print("your guess is low!")
        if guess > number:
            print("your guess is high")
        if guess == number:
            break
    if guess == number:
        print("You guess the correct number in",number_of_guesses,"Tries and the number was",number,".")
    else:
        print("you did not guess the number and the number was",number,'.')

elif choice == '2': 
        number1 = random.randint(1,50)
        print("I am going to guess a number between 1 to 50")
        while number_of_guesses <15:
            guess = int(input("Enter here"))
            number_of_guesses+=1 
            if guess < number1:
                print("your guess is low!")
            if guess > number1:
                print("your guess is high")
            if guess == number1:
                break
        if guess == number1:
            print("You guess the correct number in",number_of_guesses,"Tries and the number was",number1,".")
        else:
            print("you did not guess the number and the number was",number1,'.')