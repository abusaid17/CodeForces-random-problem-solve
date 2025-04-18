number = int(input())
color = input()
count = 0
# loop through the string
# and compare each character with the next one
# if they are the same, increment the count
# and print the count
for i in range(number -1 ): 
    if color[i] == color[i + 1]:
        count += 1
print(count)






