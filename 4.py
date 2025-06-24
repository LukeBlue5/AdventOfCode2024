file_path = '4.txt'
with open(file_path, 'r') as file:
    word_search = [line for line in file.readlines()]

times = 0
rows = len(word_search)
columns = (len(word_search[0]) - 1)

for j in range(rows):
    row = str(word_search[j])[:columns]
    for i in range(columns):
        if row[i] == "X":
            if i > 2:
                if row[i - 1] == "M" and row[i - 2] == "A" and row[i - 3] == "S":
                    times += 1
                if j > 2:
                    if str(word_search[j - 1])[:columns][i - 1] == "M" and str(word_search[j - 2])[:columns][i - 2] == "A" and str(word_search[j - 3])[:columns][i - 3] == "S":
                        times += 1

            if i + 3 < columns:
                if row[i + 1] == "M" and row[i + 2] == "A" and row[i + 3] == "S":
                    times += 1

                if j + 3 < rows:
                    if str(word_search[j + 1])[:columns][i + 1] == "M" and str(word_search[j + 2])[:columns][i + 2] == "A" and str(word_search[j + 3])[:columns][i + 3] == "S":
                        times += 1

            if j > 2:
                if str(word_search[j - 1])[:columns][i] == "M" and str(word_search[j - 2])[:columns][i] == "A" and str(word_search[j - 3])[:columns][i] == "S":
                    times += 1

                if i + 3 < columns:
                    if str(word_search[j - 1])[:columns][i + 1] == "M" and str(word_search[j - 2])[:columns][i + 2] == "A" and str(word_search[j - 3])[:columns][i + 3] == "S":
                        times += 1

            if j + 3 < rows:
                if str(word_search[j + 1])[:columns][i] == "M" and str(word_search[j + 2])[:columns][i] == "A" and str(word_search[j + 3])[:columns][i] == "S":
                    times += 1

                if i > 2:
                    if str(word_search[j + 1])[:columns][i - 1] == "M" and str(word_search[j + 2])[:columns][i - 2] == "A" and str(word_search[j + 3])[:columns][i - 3] == "S":
                        times += 1
print(times)

times = 0
rows = len(word_search)
columns = (len(word_search[0]) - 1)

for j in range(rows):
    row = str(word_search[j])[:columns]
    for i in range(columns):
        if row[i] == "A":
            if i > 0 and j > 0 and i + 1 < columns and j + 1 < rows:
                if str(word_search[j - 1])[:columns][i - 1] == "M" and str(word_search[j - 1])[:columns][i + 1] == "M"\
                        and str(word_search[j + 1])[:columns][i + 1] == "S" and str(word_search[j + 1])[:columns][i - 1] == "S":
                    times += 1

                if str(word_search[j - 1])[:columns][i - 1] == "S" and str(word_search[j - 1])[:columns][i + 1] == "M"\
                        and str(word_search[j + 1])[:columns][i + 1] == "M" and str(word_search[j + 1])[:columns][i - 1] == "S":
                    times += 1

                if str(word_search[j - 1])[:columns][i - 1] == "M" and str(word_search[j - 1])[:columns][i + 1] == "S"\
                        and str(word_search[j + 1])[:columns][i + 1] == "S" and str(word_search[j + 1])[:columns][i - 1] == "M":
                    times += 1

                if str(word_search[j - 1])[:columns][i - 1] == "S" and str(word_search[j - 1])[:columns][i + 1] == "S"\
                        and str(word_search[j + 1])[:columns][i + 1] == "M" and str(word_search[j + 1])[:columns][i - 1] == "M":
                    times += 1
print(times)