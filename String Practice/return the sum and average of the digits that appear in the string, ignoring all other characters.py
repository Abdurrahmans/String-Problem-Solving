import re

str1 = "English = 78 Science = 83 Math = 68 History = 65"

mark_list = [int(num) for num in re.findall(r'\b\d+\b', str1)]

total_mark = 0
for mark in mark_list:
    total_mark += mark

percentage = total_mark/len(mark_list)

print("Total Marks is:", total_mark, "Percentage is ", percentage)
