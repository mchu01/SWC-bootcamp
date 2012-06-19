#!/urs/bin/env python

import animals

import sys

#import argparse   # complex but powerful

filename = sys.argv[1]
animal = sys.argv[2]

try:
  mean_count = animals.main(filename,animal)
except ZeroDivisionError:
  print "There is no", animal
  
print " The mean count of ", animal, " is ", mean_count