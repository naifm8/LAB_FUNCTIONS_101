def reverse(num):
    result = ""
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result += "\n"
    return result

print(reverse.__doc__)

res = reverse(5)
print(res)