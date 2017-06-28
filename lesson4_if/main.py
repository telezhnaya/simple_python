

salary = 100000

# общий пример, что такое if
if salary < 3000:
    print("Денег очень мало")
elif salary < 20000:
    print("Возможно, денег хватит на еду")
else:
    print("Молодец!")

# пример максимально бессмысленного кода
x = 0
if x > 0:
    print("hello")
elif x > 10:
    print("how are you")

# вводим данные от пользователя 
daytime = input("Введите время суток: ")

if daytime == "утро":
    print("доброе утро!")
    # увеличила зарплату, потому что я могу
    salary = salary + 100
elif daytime == "день":
    print("добрый день!")
elif daytime == "вечер":
    print("добрый вечер!")
else:
    print("здравствуй!")

print("ты отлично выглядишь сегодня!")
