import random

word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
secret_word = random.choice(word_list)   
list_letters = []

def word_selected_dashed():
    word_selected_dashed = []
    for i in range(len(secret_word)):
        word_selected_dashed.append('_')
    return ''.join(word_selected_dashed)

word_selected_dashed = word_selected_dashed()
print(word_selected_dashed)

num_lives = 5
gussed_word = list(word_selected_dashed)

while num_lives > 0:
    if ''.join(gussed_word) == secret_word:
        print("Great, you have guessed the correct word!")
        break

    print('You have got '+ str(num_lives)+ ' number of lives! ')
    user_guseed_letter = input('Guess a letter: \n')
    
    if len(user_guseed_letter) > 1:
        print("Enter only one letter!")
        
    elif user_guseed_letter not in list_letters:
        list_letters.append(user_guseed_letter)
    else:
        print(f"{user_guseed_letter} was already used!")

    if user_guseed_letter in secret_word:
        print('Correct!')
        for i in range(len(secret_word)):
            if list(secret_word)[i] == user_guseed_letter:
                gussed_word[i] = user_guseed_letter
        print(''.join(gussed_word))

    elif user_guseed_letter not in secret_word:
        print('wrong!')
        num_lives -= 1
        
if num_lives == 0 :
    print('You have ran out of trials!')