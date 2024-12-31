correctAnswers = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D',
                   'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']

file = open("student.txt")
answers = [line.strip() for line in file.readlines()]

file.close()

corcounter = 0
incorcounter = []

if len(answers) != len(correctAnswers):
    print("some error")
else:
    corcounter = 0
    incorcounter = []

    for i in range (len(correctAnswers)):
        if answers == correctAnswers:
            corcounter +=1
        else:
            incorcounter.append(i+1)

print(corcounter)
print(len(incorcounter))
print(incorcounter)

if corcounter >= 15:
    print("perfect")
else:
    print("lose")