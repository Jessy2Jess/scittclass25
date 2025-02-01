  #Its a guess game!

def number_guess():
    print('Hey Champ! Welcome to the number guess game! Choose a number between 1and 10 only')
    while True:
          user_guess = int(input('Please write your guess here:'))
          correct_guess = 5
          if user_guess == correct_guess:
           print(f'Congratulations! You guessed the number.')
           break 
          elif user_guess >= 5:
           print('Too high! Try again.')
          else:
           print('Too low! Try again.')
          count = 0
          while count <= 4:
            print(f"You have used {count} attempts.")
          count = count +1
          if count >= 4:
           print('Sorry you have reached the maximum number of attempts for this game')
          else:
           print(f'You have {count} attempts left!')
          play_again = input('Do you want to play again? (yes/no): '.strip().lower())
    if play_again == 'yes':
      print({number_guess()})
    else:
      print('Game over.')


    
