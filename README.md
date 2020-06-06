# TETRIS
A improved tetris clone written in Python3.8 and Pygame

## What's new?
When start, you can set the falling speed of tetrominos, and... 

*Unlike* the old version, this one has an additional option - **malice** level.

Game has implemented minmax alghoritm - every time your tetromino falled, game calculates the most optimal (or not!) block. When malice level set to 9 - don't expect *L* tetromino too often ;) 


## Installation
To play this game, clone this repo, change directory and run ```./Game.py``` file. 

## How to play?
You can control falling tetromino as in the classic NES version:
|Arrow|Action|
|: -: |: -: |
| ↑ 	| rotates tetromino clockwise 	|
| ↓ 	| speeds up falling down 	|
| → 	| moves left 	|
| ← 	| moves right 	|

## Do you prefer orange or pink?
This game is fully customizable. The constans used to set window size and colors within game are located in ```config.py``` file.

When you change, in example, ```SCREEN_WIDTH``` and ```SCREEN_HEIGHT``` everything should work correct. 

## About project
This tetris clone is written as a semester project of symbolic programming. The main purpose of this project is to improve my coding skills and try make something on my own. 
