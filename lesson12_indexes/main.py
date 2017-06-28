
ages = [17, 13, 45, 7, 3, 18, 27, 36, 23]
print(ages)

for i, age in enumerate(ages):
    ages[i] = ages[i] + 10

print(ages)

print("Массив начинается с", ages[0]) 
#print(ages[9]) # - тут получим ошибку - вышли за край массива
print("В конце массива", ages[-1])
