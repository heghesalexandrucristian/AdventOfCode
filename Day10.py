

def partTwo(ordineParanteze, partTwoSumList):
    totalScore = 0

    i = len(ordineParanteze)-1
    while (i >= 0):
        if(ordineParanteze[i] == "("):
            totalScore = (totalScore * 5) + 1
        elif (ordineParanteze[i] == "["):
            totalScore = (totalScore * 5) + 2
        elif (ordineParanteze[i] == "{"):
            totalScore = (totalScore * 5) + 3
        elif (ordineParanteze[i] == "<"):
            totalScore = (totalScore * 5) + 4
        i-=1
    partTwoSumList.append(totalScore)

def partOne():

    with open("day10Data.txt", 'r') as f:
        data = f.readlines() 
    numbers = []
    numbersList = []
    for raw_line in data:
        split_line = raw_line.strip().split("/n") 
        nums_ls = [str(x) for x in split_line] 
        numbers.append(nums_ls)

        numbersTest = [str(a) for a in str(nums_ls)]
        numbersTest.pop(0)
        numbersTest.pop(0)
        numbersTest.pop(len(numbersTest) - 1)
        numbersTest.pop(len(numbersTest) - 1)
        numbersList.append(numbersTest)

    paranteze = []
    parantezeDrepte = []
    acolade = []
    sageti = []

    ordineParanteze = []
    #incomplete lines
    lineIncomplete = True
    partTwoSumList = []
    i = 0
    while (i < len(numbersList)):
        j = 0
        ordineParanteze = []
        lineIncomplete = True
        while (j < len(numbersList[i])):
            if (numbersList[i][j] == "(" or numbersList[i][j] == "[" or numbersList[i][j] == "{" or numbersList[i][j] == "<"):
                ordineParanteze.append(numbersList[i][j])
            if (numbersList[i][j] == ")"):
                if (ordineParanteze[len(ordineParanteze) - 1] != "("):
                    print("coruption found")
                    lineIncomplete = False
                    paranteze.append(numbersList[i][j])
                    j+=1
                    break
                else:
                    ordineParanteze.pop(len(ordineParanteze) - 1)
            elif (numbersList[i][j] == "]"):
                if (ordineParanteze[len(ordineParanteze) - 1] != "["):
                    print("coruption found")
                    lineIncomplete = False
                    parantezeDrepte.append(numbersList[i][j])
                    j+=1
                    break
                else:
                    ordineParanteze.pop(len(ordineParanteze) - 1)
            elif (numbersList[i][j] == "}"):
                if (ordineParanteze[len(ordineParanteze) - 1] != "{"):
                    print("coruption found")
                    lineIncomplete = False
                    acolade.append(numbersList[i][j])
                    j+=1
                    break
                else:
                    ordineParanteze.pop(len(ordineParanteze) - 1)
            elif (numbersList[i][j] == ">"):
                if (ordineParanteze[len(ordineParanteze) - 1] != "<"):
                    print("coruption found")
                    lineIncomplete = False
                    sageti.append(numbersList[i][j])
                    j+=1
                    break
                else:
                    ordineParanteze.pop(len(ordineParanteze) - 1)
            j+=1
        if (lineIncomplete == True):
            partTwo(ordineParanteze, partTwoSumList)
        i+=1

    #print(paranteze)
    #print(parantezeDrepte)
    #print(acolade)
    #print(sageti)

    total = len(paranteze) * 3 + len(parantezeDrepte) * 57 + len(acolade) * 1197 + len(sageti) * 25137
    print(total)
    partTwoSumList = sorted(partTwoSumList, reverse = True)
    print(partTwoSumList[int(len(partTwoSumList)/2)])
