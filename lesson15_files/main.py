

data = open("titanic.csv")
res = []

for line in data:
    line = line.strip().split(";")
    res.append(line)

data.close()

res_file = open("result.csv", "w")
survived = 0

for line in res[1:]: #  start from 1 because of header line
    s_flag = line[1]
    if int(s_flag):
        survived = survived + 1
        res_file.write(line[3] + "\n")

res_file.write("Survived only " + str(survived) + "\n")

res_file.close()
