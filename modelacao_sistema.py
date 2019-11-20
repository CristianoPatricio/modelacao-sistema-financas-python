import random
import datetime

# open file
f = open("log_file.txt","w")

dateNow = datetime.datetime.now()

f.write("[Date] %s\r\n" % dateNow.strftime("%c"))

# generate a number between 120 and 150
nClientes = random.randrange(120,150)
# write nClientes in log_file
f.write("[nClientes]: %d\n" % nClientes)

def getNumbersBetween0And1(seed, nClientes):
    # list to save the numbers
    listNum01 = []

     # set seed value
    random.seed(seed)
    for x in range (1,nClientes):
        # generate a rand number between 0 and 1
        num = random.random()
        listNum01.append(num)
        
    return listNum01

def getClientesPrioritarios(listNumbers):
    # list to save the arrival times for priorities
    listPrioritarios = []

    for num in listNumbers:
        if num >= 0 and num <= 0.2:
            listPrioritarios.append(random.randrange(0,nClientes-1))
    
    return listPrioritarios

def getTemposChegada(listNumbers):
    # list to save the values for the interval 9h -> 11h
    listInt1 = []
    # list to save the values for the interval 11h -> 13h
    listInt2 = []
    # list to save the values for the interval 13h -> 15h
    listInt3 = []
    # list to save the values for the interval 15h -> 17h
    listInt4 = []

    for num in listNumbers:
        # categorize the generated number according to the intervalss
        if num >= 0 and num <= 0.1:
            # Generate a rand number between 0 and 7200
            listInt1.append(random.randrange(0,7200))
        elif num >= 0.11 and num <= 0.35:
            # Generate a rand number between 7201 and 14400
            listInt2.append(random.randrange(7201,14400))
        elif num >= 0.36 and num <= 0.80:
            # Generate a rand number between 14401 and 21600
            listInt3.append(random.randrange(14401,21600))
        else:
           # Generate a rand number between 21601 and 28800
            listInt4.append(random.randrange(21601,28800))

    return listInt1 + listInt2 + listInt3 + listInt4 

# list contains random numbers between 0 and 1
listNumbersBetween0And1 = getNumbersBetween0And1(12,nClientes)
# list contains arivals times
result = getTemposChegada(listNumbersBetween0And1)

# list contains random numbers between 0 and 1 (Prioridades)
listNumbersBetween0And1Prioridades = getNumbersBetween0And1(12,nClientes)
# list contains clientes prioritários
answer = getClientesPrioritarios(listNumbersBetween0And1Prioridades)

prioritarios = []
for i in range(len(answer)):
    prioritarios.append(result[answer[i]])

#list contains clientes gerais
gerais = list(set(result) - set(prioritarios))

result.sort()
f.write("\r")
f.write("[List of Arrival Times]\n")
for i in range(len(result)):
    if (i % 10 == 0 and i != 0):
        f.write("\n")
    f.write("%s " % result[i])

answer.sort()
f.write("\r\n")
f.write("[List of Priority Customers]\n")
for i in range(len(answer)):
    if (i % 10 == 0 and i != 0):
        f.write("\n")
    f.write("%s " % result[answer[i]])

gerais.sort()
f.write("\r\n")
f.write("[List of Geral Customers]\n")
for i in range(len(gerais)):
    if (i % 10 == 0 and i != 0):
        f.write("\n")
    f.write("%s " % gerais[i])

# close log file
f.close()