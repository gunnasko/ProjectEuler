#Cheated on this
with open('euler18_pyramid.txt') as f:
    content = f.readlines()

row_under = content[-1].rstrip().split(" ")

for i in range(len(content) -2, -1, -1):
    current_row = content[i].rstrip().split(" ")
    print current_row

    print row_under
    max_nums = []
    for j in range(0, len(current_row)):
        current_number = int(current_row[j])
        row_under_number1 = int(row_under[j])
        row_under_number2 = int(row_under[j+1])
        max_nums.append(max(row_under_number1 + current_number, row_under_number2 + current_number))
    row_under = max_nums
    print current_row
