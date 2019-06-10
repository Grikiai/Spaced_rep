# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs

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
    def __init__(self, date_now, answered_questions = 0, correctly_answered_questions = 0, lives = 7):
        self.date_now = date_now
        self.answered_questions = answered_questions
        self.correctly_answered_questions = correctly_answered_questions
        self.lives = lives

    def get_progress(self):
        if answered_questions == 0 and correctly_answered_questions == 0:
            progress_now = 'there were no progress, since all boxes are empty'
        else:
            progress_now = (self.correctly_answered_questions/self.answered_questions)*100
        return progressed_now

    def exit_or_no(self):
        yes_no2 = input('do you want to exit?y/n\n')
        if yes_no2.lower().strip() == 'y':
            exit
        elif yes_no2.lower().strip() == 'n':
          print('ok cool still bye')

    def overall_progress(self):
        if self.get_progress().strip().isalpha():
            progress = open('progress.txt', 'a', encoding = 'utf-8')
            achieved = 'on session '+ str(self.date_now)+' you made no progress, since all of the boxes were empty'
            progress.write()
            progress.close()
        else:
            progress = open('progress.txt', 'a')
            achieved = 'on session '+ str(self.date_now)+' you guessed '+ str(self.get_progress()+' % of words correctly')
            progress.write()
            progress.close()

    def progress_ask(self):
        print('do you want to see your progress?y/n\n')
        yes_no2 = input()
        if yes_no2.lower().strip() == 'n':
            new_game.exit_or_no()
        elif yes_no2.lower().strip() == 'y':
            output_progress = open('progress.txt', 'r', encoding = 'utf-8')
            print(output_progress.read())
            output_progress.close()


class Card:
    def __init__(self, pol, ltu, correct = True):
        self.lenkiskai = pol
        self.lietuviskai = ltu
        self.correct = correct
        self.lives = new_game.lives
		
    def ask_in_polish(self):
        print('Whats Lithuanian for '+ self.lenkiskai+ '?\n')
        answer = input()
        if answer.lower() == self.lietuviskai:
            self.correct == True
            new_game.answered_questions += 1
            new_game.correctly_answered_questions += 1
            print('Correct!\n')
        else:
            self.correct == False
            print(':Incorrect :(\n')
            print('you have '+ str(new_game.lives)+' lives now')
            self.guess()

    def guess(self):
        if new_game.lives >0:
            print('do you want to guess this word again?y/n\n')
            x = input()
            if x.lower().strip() == 'y':
                new_game.lives -=1
                self.ask_in_polish()
            elif x.lower().strip()!= 'y' and x.lower().strip()!= 'n':
                print('only y/n allowed!')
                self.guess()
        else:
            print('this is not enough lives to guess the word :(')
            print('you can only guess word one time')

class Box:
    def __init__(self, card):
        self.card = card

    def get_first_box(self):
        if len(first_box) != 0:
            for key in first_box.keys():
                y = first_box[key]
                z = Card(key, y)
                z.ask_in_polish()
                if z.correct == True:
                    file_rewrite = open('level_2.txt', 'a', encoding = 'utf-8')
                    file_rewrite.write(' - '.join([key, y])+'\n')
                    file_rewrite.close()
                    file_rewrite = open('level_1.txt', 'r+', encoding = 'utf-8')
                    lines = file_rewrite.readlines()
                    file_rewrite.seek(0)
                    for i in lines:
                        if i.split('-')[0].strip() != key:
                            file_rewrite.write(i)
                    file_rewrite.close()

        else:
          print('there are no words in first box!')



    def get_second_box(self):
        if len(first_box) != 0:
            for key in second_box.keys():
                y = second_box[key]
                z = Card(key, y)
                z.ask_in_polish()
                temp = ' - '.join([key, second_box[key]])
                if z.correct == False:
                    file_rewrite = open('level_1.txt', 'a', encoding = 'utf-8')
                    file_rewrite.write(temp+'\n')
                    file_rewrite.close()
                    file_rewrite = open('level_2.txt', 'r+', encoding = 'utf-8')
                    lines = file_rewrite.readlines()
                    file_rewrite.seek(0)
                    for i in lines:
                        if i.split('-')[0].strip() != key:
                            file_rewrite.write(i)
                    file_rewrite.close()
                elif z.correct == True:
                    file_rewrite = open('level_3.txt', 'a', encoding = 'utf-8')
                    file_rewrite.write(temp+'\n')
                    file_rewrite.close()
                    file_rewrite = open('level_2.txt', 'r+', encoding = 'utf-8')
                    lines = file_rewrite.readlines()
                    file_rewrite.seek(0)
                    for i in lines:
                        if i.split('-')[0].strip() != key:
                            file_rewrite.write(i)
                    file_rewrite.close()
        else:
          print('there are no words in second box!')


    def get_third_box(self):
        if len(first_box) != 0:
            for key in third_box.keys():
                y = third_box[key]
                z = Card(key, y)
                z.ask_in_polish()
                temp = ' - '.join([key, third_box[key]])
                if z.correct == False:
                    file_rewrite = open('level_1.txt', 'a', encoding = 'utf-8')
                    file_rewrite.write(temp+'\n')
                    file_rewrite.close()
                    file_rewrite = open('level_3.txt', 'r+', encoding = 'utf-8')
                    lines = file_rewrite.readlines()
                    file_rewrite.seek(0)
                    for i in lines:
                        if i.split('-')[0].strip() != key:
                            file_rewrite.write(i)
                    file_rewrite.close()
                elif self.correct == True:
                    file_rewrite = open('level_4.txt', 'a', encoding = 'utf-8')
                    file_rewrite.write(' - '.join(temp)+'\n')
                    file_rewrite.close()
                    file_rewrite = open('level_3.txt', 'r+', encoding = 'utf-8')
                    lines = file_rewrite.readlines()
                    file_rewrite.seek(0)
                    for i in lines:
                        if i.split('-')[0].strip() != key:
                            file_rewrite.write(i)
                            file_rewrite.close()
        else:
          print('there are no words in third box!')

    def get_fourth_box(self):
        if len(first_box) != 0:
            for key in fourth_box.keys():
                y = fourth_box[key]
                z = Card(key, y)
                z.ask_in_polish()
                temp = ' - '.join([key, fourth_box[key]])
                if z.correct == False:
                    file_rewrite = open('level_1.txt', 'a', encoding = 'utf-8')
                    file_rewrite.write(temp+'\n')
                    file_rewrite.close()
                    file_rewrite = open('level_4.txt', 'r+', encoding = 'utf-8')
                    lines = file_rewrite.readlines()
                    file_rewrite.seek(0)
                    for i in lines:
                        if i.split('-')[0].strip() != key:
                            file_rewrite.write(i)
                    file_rewrite.close()

        else:
            print('there are no words in fourth box!')


new_game = GameDay(date)
print(new_game.lives)

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
