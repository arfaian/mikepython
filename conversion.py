import sys

def convert():
    input = sys.argv[1]
    temp = input[:-1]
    symbol = input[-1]
    print "you passed in", input
    if symbol == "C":
        print convertToFahrenheit(temp), "F"
    elif symbol == "F":
        print convertToCelsius(temp), "C"
    else:
      print "you didn't enter the correct arguments dummy"

def convertToCelsius(t):
    return (float(t) - 32) * 5 / 9

def convertToFahrenheit(t):
    return (float(t) * 9 / 5) + 32

convert()
