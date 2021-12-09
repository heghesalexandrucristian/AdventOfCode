import copy
import string

def partOne():

    zero = 6
    one = 2
    two = 5
    three = 5
    four = 4
    five = 5
    six = 6
    seven = 3
    eight = 7
    nine = 6

    uniqLengthNumbers = [one,four,seven,eight]
    numbers = []
    numbers2 = []

    with open("day8Data.txt", 'r') as f:
        data = f.readlines()

    for raw_line in data:
        split_line = raw_line.strip().split("|")
        nums_ls = [str(x) for x in split_line] 
        numbers.append(nums_ls[0].split(" "))

    for raw_line in data:
        split_line = raw_line.strip().split("|")
        nums_ls = [str(x) for x in split_line] 
        numbers2.append(nums_ls[1].split(" "))

    for i in range(len(numbers)):
        numbers[i].pop(len(numbers[i])-1)

    for i in range(len(numbers2)):
        numbers2[i].pop(0)

    i = 0
    numberCount = 0
    while (i < len(numbers2)):

        j = 0
        while (j < len(numbers2[i])):
            print (numbers2[i][j])
            print (uniqLengthNumbers)
            if len(numbers2[i][j]) in uniqLengthNumbers:
                numberCount+=1
            j+=1

        i+=1


    print(numbers)
    print(numbers2)
    print(uniqLengthNumbers)
    print(numberCount)

