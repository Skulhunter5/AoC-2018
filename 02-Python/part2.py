ids = []
with open("../res/02-input.txt", 'r') as file:
    ids = file.readlines()

def diff(a, b):
    off = -1
    for i in range(len(a)):
        if(not (a[i] == b[i])):
            if(off == -1):
                off = i
            else:
                return -1
    return off

for i in range(len(ids)):
    for j in range(i+1, len(ids)):
        off = diff(ids[i], ids[j])
        if(not off == -1):
            print(ids[i][:off] + ids[i][off+1:])
            exit()
