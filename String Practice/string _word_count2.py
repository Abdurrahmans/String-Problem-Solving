string = "Python is awesome, isn't it?"
substring = "is"
count = string.count(substring)
print('The count is:', count)

s = 'bangladesh country is a beautiful is country country'
s1 = 'country'
s2 = s.split()
count = 0
for i in s2:
    if i == s1:
        count += 1
print('The substring count is:', count)