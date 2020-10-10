

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
map =  "001100110011001100"
mapw = 6


print("Map: " + map)
enc = toInt(map)
print("Encoded: " + str(enc))
print("Decoded raw: " + str(toBin(enc, len(map))))
dec = parseMap(enc, mapw-1, len(map))
print("Decoded map: \n" + str(dec))

print()
print(pack(enc, mapw, len(map)))