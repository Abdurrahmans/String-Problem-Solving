str1 = "English = 78 Science = 83 Math = 68 History = 65"
str2 = str1.split()
totalmarks = 0
for s in str2:
    if s.isdigit():
        totalmarks += float(s)
        s += s
per = totalmarks/len(s)
print(per)
