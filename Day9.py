
def partOne():

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
    while (i<len(numbersList)):
        #print(numbersList[i])
        j=0
        while (j<len(numbersList[i])):
            if(i == 0 and j>0 and j<len(numbersList[i])-1):
                if(numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j] < numbersList[i][j+1]
                   and numbersList[i][j] < numbersList[i+1][j]):
                    minim[0].append(numbersList[i][j])
                    #print(numbersList[i][j])
            if (i == 0 and j==0):
                if(numbersList[i][j] < numbersList[i][j+1] and numbersList[i][j] < numbersList[i+1][j]):
                    minim[0].append(numbersList[i][j])
            if (i == 0 and j==len(numbersList[i])-1):
                if(numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j] < numbersList[i+1][j]):
                    minim[0].append(numbersList[i][j])
            if (i > 0 and i < len(numbersList)-1 and j > 0 and j < len(numbersList[i])-1):
                if (numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j]<numbersList[i][j+1]
                    and numbersList[i][j]<numbersList[i+1][j]and numbersList[i][j]<numbersList[i-1][j]):
                    minim[0].append(numbersList[i][j])
            if(i == len(numbersList)-1 and j > 0 and j < len(numbersList[i])-1 ):
                if(numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j] < numbersList[i][j+1] and numbersList[i][j] < numbersList[i-1][j]):
                    minim[0].append(numbersList[i][j])
            if(i == len(numbersList)-1 and j == 0 ):
                if(numbersList[i][j] < numbersList[i][j+1] and numbersList[i][j] < numbersList[i-1][j]):
                    minim[0].append(numbersList[i][j])
            if (i == len(numbersList)-1 and j == len(numbersList[i])-1):
                if(numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j] < numbersList[i-1][j]):
                    minim[0].append(numbersList[i][j])
            if (i > 0 and i < len(numbersList) -1 and j == 0):
                if(numbersList[i][j] < numbersList[i][j+1] and numbersList[i][j] < numbersList[i-1][j]
                   and numbersList[i][j] < numbersList[i+1][j]):
                    minim[0].append(numbersList[i][j])
            if (i > 0 and i < len(numbersList)-1 and j == len(numbersList[i])-1):
                if(numbersList[i][j] < numbersList[i][j-1] and numbersList[i][j] < numbersList[i-1][j]
                   and numbersList[i][j] < numbersList[i+1][j]):
                    minim[0].append(numbersList[i][j])
   
            j+=1
        i+=1
    totalSum = 0
    i = 0
    while (i < len(minim[0])):
        totalSum = totalSum + int(minim[0][i]) +1
        i+=1
    print(minim)
    print(totalSum)