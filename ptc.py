import math
import os
import random
import re
import sys

# Complete the 'jumpingOnClouds' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.

def jumpingOnClouds(c):
    # Write your code here
    a = 0
    jump = -1
    while(a<len(c)):
        jump += 1
        if(a<len(c)-2 and c[a+2]==0):
            a += 1
        a += 1
    return jump
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
