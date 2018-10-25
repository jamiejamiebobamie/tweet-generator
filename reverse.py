import sys

def reverse(*args):
    """takes in a tuple of arguments
    turns the tuple into a list to be modified
    instantiates a new empty array
    cycles through the array of arguments starting with the last element
    and appends the elements of the array to the new, empty array in reverse order"""
    args = list(args)
    new_args = []
    for word in reversed(args):
        new_args.append(word)
    return new_args

if __name__ == '__main__':
    args = sys.argv[1:]
    print(reverse(*args))
