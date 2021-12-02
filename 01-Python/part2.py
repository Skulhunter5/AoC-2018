changes = []
with open("../res/01-input.txt", 'r') as file:
    changes = list(map(int, file.readlines()))

found = False
frequency = 0
knownFrequencies = [0]
while not found:
    for change in changes:
        frequency += change
        if(frequency in knownFrequencies):
            found = True
            break
        else:
            knownFrequencies.append(frequency)

print(frequency)
