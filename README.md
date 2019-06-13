# Spaced_rep

##  About spaced_rep

This is a spaced repetition based python code for learning word pairs (in particular - polish to lithuanian translations). 
Spaced repetition is a learning technique that incorporates increasing intervals of time between subsequent review of previously learned material in order to exploit the psychological spacing effect

This code uses Leitner method, which includes sorting words by increasing learning difficulty and therefore grouping them into different 'boxes'. Every correctly guessed card is sent to subsequent 'box' and every failure sends the card to the first box. Each box is reviewed at a different time interval - first box is reviewed every session, second box every other session and so on. You have 7 lives each session, however you can guess words should you answer them incorrectly. This does NOT give you extra life, only improves your progress. the game is won only when first three boxes are empty.

Asides from current code, there are 6 relevant files:
- 4 of which are word lists(level_1.txt, level_2.txt, level_3.txt, level_4.txt)
- one file is required to log sessions(log.txt)
- another one is required to log progress(progress.txt)

## Instalation and configuration
1. Download and extract files into a folder
2. Make sure all relevant files are in the same folder
2. Make sure log.txt progress.txt are empty 
3. If you want to use custom files(for instance, learning other words), make sure there is newline character after the last pair. Words should also be separated by ' - ' (space, hyphen and then again, space. no spaces should be after each word pair). there should also be a newline character after each word pair.
