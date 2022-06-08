from os import system, name
from re import L
from time import sleep
from getkey import getkey
import colorama
from colorama import *
import random
import time
from time import sleep
import sys
import string
import collections
import re
# <<< leveys 216

current = [10,11,12,13,14,15,16,17,18,19,20,227,228,229,230,231,232,233,234,235,236,237,444,445,446,447,448,449,450,451,452,453,454,661,662,663,664,665,666,667,668,669,670,671]

string2 = """              
.___________. _______ .______      .___  ___.  __  .__   __.      ___       __              ___      .__   __.  __  .___  ___.      ___   .___________.  ______   .______         
|           ||   ____||   _  \     |   \/   | |  | |  \ |  |     /   \     |  |            /   \     |  \ |  | |  | |   \/   |     /   \  |           | /  __  \  |   _  \        
`---|  |----`|  |__   |  |_)  |    |  \  /  | |  | |   \|  |    /  ^  \    |  |           /  ^  \    |   \|  | |  | |  \  /  |    /  ^  \ `---|  |----`|  |  |  | |  |_)  |       
    |  |     |   __|  |      /     |  |\/|  | |  | |  . `  |   /  /_\  \   |  |          /  /_\  \   |  . `  | |  | |  |\/|  |   /  /_\  \    |  |     |  |  |  | |      /        
    |  |     |  |____ |  |\  \----.|  |  |  | |  | |  |\   |  /  _____  \  |  `----.    /  _____  \  |  |\   | |  | |  |  |  |  /  _____  \   |  |     |  `--'  | |  |\  \----.   
    |__|     |_______|| _| `._____||__|  |__| |__| |__| \__| /__/     \__\ |_______|   /__/     \__\ |__| \__| |__| |__|  |__| /__/     \__\  |__|      \______/  | _| `._____| 
+-+-+-+-+-+ +-+-
Press i for info
+-+-+-+-+-+ +-+- 
Animation field:::::
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
"""






c = []

# Clearing screen
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  
clear()

c_colors = [["b", "b"], ["bl", "bl"], ["c", "c"], ["g", "g"], ["l", "l"], ["lb", "lb"], ["lc", "lc"], ["lg", "lg"], ["lm", "lm"], ["lr", "lr"], ["lw", "lw"], ["ly", "ly"], ["m", "m"], ["re", "re"], ["w", "w"], ["y", "y"]]

# Encoding symbols
def tempo():
    global c
    c = []
    for x in range(7776):
        if x > 4444:
            c.append(["b", "g", "."])
        else:
            c.append(["g", "b", "."])    

tempo()


tt = ["bl","bl"," "]
# Decoding symbols:
def e(symbol):
    dic = {"r":[Back.RESET, Fore.RESET],"re":[Back.RED,Fore.RED],"w":[Back.WHITE, Fore.WHITE],"g":[Back.GREEN,Fore.GREEN],"b":[Back.BLACK, Fore.BLACK],"c":[Back.CYAN,Fore.CYAN],"bl":[Back.BLUE,Fore.BLUE],"y":[Back.YELLOW,Fore.YELLOW], "l":[Back.LIGHTBLACK_EX,Fore.LIGHTBLACK_EX],"lb":[Back.LIGHTBLUE_EX,Fore.LIGHTBLUE_EX],"lc":[Back.LIGHTCYAN_EX,Fore.LIGHTCYAN_EX],"lg":[Back.LIGHTGREEN_EX,Fore.LIGHTGREEN_EX],"lm":[Back.LIGHTMAGENTA_EX,Fore.LIGHTMAGENTA_EX],"lr":[Back.LIGHTRED_EX,Fore.LIGHTRED_EX],"lw":[Back.LIGHTWHITE_EX,Fore.LIGHTWHITE_EX],"ly":[Back.LIGHTYELLOW_EX,Fore.LIGHTYELLOW_EX],"m":[Back.MAGENTA,Fore.MAGENTA]}
    back = dic[symbol[0]][0]
    fore = dic[symbol[1]][1]
    return back + fore + symbol[2]                

lstring = list(string2)

# Making opening view:
def make():
    global string2,c,lstring
    for x in range(len(lstring)):
        if lstring[x] == "<":
            lstring[x] = f"{e(c[x-1196])}"
    string2 = "".join(lstring)       
make()


# Printing all stuff:
def default():
    clear()
    print(Back.RESET + Fore.RESET + string2 + Back.RESET + Fore.RESET  + f"\n Cursor color: " + e(c_color + ["<"]) + Back.RESET + Fore.RESET + " Selected drawing background color: " + e(s_b_color + [" "]) + Back.RESET + Fore.RESET + " Selected drawing fore symbol color: " + e(s_f_color + [" "]) + Back.RESET + Fore.RESET + " Selected drawing symbol: " + s_s)
    #print(lstring)
    #print(current+1159)


s_b_color = c_colors[14]

s_f_color = c_colors[0]

s_s = "<"

c_color = c_colors[14]


default()

frames = []




def ansi_shortner(ansi):
    result = []
    num = []
    for x in ansi:
        if x.isdigit():
            num.append(x)
        else:
            result.append("".join(num))
            num = []
    return result + [ansi[-1]]            



def play():
    name = input("Enter file name:\n")
    text = open(f"Animations/{name}", 'r').read()
    print(text)    
    l = []
    print(text[0])
    for x in eval(text)[0]:
        for y in range(x[1]):
            l.append(x[0])
 #   print(l)        
    for x in range(len(lstring[1159:])):
        try:
            if lstring[1159:][x] != '\n':
                lstring[x + 1159] = l[x]
        except:
            pass        
    default()        




file_content = []




