# inputs:
# quiz as dictionary:   entry 'state':'capital'

def run(quiz):
  import random
  
  # run quiz
  print('==== State Capital Quiz ====')
  print('Enter the capital of the following states:')
  
  # loop until all states are answered
  asked = 0
  correct = 0
  while len(quiz) > 0:
    print(f'\n============ Q{asked + 1}. =============')
    # randomly choose state, remove from quiz dict
    question, answer = random.choice(list(quiz.items()))
    del(quiz[question])
    asked += 1
  
    # ask user to guess capital
    guess = input(f'Capital of {question}?:  ')
    if guess == answer or guess == answer.lower():  # if correct
      print('\nO-O-O  Correct!  O-O-O\n')
      correct += 1
    else:  # if incorrect
      print('\nX-X-X  Incorrect!  X-X-X\n')
  
    # display correct count
    print(f'Correct: {correct}')

    # calculate incorrect count
    incorrect = asked - correct
    print(f'Incorrect: {incorrect}')
  
  # display final score
  print('\n===============================')
  print('\n\n--- Quiz Complete! ---')
  print(f'\nFinal Score: {correct} / {asked}')
  