test_case = int(input())
for number in range(test_case):
    a,b,c = map(int, input().split())
    if a+b == c:
        print("YES")
    elif a+c == b:
        print("YES")
    elif b+c == a:
        print("YES")    
    else:
        print("NO")    
