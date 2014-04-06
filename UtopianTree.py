__author__ = 'smuralid'
# This is a python3 program for the challenge UtopianTree
#This is the submitted version
import sys

# T is the nuymber of cycles
T = int(sys.stdin.readline().strip())

if T<1 or T>10:
  print ("Number of cycles to compute out of range")

# 'M' indicates onset of Monsoon season
# 'S' indicates onset of Summer season

# Storing the height variable
# Tuple is such that first coordinate in the tuple is the height, second is the next possible season


height=[(1,'M')]

for i in range(0,T):
  N = int(sys.stdin.readline().strip())
  height_history = len(height)
  if N<height_history:
    print (height[N][0])
  else:
    for i in range(height_history,N+1):
      if height[height_history-1][1] == "M":
      	height.append((height[height_history-1][0]*2,'S'))
      else:
        height.append((height[height_history-1][0]+1,'M'))
      height_history = height_history + 1
    print (height[height_history-1][0])

