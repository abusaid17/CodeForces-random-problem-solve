numbers = list(map(int, input().split("+")))
count = 0
numbers.sort()
for num in numbers:
    count += 1
    if count == len(numbers):
        print(f'{num}', end="")
    else:
        print(f'{num}+', end="")
