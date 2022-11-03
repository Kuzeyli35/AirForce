import random, os, time, threading
from pynput.keyboard import Key, Listener
from pynput import keyboard

canvas = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]


playground = canvas.copy()
enemies = []
ship = [-1, 5]
GAME = True
moves =  0

def reset():
    return  [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]
    

#generate enemy
class Enemy:
    def __init__(self, satır=0, sütun=0):
        self.satır = satır
        self.sütun = sütun

    def generate(self):
        self.satır = 0
        self.sütun = random.randint(0, len(canvas[0])-1)
        return [self.satır, self.sütun]

#print playground
def draw():
    global playground
    while True:
        os.system('cls')
        for line in playground:
            print("".join(line))
        time.sleep(0.2)

#changing ship coords but not update in scene       
def shipMove():
    global ship, moves, canvas
    if ship[1] != len(canvas[-1]) and moves == 1:
        ship[1] += 1
    elif ship[1] != 0 and moves == -1:
        ship[1] -= 1

    moves = 0



def update():
    global playground, ship
    playground = reset()  
    enemy = Enemy()

    if random.randint(0, 10) == 1:
        enemies.append(enemy.generate())

    if len(enemies) >= 1:
        for i in enemies:
            playground[i[0]][i[1]] = "0"

    for i in enemies:
        i[0] += 1
        if i[0] >= len(canvas):
            enemies.remove(i) 
    
    shipMove()
    playground[ship[0]][ship[1]] = "A"

    
#getting key press and use it in shipMove()
def getKey(key):
    global moves
    if key == Key.right:
        moves = 1
    elif key == Key.left:
        moves = -1
    else:
        pass



def main():
    while GAME:
        update()
        getKey(Key)




mainloop = threading.Thread(target=main)
move = keyboard.Listener(on_press=getKey)
scene = threading.Thread(target=draw)

mainloop.start()
move.start()
scene.start()

mainloop.join()
move.join()
scene.join()
