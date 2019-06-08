# Spaced_rep

##  About spaced_rep

This is a spaced repetition based python code for learning languages (in particular - polish to lithuanian translations). 
Spaced repetition is a learning technique that incorporates increasing intervals of time between subsequent review of previously learned material in order to exploit the psychological spacing effect

This code uses Leitner method, which includes sorting words by increasing learning difficulty and therefore grouping them into different 'boxes'. Every correctly guessed card is sent to subsequent 'box' and every failure sends the card to the first box. Each box is reviewed at a different time interval - first box is reviewed every session, second box every other session and so on.

Asides from current code, there are 6 relevant files:
- 4 of which are word lists(level_1.txt, level_2.txt, level_3.txt, level_4.txt)
- one file is required to log sessions(log.txt)
- another one is required to log progress(progress.txt)

## Instalation and configuration
1. Download and extract files into a folder
2. Make sure log.txt progress.txt are empty (if there aren't files with these names - dont worry! they will be automatically created when the code is running)
3. Open file named spaced_rep.py through command line
