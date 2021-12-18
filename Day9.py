import copy
minimPartTwo = [0] * 1000
matrix = [[0 for x in range(100)] for y in range(100)] 

def partTwo(i,j,numbersList,basinIndex):
    global minimPartTwo

    minim = 0
    while (i<len(numbersList)):
        minim = 0
        #print(numbersList[i])
        while (j<len(numbersList[i])):
            if(i == 0 and j>0 and j<len(numbersList[i])-1):
                if (int(numbersList[i][j-1]) < 9 and int(matrix[i][j-1] == 0)):
                        minimPartTwo[basinIndex]+=1
                        matrix[i][j-1] = 1
                        partTwo(i,j-1,numbersList,basinIndex)
                if (int(numbersList[i][j+1]) < 9 and int(matrix[i][j+1] == 0 )):
                        minimPartTwo[basinIndex]+=1
                        matrix[i][j+1] = 1
                        partTwo(i,j+1,numbersList,basinIndex)
                if (int(numbersList[i+1][j]) < 9 and int(matrix[i+1][j] == 0 )):
                        minimPartTwo[basinIndex]+=1
                        matrix[i+1][j] = 1
                        partTwo(i+1,j,numbersList,basinIndex)

            if (i == 0 and j==0):
                if(int(numbersList[i][j+1]) < 9 and int(matrix[i][j+1] == 0)):
                    minimPartTwo[basinIndex]+=1
                    matrix[i][j+1] = 1
                    partTwo(i,j+1,numbersList,basinIndex)
                if(int(numbersList[i+1][j]) < 9 and int(matrix[i+1][j]) == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i+1][j] = 1
                    partTwo(i+1,j,numbersList,basinIndex)

            if (i == 0 and j==len(numbersList[i])-1):

                if(int(numbersList[i][j-1]) < 9 and matrix[i][j-1] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i][j-1] = 1
                    partTwo(i,j-1,numbersList,basinIndex)

                if(int(numbersList[i+1][j]) < 9 and matrix[i+1][j] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i+1][j] = 1
                    partTwo(i+1,j,numbersList,basinIndex)

            if (i > 0 and i < len(numbersList)-1 and j > 0 and j < len(numbersList[i])-1):
                if(int(numbersList[i][j-1]) < 9 and matrix[i][j-1] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i][j-1] = 1
                    partTwo(i,j-1,numbersList,basinIndex)
                if(int(numbersList[i][j+1]) < 9 and matrix[i][j+1] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i][j+1] = 1
                    partTwo(i,j+1,numbersList,basinIndex)
                if(int(numbersList[i+1][j]) < 9 and matrix[i+1][j] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i+1][j] = 1
                    partTwo(i+1,j,numbersList,basinIndex)
                if(int(numbersList[i-1][j]) < 9 and matrix[i-1][j] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i-1][j] = 1
                    partTwo(i-1,j,numbersList,basinIndex)

            if(i == len(numbersList)-1 and j > 0 and j < len(numbersList[i])-1 ):
                if(int(numbersList[i][j-1]) < 9 and matrix[i][j-1] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i][j-1] = 1
                    partTwo(i,j-1,numbersList,basinIndex)

                if(int(numbersList[i][j+1]) < 9 and matrix[i][j+1] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i][j+1] = 1
                    partTwo(i,j+1,numbersList,basinIndex)

                if(int(numbersList[i-1][j]) < 9 and matrix[i-1][j] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i-1][j] = 1
                    partTwo(i-1,j,numbersList,basinIndex)

            if(i == len(numbersList)-1 and j == 0 ):
                if(int(numbersList[i][j+1]) < 9 and matrix[i][j+1] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i][j+1] = 1
                    partTwo(i,j+1,numbersList,basinIndex)
                if(int(numbersList[i-1][j]) < 9 and matrix[i-1][j] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i-1][j] = 1
                    partTwo(i-1,j,numbersList,basinIndex)

            if (i == len(numbersList)-1 and j == len(numbersList[i])-1):
                if(int(numbersList[i][j-1]) < 9 and matrix[i][j-1] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i][j-1] = 1
                    partTwo(i,j-1,numbersList,basinIndex)
                if(int(numbersList[i-1][j]) < 9 and matrix[i-1][j] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i-1][j] = 1
                    partTwo(i-1,j,numbersList,basinIndex)

            if (i > 0 and i < len(numbersList) -1 and j == 0):
                if(int(numbersList[i][j+1]) < 9 and matrix[i][j+1] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i][j+1] = 1
                    partTwo(i,j+1,numbersList,basinIndex)
                if(int(numbersList[i+1][j]) < 9 and matrix[i+1][j] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i+1][j] = 1
                    partTwo(i+1,j,numbersList,basinIndex)
                if(int(numbersList[i-1][j]) < 9 and matrix[i-1][j] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i-1][j] = 1
                    partTwo(i-1,j,numbersList,basinIndex)

            if (i > 0 and i < len(numbersList)-1 and j == len(numbersList[i])-1):
                if(int(numbersList[i][j-1]) < 9 and matrix[i][j-1] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i][j-1] = 1
                    partTwo(i,j-1,numbersList,basinIndex)
                if(int(numbersList[i+1][j]) < 9 and matrix[i+1][j] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i+1][j] = 1
                    partTwo(i+1,j,numbersList,basinIndex)
                if(int(numbersList[i-1][j]) < 9 and matrix[i-1][j] == 0):
                    minimPartTwo[basinIndex]+=1
                    matrix[i-1][j] = 1
                    partTwo(i-1,j,numbersList,basinIndex)
   
            break
        break

