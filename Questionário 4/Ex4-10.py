n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 == n2 == n3: 
    print(1)
elif n1 != n2 != n3:
    print(2)
elif n1 == n2 or n1 == n3 or n2 == n3:
    print(3)