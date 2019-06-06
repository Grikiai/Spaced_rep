x = 'level_1.txt'
y = 'level_2.txt'
z = 'level_3.txt'


for key in dictio:
  print('how is '+dictio[key]+' in lithuanian?')
  x = input()
  if x.lower()  == dictio[key]:
    print('you guessed correctly!!')
    dictio[key]='1'
  else:
    print('you guessed wrong :( the correct answer is '+ dictio[key])
    dictio[key]='0'

class Card:
  def __init__(self, dictio.keys(), dictio.values()):
    self.ques = dictio.keys()
    self.ans = dictio.values()

class Box:
  def __init__(self, nr, cards):
    self.nr = nr
    self.cards = cards

  def sort_cards(self):
    
