

def partOne():
    startPointsX = []
    startPointsY = []
    endPointsX = []
    endPointsY = []
    numbers = []
    maxnumber = 0
    with open("day5Data.txt", 'r') as f:
        data = f.readlines() 

    for raw_line in data:
        split_line = raw_line.strip().split(" ") 
        nums_ls = [str(x) for x in split_line] 
        numbers = nums_ls[0].split(",")
        
        startPointsX.append( numbers[0])
        startPointsY.append( numbers [1])

        if (int(numbers[0]) > maxnumber):
            maxnumber = int (numbers[0])
        if (int(numbers[1]) > maxnumber):
            maxnumber = int (numbers[1])

        numbers = nums_ls[2].split(",")

        endPointsX.append( numbers[0])
        endPointsY.append( numbers [1])

        if (int(numbers[0]) > maxnumber):
            maxnumber = int (numbers[0])
        if (int(numbers[1]) > maxnumber):
            maxnumber = int (numbers[1])

    print(startPointsX,endPointsX)

    i = 0
    j = 0
    w = len (startPointsX)
    h = len (startPointsY)

    matrix = [[0 for x in range(maxnumber+1)] for y in range(maxnumber+1)] 
    target = 0
    start = 0
    pointsOverlap = 0
    while (i < len(startPointsX)):
        
        if (startPointsX[i] == endPointsX[i]):
            if (int(startPointsY[i]) > int(endPointsY[i])):
                target = startPointsY[i]
                start = endPointsY[i]
            else:
                target = endPointsY[i]
                start = startPointsY[i]

            while (int(start) <= int(target)):
                matrix[int(start)][int(startPointsX[i])] += 1
                start = int(start)
                if (matrix[int(start)][int(startPointsX[i])] > 1 and matrix[int(start)][int(startPointsX[i])] < 3):
                    pointsOverlap+=1
                start+=1
        elif (startPointsY[i] == endPointsY[i]):
            if(int(startPointsX[i]) > int(endPointsX[i])):
                target = startPointsX[i]
                start = endPointsX[i]
            else:
                target = endPointsX[i]
                start = startPointsX[i]

            while (int(start) <= int(target)):
                matrix[int(startPointsY[i])][int(start)] += 1
                start = int(start)
                if (matrix[int(startPointsY[i])][int(start)] > 1 and matrix[int(startPointsY[i])][int(start)] < 3):
                    pointsOverlap+=1
                start+=1


        i+=1
    
    while (j < len(matrix)):
        print(matrix[j])
        j+=1

    print("points overlap:" + str(pointsOverlap))


