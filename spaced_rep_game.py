# suloginu
import datetime
inDate = datetime.datetime.now()
log = open('log.txt', 'a')
log.write(inDate)
log.close()

class GameDay:
  def __init__(self, startdate, datenow):
    self.startdate = startdate
    self.datenow = datenow
    
  def get_day(self):
    Scheduled = int(self.dateNow.strftime('%j'))-int(self.startDate.strftime('%j'))+1
    box_seq = DateScheduling[Scheduled-1]
    return box_seq

# datos kintamasis
dates = open ( 'log.txt',"r" )
DateList = dates.readlines()
dates.close()
startdate = DateList[0]
datenow = DateList[-1]

x = GameDay(startdate, datenow)

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
  def __init__(self, pol, ltu, correct = True):
    self.lenkiskai = pol
    self.lietuviskai = ltu
    self.correct = correct
    
  def ask_in_polish(self):
    print('Whats Lithuanian for '+ self.lenkiskai+ '?')
    answer = input()
    if answer.lower() == self.lietuviskai:
      self.correct == True
    else:
      self.correct == False
  
class Box:
  def __init__(self):
  
  def get_first_box(self):
    
  def get_second_box(self):
    
  def get_third_box(self):  


if x.get_day()%3 == 0 and x.get_day()%2 == 0:
  
elif x.get_day()%2 == 0

elif x.get_day()%3 == 0:
  
    # sudedu 1, 2 ir 3 i zodynus
    
    # reikia dar duoti user inputa
    # apkeist dezes
    # irasyti dezes i failus atgal
    
   
