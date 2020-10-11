import os

if os.name == "nt":
    import msvcrt
else:
    import curses, time

def cls(all = False):
    if os.name == "nt":
        os.system('cls')
    else:
        print("\033[H")
        if all:
            print("\033[J",end="")
def input_char():
    if os.name == "nt":
        return msvcrt.getch().decode("utf-8")
    else:
        try:
            win = curses.initscr()
            #win.addstr(0, 0, message)
            while True: 
                ch = win.getch()
                if ch in range(32, 127): 
                    break
                time.sleep(0.05)
        finally:
            curses.endwin()
        return chr(ch)



def toBin(val, original=-1):
    bin = format(int(val), '08b')
    if len(bin) < original:
        bin = "0"*(original-len(bin)) + bin
    return bin
def toInt(val):
    return int(val, 2)
#print(toBin(101))

def parseMap(val, wsize, fsize = -1):
    out = ""
    ind = 0
    for i in toBin(val, fsize):
        if ind > wsize:
            out += "\n"
            ind = 0
        ind = ind + 1
        out = out + i
    return out
def pack(data, wsize, fsize):
    return str(wsize) + "#" + str(data) + "#" + str(fsize)
if __name__ == "__main__":
    map =  "001100110011001100"
    mapw = 6


    #print("Map: " + map)
    enc = toInt(map)
    print("Encoded: " + str(enc))
    #print("Decoded raw: " + str(toBin(enc, len(map))))
    dec = parseMap(enc, mapw-1, len(map))
    print("Decoded map: \n" + str(dec))

    print()
    print(pack(enc, mapw, len(map)))
    input("Press enter to continue.\n")
    
    c = ""
    s = ""
    w = 9
    while True:
        c = input_char()
        cls(True)
        if c == "q":
            break
        if c in "10":
            s += c
        if c in "23456789":
            w = int(c)
        print(s)
        print()
        enc = toInt(s)
        print(enc)
        print()
        print(parseMap(enc, w, len(s)))
