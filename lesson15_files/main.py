

data = open("titanic.csv")
res = []

for line in data:
    line = line.strip().split(";")
    res.append(line)

data.close()

res_file = open("result.csv", "w")
survived = 0
without_age = 0

for line in res[1:]: #  start from 1 because of header line
    s_flag = line[1]
    if int(s_flag):
        survived = survived + 1
        res_file.write(line[3] + "\n")
    age = line[5]
    if not age: #  if age is empty
        without_age = without_age + 1
    #  so we can write "if age:" and do smth useful for age analysis
    #  we could drop all lines where we haven't age,
    #  but there are 177 lines, it's too much to be dropped

res_file.write("Survived only " + str(survived) + "\n")

res_file.close()

print(without_age)

