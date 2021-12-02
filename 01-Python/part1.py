changes = []
with open("../res/01-input.txt", 'r') as file:
    changes = list(map(int, file.readlines()))

frequency = 0
for change in changes:
    frequency += change

print(frequency)
