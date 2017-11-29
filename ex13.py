from sys import argv #import: how you add features to your script from the python feature set
#argv is the argument variable: holds te arguments you pass to your python script when you run it
script, first, second, third = argv 
#line 3 "unpacks" argv so that it is assigned to four variables.
#take wahtever is in argv, unpack it, assign it to all of these variables on the left in order
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
