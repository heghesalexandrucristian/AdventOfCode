import numpy as np


def partOne():
    
    f = open("day4Numbers.txt", "r")
    lines = f.read()
    arrayNumbers = []
    number = ""
    i= 0
    while (i < len(lines)):
        if (lines[i] == ","):
            i+=1
            continue
        try:
            if (lines[i+1] == ","):
                if (number == ""):
                    number = lines[i]
                arrayNumbers.append(number)
                number = ""
                i+=1
            else:
                number = lines[i]
                while (True):
                    if (lines[i+1] != ","):
                            number += lines[i+1]
                            i+=1
                    else:
                        break
                    
        except:
            arrayNumbers.append(number)
            i+=1

    f = open("day4Boards.txt", "r")
    lines = f.read()

    rows, cols = (5, 5)
 
    # method 2a
    arrayMatrix = [[0]*cols]*rows

    rowIndex = 0
    colIndex = 0
    number = ""
    i= 0

    with open("day4Boards.txt", 'r') as f:
        data = f.readlines() 
    
    matrixList = []
    cleaned_matrix = [] 
    for raw_line in data:
        split_line = raw_line.strip().split(" ") 
        nums_ls = [str(x) for x in split_line] 
        i= 0 
        while (i < len(nums_ls)):
            if (nums_ls[i] == ''):
                nums_ls.pop(i)
            i+=1

        if (len(nums_ls) == 0):
            matrixList.append(cleaned_matrix.copy())
            cleaned_matrix.clear()
            continue
        
        cleaned_matrix.append(nums_ls)
    matrixList.append(cleaned_matrix.copy())
    print(matrixList[0])


    i = 0
    numberIndex = 0
    j = 0
    indexMatrix = 0
    winningMatrix = 0
    lastNumber = 0
    cleaned_matrix = matrixList[0]
    i = 0
    winningOrder = [0] * len(matrixList)
    winningOrderNumber = 0
    tablesThatWon = len(matrixList)
    while (j < len(arrayNumbers)):
        i = 0
        cleaned_matrix = matrixList[0]
        indexMatrix = 0
        while (i < len(cleaned_matrix)):
                
                x = 0
                while (x < 5):
                   if (cleaned_matrix[i][x] == arrayNumbers[numberIndex]):
                            print (cleaned_matrix[i][x],  arrayNumbers[numberIndex])
                            cleaned_matrix[i][x] = cleaned_matrix[i][x].replace(str(cleaned_matrix[i][x]),"-100")
                            matrixList[indexMatrix] = cleaned_matrix.copy()
                            lastNumber = arrayNumbers[numberIndex]


                            """
                            if (int(cleaned_matrix[i][0]) + int(cleaned_matrix[i][1]) + int(cleaned_matrix[i][2]) + int(cleaned_matrix[i][3]) + int(cleaned_matrix[i][4]) == -500):
                                        j = len(arrayNumbers)
                                        #print("A castigat: "+str(indexMatrix))
                                        winningMatrix = indexMatrix
                                        #print(lastNumber)
                                        i = len(cleaned_matrix)  
                                        break

                            if (int(cleaned_matrix[0][x]) + int(cleaned_matrix[1][x]) + int(cleaned_matrix[2][x]) + int(cleaned_matrix[3][x]) + int(cleaned_matrix[4][x]) == -500):
                                            j = len(arrayNumbers)
                                            #print("A castigat: "+str(indexMatrix))
                                            winningMatrix = indexMatrix
                                            #print(lastNumber)
                                            i = len(cleaned_matrix)
                                            break
                            """
                            if (int(cleaned_matrix[i][0]) + int(cleaned_matrix[i][1]) + int(cleaned_matrix[i][2]) + int(cleaned_matrix[i][3]) + int(cleaned_matrix[i][4]) == -500):
                                        if (winningOrder[indexMatrix] == 0):
                                            winningOrderNumber+=1
                                            winningOrder[indexMatrix] = winningOrderNumber
                                            tablesThatWon-=1

                            if (int(cleaned_matrix[0][x]) + int(cleaned_matrix[1][x]) + int(cleaned_matrix[2][x]) + int(cleaned_matrix[3][x]) + int(cleaned_matrix[4][x]) == -500):

                                            if (winningOrder[indexMatrix] == 0):
                                                winningOrderNumber+=1
                                                winningOrder[indexMatrix] = winningOrderNumber
                                                tablesThatWon-=1

                            if (tablesThatWon == 0):
                                j = len(arrayNumbers)
                           
                                i = len(cleaned_matrix)
                                break



                            

                   x+=1
                i+=1
                if (i == 5):
                    if(indexMatrix < len(matrixList)-1):
                        i = 0
                  
                        print(indexMatrix)
                        print(len(matrixList))
                        indexMatrix+=1
                       
                        cleaned_matrix = matrixList[indexMatrix].copy()
        numberIndex+=1
        j+=1
    
    i = 0
    j = 0
    sum = 0
    print(winningMatrix)
    matrix = matrixList[winningMatrix]
    while (i < len(matrixList[winningMatrix])):

        while (j < 5):

            if(int(matrix[i][j]) < 0):
                print
            else:
                sum+= int(matrix[i][j])

            j+=1
        j = 0
        i+=1
    
    print("winning Order:"+str(winningOrder))
    i = 0
    print()
    while (i < len(matrix)):
        print(str(matrix[i]) + "\n")
        i+=1

    ## part 2 ###

    max = 0
    i = 0
    winningMatrixPartTwo = 0
    while (i < len(winningOrder)):
        if(winningOrder[i] > max):
            max = winningOrder[i]
            winningMatrixPartTwo = i

        i+=1


    i = 0
    j = 0
    sum2 = 0
    matrix = matrixList[winningMatrixPartTwo]
    while (i < len(matrixList[winningMatrix])):

        while (j < 5):

            if(int(matrix[i][j]) < 0):
                print
            else:
                sum2+= int(matrix[i][j])

            j+=1
        j = 0
        i+=1
    
    print(lastNumber)
    print("raspunsul este este: "+str(int(sum)*int(lastNumber)))
    print("winning matrix part two: " + str(winningMatrixPartTwo) + "cu suma" + str(int(sum2)*int(lastNumber)))
   