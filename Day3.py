
commonBits = []
commonBitsScrub = []

def commonBit(lines):
    global commonBits
    global commonBitsScrub
    commonBits.clear()
    commonBitsScrub.clear()
    numberOfDigits = len(lines[0])-1
    digitIndex = 0
    bit0Count = 0
    bit1Count = 0

    i = 0
    while (i < len(lines)):
        
        digits = [str(x) for x in str(lines[i])]

        if (digits[digitIndex] == "0"):
            
            bit0Count+=1


        else:

            bit1Count+=1

        i+=1

        if (i == len(lines) ):

            if (bit0Count > bit1Count):
                commonBits.append("0")
                commonBitsScrub.append("1")
            else:
                commonBits.append("1")
                commonBitsScrub.append("0")

            if (digitIndex < numberOfDigits):
                digitIndex+=1

            bit0Count = 0
            bit1Count = 0
            i = 0

            if (digitIndex == numberOfDigits ):
                break


def partOne():
    gamaRate = []

    f = open("day3Data.txt", "r")
    lines = f.readlines()

    bit1Count = 0
    bit0Count = 0
    numberOfDigits = len(lines[0])-1
    digitIndex = 0

    i = 0
    while (i < len(lines)):
        
        digits = [str(x) for x in str(lines[i])]

        if (digits[digitIndex] == "0"):
            
            bit0Count+=1


        else:

            bit1Count+=1

        i+=1

        if (i == len(lines) ):
      
            
            if (bit0Count > bit1Count):
                gamaRate += "0"
            else:
                gamaRate += "1"

            if (digitIndex < numberOfDigits):
                digitIndex+=1

            bit1Count = 0
            bit0Count = 0
            i = 0
            if (digitIndex == numberOfDigits ):
                break

    newGamaRate = ""
    epsilonRate = ""
    
    for x in gamaRate:
        
        newGamaRate += x

        if (x == "0"):
            epsilonRate += "1"
        else:
            epsilonRate += "0"

    gamaRateInt = int(newGamaRate,2)
    epsilonRateInt = int(epsilonRate,2)
    return(gamaRateInt * epsilonRateInt)

def partTwo():
    digitIndex = 0
    f = open("day3Data.txt", "r")
    lines = f.readlines()
    numberOfDigits = len(lines[0])-1

    commonBit(lines)

    i = 0
    length = len(lines)
    linesTest = []
    while (i < length):

        digits = [str(x) for x in str(lines[i])]
        if (digits[digitIndex] == commonBits[digitIndex]):
           linesTest.append(lines[i])


        i+=1

        if (i == len(lines)):

            lines = linesTest.copy()
            commonBit(lines)
            linesTest.clear()
            length = len(lines)
            if (length == 1):
                break

            if (digitIndex < numberOfDigits):
                digitIndex+=1
            i = 0
            if (digitIndex == numberOfDigits):
                break


    ##2 tired###
    f = open("day3Data.txt", "r")
    lines2 = f.readlines()
    i = 0
    commonBit(lines2)
    length = len(lines2)
    linesTest = []
    digitIndex = 0
    while (i < length):
        digits = [str(x) for x in str(lines2[i])]
        if (digits[digitIndex] == commonBitsScrub[digitIndex]):
           linesTest.append(lines2[i])


        i+=1

        if (i == len(lines2)):
            lines2 = linesTest.copy()
            commonBit(lines2)
            linesTest.clear()
            length = len(lines2)
            if (length == 1):
                break
 
            if (digitIndex < numberOfDigits):
                digitIndex+=1
            i = 0
            if (digitIndex == numberOfDigits):
                break
    
 
    print(lines)
    print (lines2)
 
    oxygenGeneratprRating = ""
    scruberRating = ""

    for x in lines:
        
        oxygenGeneratprRating += x

    for x in lines2:
        
        scruberRating += x

    oxygenGeneratprRatingInt = int(oxygenGeneratprRating,2)
    scruberRatingInt = int( scruberRating,2)
    return(oxygenGeneratprRatingInt *  scruberRatingInt)
