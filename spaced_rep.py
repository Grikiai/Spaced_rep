log = open('log.txt', 'r')
logs = log.readlines()
log.close()
date = len(logs)+1

log = open('log.txt', 'a')
logs = log.write(str(date)+' is the number of latest session\n')
log.close()

zodziai1 = open('level_1.txt', 'r', encoding = 'utf-8')
Wordlist1 = zodziai1.readlines()
zodziai1.close()
first_box = {}
for i in Wordlist1:
    key = i.split('-')[0].strip()
    if key not in first_box:
        first_box[key] = i.split('-')[1].strip()

zodziai2 = open('level_2.txt', 'r', encoding = 'utf-8')
Wordlist2 = zodziai2.readlines()
zodziai2.close()
second_box = {}
for i in Wordlist2:
    key = i.split('-')[0].strip()
    if key not in second_box:
        second_box[key] = i.split('-')[1].strip()

zodziai3 = open('level_3.txt', 'r', encoding = 'utf-8')
Wordlist3 = zodziai3.readlines()
zodziai3.close()
third_box = {}
for i in Wordlist3:
    key = i.split('-')[0].strip()
    if key not in third_box:
        third_box[key] = i.split('-')[1].strip()

zodziai4 = open('level_4.txt', 'r', encoding = 'utf-8')
Wordlist4 = zodziai4.readlines()
zodziai4.close()
fourth_box = {}
for i in Wordlist4:
    key = i.split('-')[0].strip()
    if key not in fourth_box:
        fourth_box[key] = i.split('-')[1].strip()

class GameDay:
    def __init__(self, date_now, answered_questions = 0, correctly_answered_questions = 0, lives = 7, winning = False):
        self.date_now = date_now
        self.answered_questions = answered_questions
        self.correctly_answered_questions = correctly_answered_questions
        self.lives = lives
        self.winning = winning

    def get_progress(self):
        if self.answered_questions == 0 and self.correctly_answered_questions == 0:
            progress_now = 'there were no progress, since all scheduled boxes are empty'
        else:
            progress_now = (self.correctly_answered_questions/self.answered_questions)*100
        return progress_now

    def exit_or_no(self):
        yes_no3 = input('do you want to exit?y/n\n')
        if yes_no3.lower().strip() == 'y':
            quit
        elif yes_no3.lower().strip() == 'n':
          print('ok cool still bye')

    def overall_progress(self):
        if self.get_progress() == 'there were no progress, since all scheduled boxes are empty':
            achieved = 'on session '+ str(self.date_now) +' you made no progress, since all of the scheduled boxes were empty\n'
            with open('progress.txt', 'a', encoding = 'utf-8') as f:
                f.write(achieved)

        else:
            achieved = 'on session ' + str(self.date_now) + ' you guessed ' +  str(self.get_progress()) + ' % of words correctly\n'
            with open('progress.txt', 'a', encoding = 'utf-8') as f:
                f.write(achieved)

        if self.winning == True:
            achieved = 'on session ' + str(self.date_now) + ' you won the game!\n'
            with open('progress.txt', 'a', encoding = 'utf-8') as f:
                f.write(achieved)

    def progress_ask(self):
        print('do you want to see your progress?y/n\n')
        yes_no2 = input()
        if yes_no2.lower().strip() == 'n':
            self.exit_or_no()
        elif yes_no2.lower().strip() == 'y':
            output_progress = open('progress.txt', 'r', encoding = 'utf-8')
            print(output_progress.read())
            output_progress.close()

    def rewrite_cards(self):
        with open('level_1.txt', 'w', encoding = 'utf-8') as f:
            for line in Wordlist1:
                f.write("%s" % line)

        with open('level_2.txt', 'w', encoding = 'utf-8') as f:
            for line in Wordlist2:
                f.write("%s" % line)

        with open('level_3.txt', 'w', encoding = 'utf-8') as f:
            for line in Wordlist3:
                f.write("%s" % line)

        with open('level_4.txt', 'w', encoding = 'utf-8') as f:
            for line in Wordlist4:
                f.write("%s" % line)

    def did_you_win(self):
        if len(first_box)+len(second_box)+len(third_box)!=0:
            self.winning = False
            print('This is the end of the game. You have not won . Yet..'.upper())
        elif len(Wordlist1)+ len(Wordlist2)+ len(Wordlist3)!=0:
            self.winning = False
            print('This is the end of the game. You have not won .Yet..'.upper())
        else:
            self.winning = True
            print('you have won the game!'.upper())

    def card_reveal(self):
        print('you now have the option to reveal sceduled cards. reveal?y/n'.upper())
        yes_no = input()
        if yes_no.strip().lower() == 'y':
            print('These are the words currently in first box:\n')
            for i in Wordlist1:
                print(i)
            if self.date_now%2 ==0:
                print('These are the words currently in second box:\n')
                for i in Wordlist2:
                    print(i)
            elif self.date_now%3 ==0:
                print('These are the words currently in third box:\n')
                for i in Wordlist3:
                    print(i)
            elif self.date_now%4 ==0:
                print('These are the words currently in fourth box:\n')
                for i in Wordlist4:
                    print(i)
    def intro(self):
        if self.date_now==1:
            print('Welcome to spaced repetition based game! this particular version is created in order to learn polish-lithuanian word translations')
            print("There are four 'boxes' in this game, each of which are scheduled to be given at diferent session")
            print('The rules are such: every incorrect word is moved down to first box and every correct word is moved to subsequent box')
            print('You have 7 lives, also you can guess the word as many times as you like(sadly, that costs one life)')
            print('The game is won when all boxes except fourth are empty (that means you know them all!)')

