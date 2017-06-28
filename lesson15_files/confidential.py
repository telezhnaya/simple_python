

data = open("titanic.csv")
res = []

for line in data:
    line = line.strip().split(";")
    res.append(line)

data.close()

survived = 0
young = 0
young_survived = 0
old = 0
old_survived = 0
girls = 0
girls_survived = 0

for line in res[1:]: #  start from 1 because of header line
    surv = int(line[1])
    sex = 0 if line[4] == "male" else 1 #  checked, no missing values
    age = float(line[5]) if line[5] else None #  here is a man with age 28.5

    if surv:
        survived += 1

        if age:
            if age < 14:
                young_survived += 1
            else:
                old_survived += 1
        if sex:
            girls_survived += 1
    if age:
        if age < 14:
            young += 1
        else:
            old += 1
    if sex:
        girls += 1

print("Stats: ")
print("Total: ", len(res) - 1, ", survived: ", survived)
print("Young people were ", young, ", survived ", young_survived)
print("People older than 14 were ", old, ", survived ", old_survived)
print("Girls were ", girls, ", survived ", girls_survived)



# Stats:
# Total:  891 , survived:  342
# Young people were  71 , survived  42
# People older than 14 were  643 , survived  248
# Girls were  314 , survived  233

# It's better to be a girl than to be a child