def partTwo():
    startPointsX = []
    startPointsY = []
    endPointsX = []
    endPointsY = []
    numbers = []
    maxnumber = 0
    with open("day5Data.txt", 'r') as f:
        data = f.readlines() 

    for raw_line in data:
        split_line = raw_line.strip().split(" ") 
        nums_ls = [str(x) for x in split_line] 
        numbers = nums_ls[0].split(",")
        
        startPointsX.append( numbers[0])
        startPointsY.append( numbers [1])

        if (int(numbers[0]) > maxnumber):
            maxnumber = int (numbers[0])
        if (int(numbers[1]) > maxnumber):
            maxnumber = int (numbers[1])

        numbers = nums_ls[2].split(",")

        endPointsX.append( numbers[0])
        endPointsY.append( numbers [1])

        if (int(numbers[0]) > maxnumber):
            maxnumber = int (numbers[0])
        if (int(numbers[1]) > maxnumber):
            maxnumber = int (numbers[1])

    print(startPointsX,endPointsX)

    i = 0
    j = 0
    w = len (startPointsX)
    h = len (startPointsY)

    matrix = [[0 for x in range(maxnumber+1)] for y in range(maxnumber+1)] 
    target = 0
    start = 0
    pointsOverlap = 0
    while (i < len(startPointsX)):
        
        if (startPointsX[i] == endPointsX[i]):
            if (int(startPointsY[i]) > int(endPointsY[i])):
                target = startPointsY[i]
                start = endPointsY[i]
            else:
                target = endPointsY[i]
                start = startPointsY[i]

            while (int(start) <= int(target)):
                matrix[int(start)][int(startPointsX[i])] += 1
                start = int(start)
                if (matrix[int(start)][int(startPointsX[i])] > 1 and matrix[int(start)][int(startPointsX[i])] < 3):
                    pointsOverlap+=1
                start+=1
        elif (startPointsY[i] == endPointsY[i]):
            if(int(startPointsX[i]) > int(endPointsX[i])):
                target = startPointsX[i]
                start = endPointsX[i]
            else:
                target = endPointsX[i]
                start = startPointsX[i]

            while (int(start) <= int(target)):
                matrix[int(startPointsY[i])][int(start)] += 1
                start = int(start)
                if (matrix[int(startPointsY[i])][int(start)] > 1 and matrix[int(startPointsY[i])][int(start)] < 3):
                    pointsOverlap+=1
                start+=1
        elif (startPointsX[i] == startPointsY[i] and endPointsX[i] == endPointsY[i]):
            if(int(startPointsX[i]) > int(endPointsX[i])):
                target = startPointsX[i]
                start = endPointsX[i]
            else:
                target = endPointsX[i]
                start = startPointsX[i]

            while (int(start) <= int(target)):
                matrix[int(start)][int(start)] += 1
                start = int(start)
                if (matrix[int(start)][int(start)] > 1 and matrix[int(start)][int(start)] < 3):
                    pointsOverlap+=1
                start+=1

        elif (startPointsX[i] == endPointsY[i] and startPointsY[i] == endPointsX[i]):
            if(int(startPointsX[i]) > int(endPointsX[i])):
                target = startPointsX[i]
                start = endPointsX[i]
                start2 = endPointsY[i]
            else:
                target = endPointsX[i]
                start = startPointsX[i]
                start2 = startPointsY[i]

            while (int(start) <= int(target)):
                matrix[int(start)][int(start2)] += 1
                start = int(start)
                start2 = int(start2)
                if (matrix[int(start)][int(start2)] > 1 and matrix[int(start)][int(start2)] < 3):
                    pointsOverlap+=1
                start+=1
                start2-=1

        else:
            if(int(startPointsX[i]) > int(endPointsX[i]) and int(startPointsY[i]) > int(endPointsY[i])):
                target = endPointsX[i]
                start = startPointsX[i]
                start2 = startPointsY[i]

                while (int(start) >= int(target)):
                    matrix[int(start2)][int(start)] += 1
                    start = int(start)
                    start2 = int(start2)
                    if (matrix[int(start2)][int(start)] > 1 and matrix[int(start2)][int(start)] < 3):
                        pointsOverlap+=1
                    start-=1
                    start2-=1

            elif (int(startPointsX[i]) < int(endPointsX[i]) and int(startPointsY[i]) < int(endPointsY[i])):
                target = startPointsX[i]
                start = endPointsX[i]
                start2 = endPointsY[i]

                while (int(start) >= int(target)):
                    matrix[int(start2)][int(start)] += 1
                    start = int(start)
                    start2 = int(start2)
                    if (matrix[int(start2)][int(start)] > 1 and matrix[int(start2)][int(start)] < 3):
                        pointsOverlap+=1
                    start-=1
                    start2-=1
            elif (int(startPointsX[i]) < int(endPointsX[i]) and int(startPointsY[i]) > int(endPointsY[i])):
                target = startPointsX[i]
                start = endPointsX[i]
                start2 = endPointsY[i]

                while (int(start) >= int(target)):
                    matrix[int(start2)][int(start)] += 1
                    start = int(start)
                    start2 = int(start2)
                    if (matrix[int(start2)][int(start)] > 1 and matrix[int(start2)][int(start)] < 3):
                        pointsOverlap+=1
                    start-=1
                    start2+=1

            elif (int(startPointsX[i]) > int(endPointsX[i]) and int(startPointsY[i]) < int(endPointsY[i])):
                target = endPointsX[i]
                start = startPointsX[i]
                start2 = startPointsY[i]

                while (int(start) >= int(target)):
                    matrix[int(start2)][int(start)] += 1
                    start = int(start)
                    start2 = int(start2)
                    if (matrix[int(start2)][int(start)] > 1 and matrix[int(start2)][int(start)] < 3):
                        pointsOverlap+=1
                    start-=1
                    start2+=1

        i+=1
    
    while (j < len(matrix)):
        print(matrix[j])
        j+=1

    print("points overlap part two:" + str(pointsOverlap))
