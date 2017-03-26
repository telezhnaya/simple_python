
def greet(name):
    res = "Привет, " + name
    return res

print(greet("Оля"))
# А можно было в 2 строчки. Примерно так:
# a = greet("Оля")
# print(a)

# Из-за этой строчки программа упадет.
# Функция ждет строку, а мы даем число
# print(greet(1000))


# Бессмысленный и беспощадный пример :)
def do_something_useless(age, weight):
    if age < 10:
        return age * weight
    age = age + 10
    weight = weight + 20
    return age + weight

a = do_something_useless(35, 70)
print(a)


# Во многих языках типы принимаемых и возвращаемых значений
# четко фиксируются. В питоне - нет.
# Без видео неясно, что я тут устроила. Смотрите видео :)

#def greet(name):
#def str greet(str name):

#def do_something_useless(age, weight):
#def int do_something_useless(int age, int weight):


# Забавный пример
def multiply(a, b):
    return a * b

print(multiply(5, "Оля"))
