file_path = '1.txt'
with open(file_path, 'r') as file:
    lines = [line.split() for line in file]
# print(lines)

left_tuple, right_tuple = zip(*lines)

# print(left_tuple)
# print(right_tuple)
left_list = list(left_tuple)
right_list = list(right_tuple)

left_list.sort()
right_list.sort()

# print(left_list)
# print(right_list)

total_distance = 0
similarity_score = 0

for i in range(len(left_list)):
    # print(left_list[i], right_list[i])
    total_distance += abs(int(right_list[i]) - int(left_list[i]))
    similarity_score += (int(left_list[i]) * right_list.count(left_list[i]))

print(total_distance)
print(similarity_score)
