world = input().strip()

upperCount = 0
lowerCount = 0
for letter in world:
    if letter.islower():
        lowerCount += 1
    else:
        upperCount += 1
if (lowerCount >= upperCount):
    print(world.lower())
else:
    print(world.upper())
