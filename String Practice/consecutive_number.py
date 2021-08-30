m = int(input('Enter the first number:'))
n = int(input("Enter the second number:"))
sum = count = 0
counter = 1
for i in range(m, n+1):
    for j in range(1, i + 1):
        temp = sum + j
        if temp < i:
            temp += j
            if temp == i:
                count += 1
                break
            else:
                counter += 1
                j = counter
                temp = 0
    counter = 0
print(count)