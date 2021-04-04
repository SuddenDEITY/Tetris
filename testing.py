import numpy as np
import sys
def dletters():
    return {
     "I": [[4, 14, 24, 34],
           [3, 4, 5, 6]],
     "S": [[4, 5, 13, 14],
           [4, 14, 15, 25]],
     "J": [[5, 15, 24, 25],
           [3, 4, 5, 15],
           [4, 5, 14, 24],
           [4, 14, 15, 16]],
     "T": [[4, 14, 15, 24],
           [4, 13, 14, 15],
           [5, 14, 15, 25],
           [4, 5, 6, 15]],
     "O": [[4, 5, 14, 15]],
     "L": [[4, 14, 24, 25],
           [5, 14, 15, 13],
           [4, 5, 15, 25],
           [4, 5, 6, 14]],
     "Z": [[4, 5, 15, 16],
           [5, 14, 15, 24]]}
class Tetris:
 dimens = None
 letters = {
     "I": [[4, 14, 24, 34],
           [3, 4, 5, 6]],
     "S": [[4, 5, 13, 14],
           [4, 14, 15, 25]],
     "J": [[5, 15, 24, 25],
           [3, 4, 5, 15],
           [4, 5, 14, 24],
           [4, 14, 15, 16]],
     "T": [[4, 14, 15, 24],
           [4, 13, 14, 15],
           [5, 14, 15, 25],
           [4, 5, 6, 15]],
     "O": [[4, 5, 14, 15]],
     "L": [[4, 14, 24, 25],
           [5, 14, 15, 13],
           [4, 5, 15, 25],
           [4, 5, 6, 14]],
     "Z": [[4, 5, 15, 16],
           [5, 14, 15, 24]]}
 default = None
 curpos = 0
 curletter = None

def checkborders(dir):
    sp = Tetris.letters[Tetris.curletter][Tetris.curpos]
    bl = True
    if dir == 'right':
        for el in sp:
            if str(el).endswith('9') or str(el).startswith(str(Tetris.dimens[0] - 1)) and el != Tetris.dimens[0] - 1:
                bl = False
    if dir == 'down':
        for el in sp:
            if str(el).startswith(str(Tetris.dimens[0] - 1)) and el != Tetris.dimens[0] - 1:
                bl = False
    if dir == 'left':
        print(sp)
        for el in sp:
            if str(el).endswith('0') or str(el).startswith(str(Tetris.dimens[0] - 1)) and el != Tetris.dimens[0] - 1:
                bl = False
    if dir == 'rotate':
        first = False
        second = False
        if Tetris.curpos + 1 < (len(Tetris.letters[Tetris.curletter])):
            spc = Tetris.letters[Tetris.curletter][Tetris.curpos + 1]
        else:
            spc = Tetris.letters[Tetris.curletter][0]
        for el in spc:
            if str(el).endswith('9'):
                first = True
            if str(el).endswith('0'):
                second = True
        for el in sp:
            if str(el).startswith(str(Tetris.dimens[0] - 1)) and el != Tetris.dimens[0] - 1:
                bl = False
        bl = (not (first * second)) and bl
    return bl

