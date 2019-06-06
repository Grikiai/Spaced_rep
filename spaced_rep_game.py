# suloginu
import datetime
inDate = datetime.datetime.now()
log = open('log.txt', 'a')
log.write(inDate)
log.close()
answered_questions = 0
correctly_answered_questions = 0

class GameDay:
  def __init__(self, startdate, datenow, ):
    self.startdate = startdate
    self.datenow = datenow
    
  def get_day(self):
    Scheduled = int(self.dateNow.strftime('%j'))-int(self.startDate.strftime('%j'))+1
    box_seq = DateScheduling[Scheduled-1]
    return box_seq
  
  def progress(self):
    

dates = open ( 'log.txt',"r" )
DateList = dates.readlines()
dates.close()
startdate = DateList[0]
datenow = DateList[-1]



# sudedu 1, 2 ir 3 i zodynus
zodziai1 = open('level_1.txt', 'r')
Wordlist1 = zodziai1.readlines()
zodziai1.close()
first_box = {}
for i in Wordlist1:
  key = i.split('-')[0].strip()
  if key not in first_box:
    first_box[key] = i.split('-')[1].strip()
    
zodziai2 = open('level_2.txt', 'r')
Wordlist2 = zodziai2.readlines()
zodziai2.close()
second_box = {}
for i in Wordlist2:
  key = i.split('-')[0].strip()
  if key not in second_box:
    second_box[key] = i.split('-')[1].strip()
    
zodziai3 = open('level_3.txt', 'r')
Wordlist3 = zodziai3.readlines()
zodziai2.close()
third_box = {}
for i in Wordlist3:
  key = i.split('-')[0].strip()
  if key not in third_box:
    third_box[key] = i.split('-')[1].strip()  
      
      
class Card:
  Lives = 5
  def __init__(self, pol, ltu, correct = False):
    self.lenkiskai = pol
    self.lietuviskai = ltu
    self.correct = correct
    
  def ask_in_polish(self):
    print('Whats Lithuanian for '+ self.lenkiskai+ '?')
    answer = input()
    if answer.lower() == self.lietuviskai:
      self.correct == True
      answered_questions += 1
      correctly_answered_questions += 1
      print('Well done! You guessed correctly!!!!!!')
    else:
      self.correct == False
      print(':((((((((((((((((((( do you want to try again(y/n)? it will cost you one live thanks')
      self.do_you_want_to_die()
      
  def do_you_want_to_die(self):
      yes_no = input()
      try:
        if yes_no.lower().strip() == 'n':
          answered_questions += 1
          continue
        elif yes_no.lower().strip() == 'y' and Lives>0:
          Lives -=1
          self.ask_in_polish()
      except:
        if Lives<=0:
          print('sorry, you dont have lives anymore')
        elif yes_no.lower().strip() != 'n' or yes_no.lower().strip() != 'y':
          print('please write y/n only')
          self.do_you_want_to_die()
          
        
  
class Box:
  def __init__(self, card):
     self.card = card
      
  def get_first_box(self):
    for key in first_box.keys():
      y = first_box[key]
      z = Card(y, key)
      z.ask_in_polish()
      
  def get_second_box(self):
    for key in second_box.keys():
      y = second_box[key]
      z = Card(y, key)
      z.ask_in_polish()
      if self.correct == False:
        first_box[key] = y
        del(second_box[key])
      elif self.correct == True:
        third_box[key] = y
        del(second_box[key])
        
  def get_third_box(self):  
    for key in second_box.keys():
      y = third_box[key]
      z = Card(y, key)
      z.ask_in_polish()
      if self.correct == False:
        first_box[key] = y
        del(third_box[key])
      elif self.correct == True:
        continue
  
new_game = GameDay(startdate, datenow)

if new_game.get_day()%3 == 0 and new_game.get_day()%2 == 0:
  
elif new_game.get_day()%2 == 0

elif new_game.get_day()%3 == 0:
  
    # sudedu 1, 2 ir 3 i zodynus
    
    # reikia dar duoti user inputa
    # apkeist dezes
    # irasyti dezes i failus atgal
    # gal dar sekti progresa??
   
