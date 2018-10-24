import sys

def rearrange(*args):
    args = list(args)
    new_args = []
    for word in reversed(args):
        new_args.append(word)
    return new_args

if __name__ == '__main__':
    args = sys.argv[1:]
    print(rearrange(*args))
