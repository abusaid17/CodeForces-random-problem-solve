t = int(input()) 
for _ in range(t):
    ticket = input().strip()
    if sum(int(d) for d in ticket[:3]) == sum(int(d) for d in ticket[3:]):
        print("YES")
    else:
        print("NO")



