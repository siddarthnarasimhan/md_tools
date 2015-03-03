
############################################################################################
##  A multifuntional python script to carryout secondary structure analyses using MDTraj  ##
##                                Author: Sid Narasimhan                                  ## 
############################################################################################

"""
GENERAL INFO:
make sure you copy this script in the folder containing your md run files
Usage: python ss_mdtraj.py <xtc file> <tpr file> <function_name>
"""

import os
import sys
import pickle as p
import matplotlib as mpl
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
import numpy as np
import mdtraj as md
from math import pi
traj = md.load_xtc(sys.argv[1],top=sys.argv[2])
n_frames = traj.n_frames


"""	 Dictionary of secondary structures 	"""
"""	       function_name: dssp	        """
"""     Output: DSSP matrix [residueXframes]    """

if sys.argv[3] == 'dssp':
  dssp_array = md.compute_dssp(traj,simplified=True)
  ss = range(2*n_frames)
  file = open('dssp.txt','w')
  file.close()
  file = open('dssp.txt','r+')
  for i in range(n_frames):
    #file.write('Frame_%s: ' % i)    """ UNCOMMENT THIS LINE IF YOU WANT FRAME NUMBERS IN YOUR OUTPUT """
    file.write(dssp_array[i])
    file.write('\n')		
  file.close()


"""		Ramachandran plot		"""
"""	       function_name: rplot		"""
""" WARNING: THIS WILL GENERATE <n_frames> PNGS """

if sys.argv[3] == 'rplot':
  phi = md.compute_phi(traj)
  psi = md.compute_psi(traj)
  print phi[1][traj.n_frames-1]
  for i in range(20):
    plt.scatter(phi[1][i], psi[1][i], marker = 'x')
    plt.xlabel(r'$\Phi$ Angle [radians]')
    plt.ylabel(r'$\Psi$ Angle [radians]')
    plt.xlim(-pi,pi)
    plt.ylim(-pi,pi)
    plt.savefig('%s_frame' % i, dpi=320)	
    plt.close()
