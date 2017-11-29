def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a + b

def subtract (a,b):
    print "SUBTRACTING %d - %d" %(a,b)
    return a-b

def multiply(a,b):
    print "MULTIPLY %d * %d" %(a,b)
    return a * b

def divide (a,b):
    print "DIVIDING %d / %d" %(a,b)
    return a / b


print "Let's do some math with just functions!"

age = add (20,6)
height = subtract (200, 32)
weight = multiply (10, 7)
iq = divide (100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


print "here is a puzzle."
what= add (age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
