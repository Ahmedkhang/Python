quest =(
    ('1. Which of the following is NOT a valid variable name in Python? : '),
    ('2. What will be the output of bool([]) in Python? : '),
    ('3. What does the is keyword do in Python? : '),
    ('4. Which of the following is NOT a Python data type? : '),
    )
options =(
    ('A. _my_var','B. 2nd_var','C. myVar','D my_var'),
    ('A. True','B. False','C. None','D. Error'),
    ('A. Checks if two variables have the same value','B. Checks if two variables refer to the same object in memory','C. Compares two variables using ==','D. Declares a variable'),
    ('A. list','B. tuple','C. dictionary','D. array')
    )
answer= ("B","B","B","D")
score = 0
guesses = []
quest_num = 0

for ques in quest:
    print('------------------------')
    print(ques)
    for option in options[quest_num]:
        print(option)

      
    guess = input('Enter (A,B,C,D) : ').upper()
    guesses.append(guess)
      
    if guess == answer[quest_num]:
        print('-------------------')
        print('Correct Answer!')
        print('-------------------')
        score += 1
    else:
        print('-------------------')
        print('Incorrect Answer!')  
        print('-------------------')
        print(f'\n{answer[quest_num]} is the Correct answer') 
    quest_num += 1

score = int(score/len(quest) * 100)
print('----Result----')
print(f'{score}%')
 