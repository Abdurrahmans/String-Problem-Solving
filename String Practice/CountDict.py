str1 = "Apple"
countDict = dict()
for char in str1:
    count = str1.count(char)
    countDict[char] = count
print(countDict)