def save():
    global file_content
    # eka sybooli ei tulku
    data_to_be_pushed_to_file_content = []
    previos = None
    num_o_times = 0
    nnn = []
    for x in lstring:
        if x != '\n':
            nnn.append(x)
    nnn = nnn[1149:]   
    nnn.append(nnn[-1])  
    for y in range(len(nnn)):
        x = nnn[y]
        if x == previos and y != len(nnn)-1:
            num_o_times += 1  
        else:
            data_to_be_pushed_to_file_content.append([previos, num_o_times])    
            num_o_times = 0
        previos = x
    file_content.append(data_to_be_pushed_to_file_content[1:])   


def count_h_w():
    global h,width,minH,debug
    for x in current:
        h.append(x // 217)
    debug.append([h])  
    minH = min(h)   
    width = h.count(max(h,key=h.count))
    h = max(h) - min(h) + 1
    


# 217 is number of chars in one x level on animator

while True:
    # var move tells direction for movement
    h, prevs, debug, Hpositions, newcur = [], [], [], [], []
    move, wasd, previous_x = 0, 0, 0
    count_h_w()
    key = getkey()
    if key == "i":
        clear()
        print(Back.RESET + Fore.RESET + """
        Terminal Animator v.1.2 is an animator that runs in bash terminal
        How to use it?
        //FILLLATER//
        press b to get back to the default view
        press q to quit
        
        Cursor:
        Move cursor from wasd
        Cursor areas background is red
        press m to make cursor larger x level
        press n to make cursor larger in y level
        press j to make cursor smaller y level
        press k to make cursor smaller x level
        Drawing:
        press b to change pencil bg color
        press f to change pencil symbol color
        press z to write down selected symbol for pencil


        press S to save current draw


        IF ALL TEXT GETS UNDERLINED: RESET TERMIAL (bash: Terminal: Reset and then press any key) (Program wont go away)
        """, Back.RESET)
    if key == "b":
        clear()
        default()   
    if key == "q":
        clear()
        raise SystemExit(0)       
    if key == "w":
            move -= 217
            wasd += 1
    if key == "s":
            move += 217
            wasd += 1
    if key == "d":
            move += 1
            wasd += 1
    if key == "a":
            move -= 1
            wasd += 1
    if key == "c":
        if c_colors.index(c_color) == len(c_colors) - 1:
            c_color = c_colors[0]
        else:
            c_color = c_colors[c_colors.index(c_color)+1]  
        wasd += 1   
    if key == "b":
        if c_colors.index(s_b_color) == len(c_colors) - 1:
                s_b_color = c_colors[0]
        else:
            s_b_color = c_colors[c_colors.index(s_b_color)+1]  
        wasd += 1  
    if key == "f":
        if c_colors.index(s_f_color) == len(c_colors) - 1:
            s_f_color = c_colors[0]
        else:
            s_f_color = c_colors[c_colors.index(s_f_color)+1]  
        wasd += 1           
    if key == "z":
        s_s = input("Write symbol:\n") 
        wasd += 1


    if key == "S":
        save()


    if key == "P":
        play()    

    # Largening cursor x level
    if key == "m":
        for x in current:
            if previous_x != 0:
                if x != previous_x + 1 and not (previous_x + 1) % 217 == 0:
                    newcur.append(previous_x + 1)
                    newcur.append(x)
                else:
                    newcur.append(x)  
            else:
                newcur.append(x)     
            if current.index(x) == len(current)-1 and not (x + 1) % 217 == 0:
                newcur.append(x + 1)         
            previous_x = x        
        current = newcur
        wasd += 1 
    # Largening curor y level
    if key == "n":
        lasts = current[-width:]
        for x in lasts:
            if x + 217 + 1159 < len(lstring):
                current.append(x+217)
        wasd += 1    
    # Blocking cursor for going over area:        
    
    if key == "j":
        if len(current) / width > 1:
            for x in range(width):
                current = current[:-1]
            wasd += 1    

    if key == "k":
        if width > 1:
            del current[width-1::width]
            wasd += 1
    debug.append([h, "Haloe"]) 


    if key == "C":
        name = input("Enter animation's file name (for example anim.ta)\n")
        with open(f"Animations/{name}", 'w') as f:
            f.write(str(file_content))

    for x in range(len(current)):
        if current[x] // 217 - minH not in Hpositions:
            Hpositions.append(current[x] // 217 - minH)
    
    for x in range(len(current)):
        positionH_for_up_wall = current[x] // 217 - minH
        positionH_for_down_wall = Hpositions[len(Hpositions) - Hpositions.index(positionH_for_up_wall) - 1]
        debug.append([positionH_for_up_wall,current[x] // 217,h,current[x] // 217 - minH,current[x] // 217 + minH]) 
        # Setting move orders: 
        if current[x] + move >= 0 + positionH_for_up_wall * 217 and current[x] + move < len(lstring) - 1159 - positionH_for_down_wall * 217 and not (current[len(current)-1] + move) % 217 == 0 and not (current[len(current)-1] - width + 1 + move + -217*987) % -217 == 0:
            current[x] = current[x] + move    
    #### 
    # Displaying movement:  
    for x in current:      
        prevs.append([lstring[x + 1159], x + 1159])        
        lstring[x + 1159] = e(c_color + ["<"])
 
    string2 = "".join(lstring)  
    for x in prevs:
        lstring[x[1]] = x[0] 
    if key == "x":
        for x in current:
            lstring[x + 1159] = e([s_b_color[0], s_f_color[0], s_s])         
    if wasd > 0:         
        default()  
    #print(Fore.RESET,current, len(lstring) - 1159,debug)    
      