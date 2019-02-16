#!/usr/bin/python3

import os
import sys

class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def print_map(map):
    for string in map:
        print(string[:-1])
    print()

def change(map, Xposition, Xnewposition):
    map[Xposition.y] = map[Xposition.y].replace("X", " ")
    map[Xnewposition.y] = map[Xnewposition.y][:Xnewposition.x] + "X" + map[Xnewposition.y][Xnewposition.x + 1:]
    Xposition.x = Xnewposition.x
    Xposition.y = Xnewposition.y

def move(map, direction, number, Xposition):
    Xnewpositon = position(0,0)
    while (number > 0):
        if (direction == "N"):
            Xnewpositon.x = Xposition.x
            Xnewpositon.y = Xposition.y - 1
            if (map[Xnewpositon.y][Xnewpositon.x] == " "):
                change(map, Xposition, Xnewpositon)
            elif (map[Xnewpositon.y][Xnewpositon.x] == "U"):
                change(map, Xposition, Xnewpositon)
                return True
            else:
                break
        elif (direction == "E"):
            Xnewpositon.x = Xposition.x + 1
            Xnewpositon.y = Xposition.y
            if (map[Xnewpositon.y][Xnewpositon.x] == " "):
                change(map, Xposition, Xnewpositon)
            elif (map[Xnewpositon.y][Xnewpositon.x] == "U"):
                change(map, Xposition, Xnewpositon)
                return True
            else:
                break
        elif (direction == "S"):
            Xnewpositon.x = Xposition.x
            Xnewpositon.y = Xposition.y + 1
            if (map[Xnewpositon.y][Xnewpositon.x] == " "):
                change(map, Xposition, Xnewpositon)
            elif (map[Xnewpositon.y][Xnewpositon.x] == "U"):
                change(map, Xposition, Xnewpositon)
                return True
            else:
                break
        elif (direction == "O"):
            Xnewpositon.x = Xposition.x - 1
            Xnewpositon.y = Xposition.y
            if (map[Xnewpositon.y][Xnewpositon.x] == " "):
                change(map, Xposition, Xnewpositon)
            elif (map[Xnewpositon.y][Xnewpositon.x] == "U"):
                change(map, Xposition, Xnewpositon)
                return True
            else:
                break
        number -= 1
    return False

def save(map, path):
    file = open(path, "w+")
    for string in map:
        file.write(string)
    file.close()

def play(map, path, Xposition):
    win = False
    number = 0
    allowed_chars = set('qnesoQNESO')
    print_map(map)
    while (win == False):
        save(map, path)
        while (True):
            command = input("> ")
            if set(command[0]).issubset(allowed_chars):
                if (command[0].upper() == "Q"):
                    save(map, path)
                    exit()
                if (len(command) > 1):
                    try:
                        number = int(command[1:])
                    except:
                        continue
                else:
                    number = 1
                break
        win = move(map, command[0].upper(), number, Xposition)
        print()
        print_map(map)
    print("You win")

def check(fichier, path):
    X = 0
    map = fichier.readlines()
    fichier.close()
    allowed_chars = set('O \nUX')
    allowed_chars_line = set('O \nU')
    for i, validationString in enumerate(map):
        if not set(validationString).issubset(allowed_chars):
            print("Problem with the map")
            exit()
        X += validationString.count("X")
        if (validationString.find("X") != -1 and X == 1):
            Xposition = position(validationString.find("X"),i)
        if (i == 0 or len(map) == i):
            if not set(validationString).issubset(allowed_chars_line):
                print("Problem with the map")
                exit()
        elif not ((validationString[-2:] == "O\n" or validationString[-2:] == "U\n") and (validationString[0] == "O" or validationString[0] == "U")):
            print("Problem with the map")
            exit()
    if (X == 0 or X > 1):
        print("Problem with the map")
        exit()
    play(map, path, Xposition)

if (len(sys.argv) == 2):
    try:
        fichier = open(sys.argv[1], "r")
    except:
        print('Open problem with file :'+os.path.normpath(sys.argv[1]))
        exit()
    check(fichier,sys.argv[1])
else:
    print("Problem with argument")