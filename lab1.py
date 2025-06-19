def reverse (num):

    for i in range(num,0,-1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()

print(reverse.__doc__)
reverse(5)