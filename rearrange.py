import sys
import random

def rearrange(*args):
    count = len(args)
    args = list(args)
    for i in range(count):
        j = random.randint(0, i)
        args[i], args[j] = args[j], args[i]
    return args

if __name__ == '__main__':
    args = sys.argv[1:]
    print(rearrange(*args))

#SOURCE: https://www.geeksforgeeks.org/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/
