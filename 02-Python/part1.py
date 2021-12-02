ids = []
with open("../res/02-input.txt", 'r') as file:
    ids = file.readlines()

nTwo = 0
nThree = 0
for id in ids:
    chars = {}
    hasTwo = False
    hasThree = False
    for char in id:
        if(char in chars):
            chars[char] += 1
        else:
            chars[char] = 1
    for char in chars:
        if(chars[char] == 2 and not hasTwo):
            hasTwo = True
            nTwo += 1
        elif(chars[char] == 3 and not hasThree):
            hasThree = True
            nThree += 1

print(nTwo * nThree)
