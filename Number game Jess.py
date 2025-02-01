#Game time
def number_guess():
    print('Hey Champ! Welcome to the number guess game. Choose a number between 1 and 10 only.')
    count = 0
    while count <= 3:
        print(f'You have {count} attempts')
        count = count +1
        correct_guess = 5
        while True:
            user_guess = int(input('Please write your guess here:'))
            if user_guess == correct_guess:
                print(f'Congratulations! You guessed the number in {count} attempts')
                break
            elif user_guess >= 5:
                print('Too high! Try again.')
            else:
                print('Too low! Try again.')
            if count >= 6:
                print('Sorry you have reached the maximum munber of attempts')
                
        play_again = input('Do you want to play again? (yes/no): '.strip().lower())
        if play_again == 'yes':
            print({user_guess})
        else:
            print('Game over.')