number = int(input())
number_of_drink = list(map(int, input().split()))

average = sum(number_of_drink) / number
# print(average)
print("{0:.12f}".format(average))
