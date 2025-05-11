n = int(input())
numbers = input().split()  # Split into ["0", "0", "1"]

for num in numbers:
    difficulty = "EASY"
    temp = int(num)
    if temp == 1:
        difficulty = "HARD"
        break


print(difficulty)
