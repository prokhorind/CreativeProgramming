# Перший набір даних
data1 = [10, 20, 30, 40, 50]
mean1 = sum(data1) / len(data1)

# Медіана для першого набору
data1_sorted = sorted(data1)
if len(data1_sorted) % 2 == 1:
    median1 = data1_sorted[len(data1_sorted) // 2]
else:
    median1 = (data1_sorted[len(data1_sorted) // 2 - 1] + data1_sorted[len(data1_sorted) // 2]) / 2

# Мода для першого набору
count1 = {x: data1.count(x) for x in data1}
mode1 = max(count1, key=count1.get)
print(f"Набір 1: Середнє = {mean1}, Медіана = {median1}, Мода = {mode1}")

# Другий набір даних
data2 = [15, 25, 35, 45, 55]
mean2 = sum(data2) / len(data2)

# Медіана для другого набору
data2_sorted = sorted(data2)
if len(data2_sorted) % 2 == 1:
    median2 = data2_sorted[len(data2_sorted) // 2]
else:
    median2 = (data2_sorted[len(data2_sorted) // 2 - 1] + data2_sorted[len(data2_sorted) // 2]) / 2

# Мода для другого набору
count2 = {x: data2.count(x) for x in data2}
mode2 = max(count2, key=count2.get)
print(f"Набір 2: Середнє = {mean2}, Медіана = {median2}, Мода = {mode2}")

# Третій набір даних
data3 = [12, 22, 32, 42, 52]
mean3 = sum(data3) / len(data3)

# Медіана для третього набору
data3_sorted = sorted(data3)
if len(data3_sorted) % 2 == 1:
    median3 = data3_sorted[len(data3_sorted) // 2]
else:
    median3 = (data3_sorted[len(data3_sorted) // 2 - 1] + data3_sorted[len(data3_sorted) // 2]) / 2

# Мода для третього набору
count3 = {x: data3.count(x) for x in data3}
mode3 = max(count3, key=count3.get)
print(f"Набір 3: Середнє = {mean3}, Медіана = {median3}, Мода = {mode3}")
