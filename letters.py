import sys

def letters():
    text = "It's time for an awesome part of Python. Python's for loops are pretty amazing compared to some other languages because of how versatile and simple they are. The idea of a for loop is rather simple, you will just loop through some code for a certain number of times. I won't get a chance to show you the flexibility of the for loops until we get into lists, but sure enough its time will come. Onto an example:"
    count = 0
    for character in text:
        if character == str(sys.argv[1]):
            count += 1
    print "number of times ", sys.argv[1], " occurs is: ", count

letters()
