count = 0
total = 0
grade_list = []

while count < 5:
    grades = int(input('enter grades'))
    grade_list.append(grades)
    count += 1

total = sum(grade_list)
avg = total/len(grade_list)
largest = max(grade_list)
smallest = min(grade_list)
print('avg>>>>>',avg)
print(len(grade_list))
print("largest--->", largest)
print("smallest---->",smallest)
if total >= 60:
    print('passed')
elif total == 50 < 60:
    print('watchlist')
elif total < 50:
    print("remedial action required")
else:
    print('fail')
