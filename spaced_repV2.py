
log = open('log.txt', 'r')
logs = log.readlines()
log.close()
date_now = len(logs)+1

log = open('log.txt', 'a')
logs = log.write(str(date_now)+' is the number of latest session\n')
log.close()

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
zodziai3.close()
third_box = {}
for i in Wordlist3:
  key = i.split('-')[0].strip()
  if key not in third_box:
    third_box[key] = i.split('-')[1].strip()

zodziai4 = open('level_4.txt', 'r')
Wordlist4 = zodziai4.readlines()
zodziai4.close()
fourth_box = {}
for i in Wordlist4:
  key = i.split('-')[0].strip()
  if key not in fourth_box:
    fourth_box[key] = i.split('-')[1].strip()

class GameDay:
  Lives = 5
  def __init__(self, date_now, answered_questions = 0, correctly_answered_questions = 0):
    self.date_now = date_now
    self.answered_questions = answered_questions
    self.correctly_answered_questions = correctly_answered_questions

  def get_progress(self):
      progress = (self.correctly_answered_questions/self.answered_questions)*100
      return progress

  def exit_or_no(self):
    yes_no3 = input('do you want to exit?y/n\n')
    if yes_no3.lower().strip() == 'y':
      exit
    elif yes_no2.lower().strip() == 'n':
      print('ok cool still bye')

  def overall_progress(self):
    progress = open ( 'progress.txt',"a")
    for line in progress.readlines():
      if '%' in line:
        continue
      else:
        one_record = 'on '+ date_now +' session your answered '+ str(new_game.get_progress()) +'% correctly'
        progress.write(one_record)
    progress.close()

  def progress_ask(self):
       print('do you want to see your progress?y/n\n')
       yes_no2 = input()
       if yes_no2.lower().strip() == 'n':
           new_game.exit_or_no()

       elif yes_no2.lower().strip() == 'y':
         output_progress = open('progress.txt', 'r')
         print(output_progress.read())
         output_progress.close()


class Card:
  def __init__(self, pol, ltu, correct = True):
    self.lenkiskai = pol
    self.lietuviskai = ltu
    self.correct = correct

  def ask_in_polish(self):
    print('Whats Lithuanian for '+ self.lenkiskai+ '?\n')
    answer = input()
    if answer.lower() == self.lietuviskai:
      self.correct == True
      new_game.answered_questions += 1
      new_game.correctly_answered_questions += 1
      print('Well done! You guessed correctly!!!!!!\n')
    else:
      self.correct == False
      print(':((((((((((((((((((( you answered incorrectly\n')


class Box:
  def __init__(self, card):
     self.card = card

  def get_first_box(self):
    for key in first_box.keys():
      y = first_box[key]
      z = Card(key, y)
      z.ask_in_polish()
      if z.correct == True:
        file_rewrite = open('level_2.txt', 'a')
        temp = [key, first_box[key]]
        file_rewrite.write(' - '.join([key, y])+'\n')
        file_rewrite.close()
        file_rewrite = open('level_1.txt', 'r+')
        lines = file_rewrite.readlines()
        file_rewrite.seek(0)
        for i in lines:
            if i.split('-')[0].strip() != key:
                file_rewrite.write(i)
        file_rewrite.close()

  def get_second_box(self):
    for key in second_box.keys():
      y = second_box[key]
      z = Card(key, y)
      z.ask_in_polish()
      temp = ' - '.join([key, second_box[key]])
      if z.correct == False:
        file_rewrite = open('level_1.txt', 'a')
        file_rewrite.write(temp+'\n')
        file_rewrite.close()
        file_rewrite = open('level_2.txt', 'r+')
        lines = file_rewrite.readlines()
        file_rewrite.seek(0)
        for i in lines:
            if i.split('-')[0].strip() != key:
                file_rewrite.write(i)
        file_rewrite.close()

      elif z.correct == True:
        file_rewrite = open('level_3.txt', 'a')
        file_rewrite.write(temp+'\n')
        file_rewrite.close()
        file_rewrite = open('level_2.txt', 'r+')
        lines = file_rewrite.readlines()
        file_rewrite.seek(0)
        for i in lines:
            if i.split('-')[0].strip() != key:
                file_rewrite.write(i)
        file_rewrite.close()

  def get_third_box(self):
    for key in third_box.keys():
      y = third_box[key]
      z = Card(key, y)
      z.ask_in_polish()
      temp = ' - '.join([key, third_box[key]])
      if z.correct == False:
        file_rewrite = open('level_1.txt', 'a')
        file_rewrite5.write(temp+'\n')
        file_rewrite5.close()
        file_rewrite = open('level_3.txt', 'r+')
        lines = file_rewrite.readlines()
        file_rewrite.seek(0)
        for i in lines:
            if i.split('-')[0].strip() != key:
                file_rewrite.write(i)
        file_rewrite.close()

      elif self.correct == True:
        file_rewrite3 = open('level_4.txt', 'a')
        file_rewrite3.write(' - '.join(temp)+'\n')
        file_rewrite3.close()
        file_rewrite = open('level_3.txt', 'r+')
        lines = file_rewrite.readlines()
        file_rewrite.seek(0)
        for i in lines:
            if i.split('-')[0].strip() != key:
                file_rewrite.write(i)
        file_rewrite.close()

    def get_fourth_box(self):
      for key in fourth_box.keys():
        y = fourth_box[key]
        z = Card(key, y)
        z.ask_in_polish()
        temp = ' - '.join([key, fourth_box[key]])
        if z.correct == False:
          file_rewrite = open('level_1.txt', 'a')
          file_rewrite.write(temp+'\n')
          file_rewrite.close()
          file_rewrite = open('level_4.txt', 'r+')
          lines = file_rewrite.readlines()
          file_rewrite.seek(0)
          for i in lines:
              if i.split('-')[0].strip() != key:
                  file_rewrite.write(i)
          file_rewrite.close()
        elif self.correct == True:
          continue

new_game = GameDay(date_now)

if new_game.date_now%1==0:
  begin_playing = Box(first_box)
  begin_playing.get_first_box()


  if new_game.date_now%2 == 0 and new_game.date_now%3 == 0 and new_game.date_now%4 == 0:
    begin_playing = Box(second_box)
    begin_playing.get_second_box()
    begin_playing = Box(third_box)
    begin_playing.get_third_box()
    begin_playing = Box(fourth_box)
    begin_playing.get_fourth_box()

  elif new_game.date_now%2 == 0 and new_game.date_now%3 == 0:
    begin_playing = Box(second_box)
    begin_playing.get_second_box()
    begin_playing = Box(third_box)
    begin_playing.get_third_box()

  elif new_game.date_now%2 == 0 and new_game.date_now%4 == 0:
    begin_playing = Box(second_box)
    begin_playing.get_second_box()
    begin_playing = Box(fourth_box)
    begin_playing.get_fourth_box()

  elif new_game.date_now%2 == 0:
    begin_playing = Box(second_box)
    begin_playing.get_second_box()

  elif new_game.date_now%3 == 0:
    begin_playing = Box(third_box)
    begin_playing.get_third_box()


print('this is the end of the game!\n ')

new_game.overall_progress()

new_game.progress_ask()

new_game.exit_or_no()
