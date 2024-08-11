# outputs:
# quiz as dictionary:   entry 'state':'capital'

def run():
  # open txt file
  quiz_dict = open('states_capitals_dict', 'r')

  # initiate and step into dict assignment
  quiz = {}
  read = True
  while read:
    # assign state from txt file
    state = quiz_dict.readline().rstrip()

    # assign capital from txt file
    capital = quiz_dict.readline().rstrip()
    quiz_dict.readline()

    # stop reading at end of file
    if not state or not capital:
      read = False

    # assign quiz dict entry
    else:
      quiz[state] = capital

  # close file
  quiz_dict.close()
  return quiz
