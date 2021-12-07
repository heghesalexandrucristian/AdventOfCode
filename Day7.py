

def partOne():

    with open("day7Data.txt", 'r') as f:
        data = f.readlines() 

    for raw_line in data:
        split_line = raw_line.strip().split(" ") 
        nums_ls = [str(x) for x in split_line] 
        numbers = nums_ls[0].split(",")

    i = 0
    while (i < len(numbers)):
        numbers[i] = int(numbers[i])
        i+=1
    #print(numbers)
    maxPos = 0
    maxPos = sum(numbers)

    i = 1
    fuelMin = maxPos
    lastFuel = maxPos
    while ( i <= maxPos):
        lastFuel = fuelMin
        print(fuelMin)
        j = 0
        fuel = 0
        while (j < len(numbers)):
            
            fuel+= abs(numbers[j] - i)
            j+=1

        if (fuel < fuelMin ):
            fuelMin = fuel
            
        if(lastFuel == fuelMin):
                i = maxPos
                break
           

        i+=1

    print(fuelMin)


def partTwo():
    with open("day7Data.txt", 'r') as f:
        data = f.readlines() 

    for raw_line in data:
        split_line = raw_line.strip().split(" ") 
        nums_ls = [str(x) for x in split_line] 
        numbers = nums_ls[0].split(",")

    i = 0
    while (i < len(numbers)):
        numbers[i] = int(numbers[i])
        i+=1

    maxPos = 0
    maxPos = sum(numbers)

    i = 1
    #takes so much time
    fuelMin = maxPos * len(numbers)
    lastFuel = maxPos * len(numbers)
    fuelIncrease = 0
    while ( i <= maxPos):
        lastFuel = fuelMin
        j = 0
        fuel = 0
        while (j < len(numbers)):
            fuelIncrease = 0
            k = 1
            test  = abs(numbers[j] - i)
            #print(test)
            while (k <= test):
                fuelIncrease+=1
                fuel+=fuelIncrease
                k+=1
                
            j+=1
        print(fuel)

        if (fuel < fuelMin ):
            fuelMin = fuel
            
        if(lastFuel == fuelMin):
                i = maxPos
                break
           
        i+=1

    print(fuelMin)
