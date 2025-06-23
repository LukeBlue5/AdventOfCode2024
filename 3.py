import re
file_path = '3.txt'
with open(file_path, 'r') as file:
    memory = [line.split("mul(") for line in file]

print(memory)

total = 0
for array in memory:
    for element in array:
        # print(element)
        if element.find(")") != -1:
            index = element.index(")")  # Find the index of the first ')'
            two_nums = element[:index]  # Slice the string up to the index)

            pattern = r'^(\d+)$'
            if two_nums.find(",") != -1:
                # print(two_nums)
                num1 = two_nums.split(",", 1)[0]
                num2 = two_nums.split(",", 1)[1]
                if re.match(pattern, num1) and re.match(pattern, num2):
                    # print(num1 + "," + num2)
                    total += int(num1) * int(num2)
print(total)

do = True
total = 0
for array in memory:
    for element in array:
        # print(element)
        if do and element.find(")") != -1:
            index = element.index(")")  # Find the index of the first ')'
            two_nums = element[:index]  # Slice the string up to the index)

            pattern = r'^(\d+)$'
            if two_nums.find(",") != -1:
                # print(two_nums)
                num1 = two_nums.split(",", 1)[0]
                num2 = two_nums.split(",", 1)[1]
                if re.match(pattern, num1) and re.match(pattern, num2):
                    # print(num1 + "," + num2)
                    total += int(num1) * int(num2)
        if element.find("don't()") != -1:
            do = False
        elif element.find("do()") != -1:
            do = True
print(total)
