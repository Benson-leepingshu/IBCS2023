# lisy_exercise.py

# 01. Sum of all elemets in one list
mylist = [1, 2, 3, 4, 5]
answer = 0
# answer = sum(mylist)
for i in range(len(mylist)):
    answer = answer + mylist[i]
print(answer)


# 02. Write a program that removes all duplication from a list
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
answer = []
for i in range(len(mylist)):
    cnt = answer.count(mylist[i])
    if cnt < 1:
        answer.append(mylist[i])
# sulotion 1
answer = list(set(mylist))
# sulotion 2
for val in mylist:
    while mylist.count(val) > 1:
        mylist.remove(val)
# sulotion 3
answer = [x for i, x in enumerate(mylist) if mylist.index(x) == i]
# sulotion 4
answer = [x for i, x in enumerate(mylist) if x not in mylist[i + 1 :]]
print(answer)


# 03. Write a program that finds the intersection of two lists
lista = [0, 0, 1, 12, 5, 83, 246, 568]
listb = [0, 356, 6, 5, 568, 24, 25]
filtered = []
answer = []
n = 0
for i in range(len(lista)):
    n = 0
    for j in range(len(listb)):
        if lista[i] == listb[j] and n < 1:
            filtered.append(lista[i])
            n = n + 1
for i in range(len(listb)):
    n = 0
    for j in range(len(filtered)):
        if listb[i] == filtered[j] and n < 1:
            answer.append(listb[i])
            n = n + 1
print(answer)
# solution 1
answer = [x for x in lista if x in listb]
answer = list(set(answer))
# solution 2
answer = [x for i, x in enumerate(lista) if x in listb and list.index(x) == i]
# 04. Write a program that finds the union of two lists, omitting duplicates
lista = [0, 0, 1, 12, 5, 83, 246, 568]
listb = [0, 356, 6, 5, 568, 24, 25]
filtered = []
answer = list(set(lista + listb))
print(answer)
# 05. Write a program that finds the differences of two lists
lista = [0, 0, 1, 12, 5, 83, 246, 568]
listb = [0, 356, 6, 5, 568, 24, 25]
filtered = []
answer = []
answer1 = []
n = 0
for i in range(len(lista)):
    n = 0
    for j in range(len(listb)):
        if lista[i] == listb[j] and n < 1:
            filtered.append(lista[i])
            n = n + 1
for i in range(len(listb)):
    n = 0
    for j in range(len(filtered)):
        if listb[i] == filtered[j] and n < 1:
            answer1.append(listb[i])
            n = n + 1
for i in range(len(answer1)):
    lista.remove(answer1[i])
    listb.remove(answer1[i])
answer = lista + listb
print(answer)
# solution 1
answer = [x for x in lista if not x in listb]
answer += [x for x in listb if not x in lista]
answer = list(set(answer))
# solution 2
answer = [x for x in (lista + listb) if ((x not in lista) != (x not in listb))]


# 06. Write a program that creates a list containing the frequencies of elements in a list
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
answer = []
answer1 = []
for i in range(len(mylist)):
    cnt = answer1.count(mylist[i])
    if cnt < 1:
        answer1.append(mylist[i])
for i in range(len(answer1)):
    cnt = mylist.count(answer1[i])
    answer.append(cnt)
# solution 1
answer = list(set(mylist))
newlist = []
for val in answer:
    newlist += [(val, answer.count(val))]
# solution 2
freq = [(x, answer.count(x)) for i, x in enumerate(answer) if i == answer.index(x)]
print(answer)