def newspawn(letter):
    if letter == 'piece':
        letter = input()
    localflat = Tetris.default.flatten()
    for i in range(4):
        localflat[Tetris.letters[Tetris.curletter][Tetris.curpos][i]] = '0'
    Tetris.curpos = 0
    Tetris.default = localflat
    Tetris.curletter = letter
    Tetris.letters = dletters()
    if letter == 'break':
        while '-' not in Tetris.default.reshape(Tetris.dimens)[-1]:
         localflat = Tetris.default.flatten()
         for i in range(4):
             localflat[Tetris.letters[Tetris.curletter][Tetris.curpos][i]] = '0'
         Tetris.curpos = 0
         Tetris.default = localflat
         Tetris.default = np.insert(Tetris.default.reshape(Tetris.dimens), 0, ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'])
         Tetris.default = Tetris.default.reshape(Tetris.dimens[0]+1, Tetris.dimens[1])[:-1]


def right():
  if checkborders('right') and collision('right'):
      for i in range(len(Tetris.letters[Tetris.curletter])):
          for j in range(4):
              Tetris.letters[Tetris.curletter][i][j] += 1
  if checkborders('down') and collision('down'):
      for i in range(len(Tetris.letters[Tetris.curletter])):
          for j in range(4):
              Tetris.letters[Tetris.curletter][i][j] += 10

def down():
  res = False
  sp = Tetris.letters[Tetris.curletter][Tetris.curpos]
  for el in sp:
      if el < 20 and not collision('down'):
          res = True
  if res:
      printer()
      print()
      print('Game Over!')
      sys.exit()
  if checkborders('down') and collision('down'):
     for i in range(len(Tetris.letters[Tetris.curletter])):
         for j in range(4):
              Tetris.letters[Tetris.curletter][i][j] += 10
  else:
      newspawn(input())


def left():
    if checkborders('left') and collision('left'):
        for i in range(len(Tetris.letters[Tetris.curletter])):
            for j in range(4):
                Tetris.letters[Tetris.curletter][i][j] -= 1
    if checkborders('down') and collision('down'):
        for i in range(len(Tetris.letters[Tetris.curletter])):
            for j in range(4):
                Tetris.letters[Tetris.curletter][i][j] += 10

def rotate():
  if checkborders('rotate') and collision('rotate'):
        if Tetris.curpos < len(Tetris.letters[Tetris.curletter]) - 1:
            Tetris.curpos += 1
        else:
            Tetris.curpos = 0
  if checkborders('down') and collision('down'):
    for i in range(len(Tetris.letters[Tetris.curletter])):
        for j in range(4):
            Tetris.letters[Tetris.curletter][i][j] += 10

def start():
     size = input()
     size = size.split(' ')
     Tetris.dimens = (int(size[1]), int(size[0]))
     Tetris.default = np.full((Tetris.dimens[0], Tetris.dimens[1]), '-')
     for i in range(int(size[1])):
         print(*Tetris.default[i])
     Tetris.default = Tetris.default.flatten()
     print()
     letter = input()
     if letter == 'piece':
         letter = input()
     Tetris.curletter = letter
     for i in range(4):
         Tetris.default[Tetris.letters[Tetris.curletter][0][i]] = '0'
     for i in range(Tetris.dimens[0]):
         print(*Tetris.default.reshape(int(size[1]), int(size[0]))[i])
     Tetris.default = np.full((Tetris.dimens[0], Tetris.dimens[1]), '-')
     print()
     game()

def collision(dir):
    sp = Tetris.letters[Tetris.curletter][Tetris.curpos]
    bl = True
    if dir == 'right':
        for el in sp:
            if Tetris.default.flatten()[el+1] == '0' or Tetris.default.flatten()[el+10] == '0':
                bl = False
    if dir == 'down':
        for el in sp:
            if Tetris.default.flatten()[el+10] == '0':
                bl = False
    if dir == 'left':
        for el in sp:
            if Tetris.default.flatten()[el-1] == '0' or Tetris.default.flatten()[el+10] == '0':
                bl = False
    if dir == 'rotate':
        if Tetris.curpos + 1 < len(Tetris.letters[Tetris.curletter]):
         spc = Tetris.letters[Tetris.curletter][Tetris.curpos + 1]
        else:
         spc = Tetris.letters[Tetris.curletter][0]
        for el in sp:
            if Tetris.default.flatten()[el+10] == '0':
                bl = False
        for el in spc:
            if Tetris.default.flatten()[el] == '0':
                bl = False
    return bl

def printer():
    localflat = Tetris.default.flatten()
    for i in range(4):
          localflat[Tetris.letters[Tetris.curletter][Tetris.curpos][i]] = '0'
    for i in range(Tetris.dimens[0]):
          print(*localflat.reshape(Tetris.dimens)[i])

def game():
    n = input()
    while n != 'exit':
        if n.lower() == 'down':
         down()
        elif n.lower() == 'right':
         right()
        elif n.lower() == 'left':
         left()
        elif n.lower() == 'rotate':
            rotate()
        printer()
        print()
        n = input()

start()