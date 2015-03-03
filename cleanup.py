##########################################################################
##                 ss_stride.sh data cleaner and organizer              ##
##                        Author: Sid Narasimhan                        ##
##########################################################################

"""
This script works in association with ss_stride.sh.
"""

import sys
import re
import os
import numpy as np
file = open("stride_output.txt", "w")
file.close()
file = open("stride_output.txt", "r+")
looper = int(sys.argv[1]) -1
for i in range(looper):
  f = open("ss_frame%s.txt" % i, "r+")
  a = []
  for line in f:
    a.append(line.split()[5])
    a.append(" ")
  file.write(np.asarray(a))
  file.write("\n")
  f.close()
file.close()
my_dir = os.getcwd()
for fname in os.listdir(my_dir):
  if fname.startswith("ss_frame"):
    os.remove(os.path.join(my_dir, fname))