def partTwo():
    zero = 6
    one = 2
    two = 5
    three = 5
    four = 4
    five = 5
    six = 6
    seven = 3
    eight = 7
    nine = 6

    uniqLengthNumbers = [one,four,seven,eight]
    numbers = []
    numbers2 = []

    with open("day8Data.txt", 'r') as f:
        data = f.readlines()

    for raw_line in data:
        split_line = raw_line.strip().split("|")
        nums_ls = [str(x) for x in split_line] 
        numbers.append(nums_ls[0].split(" "))

    for raw_line in data:
        split_line = raw_line.strip().split("|")
        nums_ls = [str(x) for x in split_line] 
        numbers2.append(nums_ls[1].split(" "))

    for i in range(len(numbers)):
        numbers[i].pop(len(numbers[i])-1)

    for i in range(len(numbers2)):
        numbers2[i].pop(0)

    top = ""
    topLeft = ""
    topRight = ""
    middle = ""
    bottomLeft = ""
    bottomRight = ""
    bottom = ""

    numberEight = [top,topLeft,topRight,middle,bottomLeft,bottomRight,bottom]
    numberOne = ""
    numberFour = ""
    numberSeven = ""
    numberEight = ""

    test1 = True

    i = 0
    numberCount = 0
    totalSum = 0
    while (i < len(numbers)):

            j = 0
            numbers[i].sort(key=len)
            print(numbers)
            while (j < len(numbers[i])):

                if (len(numbers[i][j]) == uniqLengthNumbers[0]):
                    number = numbers[i][j]
                    topRight = number[0]
                    bottomRight = number[1]
                    numberOne = number
                if (len(numbers[i][j]) == uniqLengthNumbers[1]):

                    fuck = 0
                    while (fuck < len(numbers[i][j])):
                        number = numbers[i][j]
                        if number[fuck] not in numberOne:
                            if (middle == ""):
                                middle = number[fuck]
                            else:
                                topLeft = number[fuck]
                        numberFour = number
                        fuck+=1

                if (len(numbers[i][j]) == uniqLengthNumbers[2]):
                    fuck = 0
                    while (fuck < len(numbers[i][j])):
                        number = numbers[i][j]
                        if number[fuck] not in numberOne:
                            top = number[fuck]

                        numberSeven = number
                        fuck+=1

                if (len(numbers[i][j]) == uniqLengthNumbers[3]):
                    fuck = 0
                    while (fuck < len(numbers[i][j])):
                        numberToCompare = numberSeven + numberFour
                        number = numbers[i][j]
                        if number[fuck] not in numberToCompare:
                            if (bottom == ""):
                                bottom = number[fuck]
                            else:
                                bottomLeft = number[fuck]
                            numberEight = number
                        fuck+=1
                    x = 0
                    if (fuck == len(numbers[i][j]) and bottomLeft!=""):
                        while (x < len(numbers[i])):
                            if (len(numbers[i][x]) == 6):
                                fuck = 0
                                number =  numberFour
                                while (fuck < len(numberOne)):  
                                    if numberOne[0] in number:
                                        number = number.replace(numberOne[0],'')
                                    if numberOne[1] in number:
                                        number = number.replace(numberOne[1],'')

                                    if number[fuck] not in numbers[i][x]:
                                        if (number[fuck] != middle):
                                            buffer = middle
                                            middle = topLeft
                                            topLeft = buffer

                                    if numberOne[fuck] not in numbers[i][x]:
                                        if (topRight != numberOne[fuck]):
                                            buffer = topRight
                                            topRight = numberOne[fuck]
                                            bottomRight = buffer

                                    numberSevenPlusFour = numberSeven+numberFour
                                    numberSevenPlusFour = ''.join(sorted(set(numberSevenPlusFour), key=numberSevenPlusFour.index))

                                    fuck2 = 0
                                    while (fuck2 < len(numberEight)):
                                        number9 = numbers[i][x]
                                        if (numberEight[fuck2] not in number9):
                                            if (numberEight[fuck2] not in  numberOne):
                                                 if (bottomLeft != numberEight[fuck2]):
                                                         print(numberEight)
                                                         print(number9)
                                                         print(len(number9))
                                                         buffer = bottomLeft
                                                         bottomLeft = bottom
                                                         bottom = buffer
                                        fuck2+=1
                                        test1 = False
                                        
                                    fuck+=1
                            x+=1

                j+=1
                zero = top+topLeft+topRight+bottomLeft+bottomRight+bottom
                one = topRight+bottomRight
                two = top+topRight+middle+bottomLeft+bottom
                three = top+topRight+middle+bottomRight+bottom
                four = topRight+middle+bottomRight+topLeft
                five = top+topLeft+middle+bottomRight+bottom
                six = top+topLeft+middle+bottomRight+bottom+bottomLeft
                seven = top+topRight+bottomRight
                eight = top+topLeft+topRight+bottomLeft+bottomRight+bottom+middle
                nine = top+topLeft+topRight+bottomRight+bottom+middle
                sum = ""
                k=0
                while (k < len(numbers2[i])):
                    #print(numbers2[k])
                    if (sorted(numbers2[i][k]) == sorted(five)):
                        sum+="5"
                        print (sorted(five))
                    if (sorted(numbers2[i][k]) == sorted(three)):
                        sum+="3"
                    if (sorted(numbers2[i][k]) == sorted(four)):
                        sum+="4"
                    if (sorted(numbers2[i][k]) == sorted(six)):
                        sum+="6"
                    if (sorted(numbers2[i][k]) == sorted(seven)):
                        sum+="7"
                    if (sorted(numbers2[i][k]) == sorted(eight)):
                        sum+="8"
                    if (sorted(numbers2[i][k]) == sorted(nine)):
                        sum+="9"
                    if (sorted(numbers2[i][k]) == sorted(zero)):
                        sum+="0"
                    if (sorted(numbers2[i][k]) == sorted(one)):
                        sum+="1"
                    if (sorted(numbers2[i][k]) == sorted(two)):
                        sum+="2"
                    k+=1

            print(sum)
            totalSum+= int(sum)
            zero = ""
            one = ""
            two = ""
            three = ""
            four = ""
            five = ""
            six = ""
            seven = ""
            eight = ""
            nine = ""
            top = ""
            topLeft = ""
            topRight = ""
            middle = ""
            bottomLeft = ""
            bottomRight = ""
            bottom = ""
            numberEight = [top,topLeft,topRight,middle,bottomLeft,bottomRight,bottom]
            numberOne = ""
            numberFour = ""
            numberSeven = ""
            numberEight = ""
            i+=1

    print(totalSum)
