# The code calculates the total cost of bananas and determines how much money the soldier needs to borrow.
k, n, w = map(int, input().split())
total_cost = k * w * (w + 1) // 2
borrow = max(0, total_cost - n)
print(borrow) 
