n = input().strip()
count = sum(1 for digit in n if digit in {'4', '7'})

if count == 0:
    print("NO")
else:
    count_str = str(count)
    is_lucky = all(c in {'4', '7'} for c in count_str)
    if is_lucky:
        print("YES")
    else:
        print("NO")