def partOne():
    global matrix
    global minimPartTwo

    with open("day9Data.txt", 'r') as f:
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
        numbersTest.pop(len(numbersTest)-1)
        numbersTest.pop(len(numbersTest)-1)
        numbersList.append(numbersTest)

    i = 0
    minim = [[]] * 1
    basinIndex = 0
    while (i<len(numbersList)):
        #print(numbersList[i])
        j=0
        while (j<len(numbersList[i])):
            if(i == 0 and j>0 and j<len(numbersList[i])-1):
                if(numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j] < numbersList[i][j+1]
                   and numbersList[i][j] < numbersList[i+1][j]):
                    minim[0].append(numbersList[i][j])
                    matrix[i][j] = 1
                    basinIndex+=1
                    minimPartTwo[basinIndex]+=1
                    partTwo(i,j,numbersList,basinIndex)
            if (i == 0 and j==0):
                if(numbersList[i][j] < numbersList[i][j+1] and numbersList[i][j] < numbersList[i+1][j]):
                    minim[0].append(numbersList[i][j])
                    matrix[i][j] = 1
                    basinIndex+=1
                    minimPartTwo[basinIndex]+=1
                    partTwo(i,j,numbersList,basinIndex)
            if (i == 0 and j==len(numbersList[i])-1):
                if(numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j] < numbersList[i+1][j]):
                    minim[0].append(numbersList[i][j])
                    matrix[i][j] = 1
                    basinIndex+=1
                    minimPartTwo[basinIndex]+=1
                    partTwo(i,j,numbersList,basinIndex)
            if (i > 0 and i < len(numbersList)-1 and j > 0 and j < len(numbersList[i])-1):
                if (numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j]<numbersList[i][j+1]
                    and numbersList[i][j]<numbersList[i+1][j]and numbersList[i][j]<numbersList[i-1][j]):
                    minim[0].append(numbersList[i][j])
                    matrix[i][j] = 1
                    basinIndex+=1
                    minimPartTwo[basinIndex]+=1
                    partTwo(i,j,numbersList,basinIndex)
            if(i == len(numbersList)-1 and j > 0 and j < len(numbersList[i])-1 ):
                if(numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j] < numbersList[i][j+1] and numbersList[i][j] < numbersList[i-1][j]):
                    minim[0].append(numbersList[i][j])
                    matrix[i][j] = 1
                    basinIndex+=1
                    minimPartTwo[basinIndex]+=1
                    partTwo(i,j,numbersList,basinIndex)
            if(i == len(numbersList)-1 and j == 0 ):
                if(numbersList[i][j] < numbersList[i][j+1] and numbersList[i][j] < numbersList[i-1][j]):
                    minim[0].append(numbersList[i][j])
                    matrix[i][j] = 1
                    basinIndex+=1
                    minimPartTwo[basinIndex]+=1
                    partTwo(i,j,numbersList,basinIndex)
            if (i == len(numbersList)-1 and j == len(numbersList[i])-1):
                if(numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j] < numbersList[i-1][j]):
                    minim[0].append(numbersList[i][j])
                    matrix[i][j] = 1
                    basinIndex+=1
                    minimPartTwo[basinIndex]+=1
                    partTwo(i,j,numbersList,basinIndex)
            if (i > 0 and i < len(numbersList) -1 and j == 0):
                if(numbersList[i][j] < numbersList[i][j+1] and numbersList[i][j] < numbersList[i-1][j]
                   and numbersList[i][j] < numbersList[i+1][j]):
                    minim[0].append(numbersList[i][j])
                    matrix[i][j] = 1
                    basinIndex+=1
                    minimPartTwo[basinIndex]+=1
                    partTwo(i,j,numbersList,basinIndex)
            if (i > 0 and i < len(numbersList)-1 and j == len(numbersList[i])-1):
                if(numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j] < numbersList[i-1][j]
                   and numbersList[i][j] < numbersList[i+1][j]):
                    minim[0].append(numbersList[i][j])
                    matrix[i][j] = 1
                    basinIndex+=1
                    minimPartTwo[basinIndex]+=1
                    partTwo(i,j,numbersList,basinIndex)
   
            j+=1
        i+=1
    totalSum = 0
    i = 0
    while (i < len(minim[0])):
        totalSum = totalSum + int(minim[0][i]) +1
        i+=1
    print(minim)
    print(totalSum)
    print("Part two: " + "\n")
    answear = copy.deepcopy(minimPartTwo)
    answear = sorted(answear, reverse = True)
    print(answear[0]*answear[1]*answear[2])
    
