from string import punctuation

str1 = '/*Jon is @developer & musician!!'

print(str1)

replace_char = '#'
for char in punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement :", str1)
