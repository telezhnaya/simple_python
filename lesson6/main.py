
ages = [17, 13, 45, 7, 3, 18, 27, 36, 23]

# Хотим посчитать средний возраст
res = 0
for age in ages:
    res = res + age
    # print("Текущее значение результата: ", res)

res = res / len(ages)
print("Средний возраст:", res)

# Хотим учитывать только взрослых
adult_res = 0  # сумма
num_of_adults = 0  # количество

for age in ages:
    if age >= 18:
        num_of_adults = num_of_adults + 1
        adult_res = adult_res + age
    # print("Текущее значение результата: ", adult_res)

adult_res = adult_res / num_of_adults
print("Средний возраст среди совершеннолетних:", adult_res)
