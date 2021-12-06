import copy


def partOne():

    with open("day6DataSmall.txt", 'r') as f:
        data = f.readlines() 

    for raw_line in data:
        split_line = raw_line.strip().split(" ") 
        nums_ls = [str(x) for x in split_line] 
        numbers = nums_ls[0].split(",")

    print(numbers)
    i = 0
    while (i < len(numbers)):
        numbers[i] = int(numbers[i])
        i+=1
    i = 0
    j = 0
    length = len(numbers)
    while (i < 80):
        j=0
        length = len(numbers)
        print(len(numbers))
        while (j < length):
            if(numbers[j] == 0):
                numbers[j] = 6
                numbers.append(8)
            else:
                numbers[j] = numbers[j]-1
            
            j+=1
        i+=1
    print(len(numbers))

def partTwo():
    with open("day6Data.txt", 'r') as f:
        data = f.readlines() 

    for raw_line in data:
        split_line = raw_line.strip().split(" ") 
        nums_ls = [str(x) for x in split_line] 
        numbers = nums_ls[0].split(",")

    i = 0
    totalNr = [0]*11
    while (i < len(numbers)):
        numbers[i] = int(numbers[i])
        totalNr[numbers[i]]+=1

        i+=1
    numbers2 = [0] * 11
    i = 0
    while (i < len(numbers)):
        if (numbers2[numbers[i]] == 0):
            numbers2[numbers[i]] = numbers[i]
        i+=1

    
    i = 0
    j = 0
    k = 0
    numbers = copy.deepcopy(numbers2)
    print(numbers)
    totalnr6 = 0
    totalnr8 = 0
    while (i < 256):
        j = 0
        length = len(numbers)-2
        print(len(numbers))

        if (totalNr[9] > 0):
            numbers[6] = 6
            totalNr[6]+=totalnr6
            totalNr[9]-=totalnr6
        if (totalNr[10]>0):
            numbers[8] = 8
            totalNr[8]+=totalnr8
            totalNr[10]-=totalnr8
            

        while (j < length):
            if(j == 0 and totalNr[0] > 0):
                totalNr[9]+=totalNr[j]
                numbers[9] = 6
                totalnr6 = totalNr[j]
                totalNr[10]+=totalNr[0]
                totalnr8 = totalNr[j]
                totalNr[0] = 0
                numbers[10] = 8
                skip = True

                
            if (totalNr[j] > 0):

                numbers[j-1] = numbers[j] - 1
                totalNr[j-1] += totalNr[j]
                numbers[j] = 0
                totalNr[j]  = 0
                
            
            j+=1
        i+=1
    

    print(totalNr)
    print(sum(totalNr))




  
   


