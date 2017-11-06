import math
lat = "49.250624 N"
#        49 deg 15min 2.2464sec
# lon = gspData.TPV['lon'] 
# lon = "123.003349 W"

# precondition: decimalStr must be in this format: "49.250624 N"
def decimalToDegMinSec(decimalStr):
    # delimits using spaces into list of strings, then casts first elem to float
    decimalFloat = float(decimalStr.split()[0])
    degreesInt = int(decimalFloat)

    # minutes calc
    floatPart = truncateFloat(decimalFloat)
    minutesFloat = floatPart * 60 
    minutesInt = int(minutesFloat)

    #seconds calc 
    floatPart = truncateFloat(minutesFloat)
    secondsFloat = floatPart * 60 
    # print("deg:{}, min:{}, sec:{}".format(degreesInt, minutesInt, secondsFloat))
    decimalList = [degreesInt, minutesInt, secondsFloat]
    return decimalList

# eg. pass in eg float(3.15), return str(0.15), never 0.1500
def truncateFloat(wholeFloat):
    intPart = int(wholeFloat)
    floatPartLen = len(str(wholeFloat)) - len(str(intPart))-1
    floatPartWithJunk = wholeFloat - intPart 
    pattern = "." + str(floatPartLen) + "f" # produces ".2f" style sig fig
    floatPartStr = format(floatPartWithJunk, pattern)
    return float(floatPartStr)

# note, this works if u pass in int, int, float too
def degMinSecToDecimal(degStr, minStr, secStr):
    secFloat = float(secStr)
    floatPart = secFloat / 60
    minInt = int(minStr)
    minFloat = minInt + floatPart
    floatPart = minFloat / 60
    degInt = int(degStr)
    degFloat = degInt + floatPart
    # print(degFloat)
    return degFloat
print(degMinSecToDecimal("49", "15", "2.2464"))
print(decimalToDegMinSec("49.250624"))