class Card:
    def __init__(self, pol, ltu, correct = True):
        self.lenkiskai = pol
        self.lietuviskai = ltu
        self.correct = correct
        self.lives = new_game.lives

    def ask_in_polish(self):
        print('\nWhats Lithuanian for '.upper()+ self.lenkiskai.upper()+ '?')
        answer = input()
        if answer.lower().strip() == self.lietuviskai:
            self.correct = True
            new_game.answered_questions += 1
            new_game.correctly_answered_questions += 1
            print('Correct!\n'.upper())
        else:
            self.correct = False
            new_game.lives -=1
            print(':Incorrect :(\n'.upper())
            print('you have '.upper() + str(new_game.lives)+' lives now\n'.upper())
            self.guess()

    def guess(self):
        if new_game.lives >0:
            print('do you want to guess this word again?y/n'.upper())
            x = input()
            if x.lower().strip() == 'y':
                new_game.lives -=1
                self.ask_in_polish()
            elif x.lower().strip() == 'n':
                new_game.answered_questions +=1
            elif x.lower().strip()!= 'y' and x.lower().strip()!= 'n':
                print('only y/n allowed!\n'.upper())
                self.guess()
        else:
            print('this is not enough lives to guess the word or play the game:(')

class Box:
    def __init__(self, card):
        self.card = card

    def get_first_box(self):
        if len(first_box) != 0:
            for key in first_box.keys():
                if new_game.lives>0:
                    y = first_box[key]
                    z = Card(key, y)
                    z.ask_in_polish()
                    if z.correct == True:
                        temp = ' - '.join([key, y])+'\n'
                        Wordlist2.append(temp)
                        Wordlist1.remove(temp)
                else:
                    break
        else:
          print('there are no words in first box!')


    def get_second_box(self):
        if len(first_box) != 0:
            for key in second_box.keys():
                if new_game.lives>0:
                    y = second_box[key]
                    z = Card(key, y)
                    z.ask_in_polish()
                    if z.correct == False:
                        temp = ' - '.join([key, y])+'\n'
                        Wordlist1.append(temp)
                        Wordlist2.remove(temp)
                    elif z.correct == True:
                        temp = ' - '.join([key, y])+'\n'
                        Wordlist3.append(temp)
                        Wordlist2.remove(temp)
                else:
                    break
        else:
          print('there are no words in second box!')

    def get_third_box(self):
        if len(first_box) != 0:
            for key in third_box.keys():
                if new_game.lives>0:
                    y = third_box[key]
                    z = Card(key, y)
                    z.ask_in_polish()
                    if z.correct == False:
                        temp = ' - '.join([key, y])+'\n'
                        Wordlist1.append(temp)
                        Wordlist3.remove(temp)
                    elif z.correct == True:
                        temp = ' - '.join([key, y])+'\n'
                        Wordlist4.append(temp)
                        Wordlist3.remove(temp)
                else:
                    break
        else:
          print('there are no words in third box!')

    def get_fourth_box(self):
        if len(first_box) != 0:
            for key in fourth_box.keys():
                if new_game.lives>0:
                    y = fourth_box[key]
                    z = Card(key, y)
                    z.ask_in_polish()
                    if z.correct == False:
                        temp = ' - '.join([key, y])+'\n'
                        Wordlist1.append(temp)
                        Wordlist4.remove(temp)
                else:
                    break
        else:
            print('there are no words in fourth box!')

new_game = GameDay(date)
new_game.intro()
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

new_game.rewrite_cards()
new_game.did_you_win()
new_game.card_reveal()
new_game.overall_progress()
new_game.progress_ask()
new_game.exit_or_no()
