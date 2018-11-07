M = input()
M = int(M)

string = input("hey:")

spacesM = -1
mSet = set()
while len(mSet) < M:
    element = ""
    for char in string:
        if char != " ":
            element += char
        else:
            mSet.add(element)
            element = ""
            print((len(mSet), M))
else:
    mSet.remove()

print(mSet)

N = input()
N = int(M)

string = input("hey:")

spacesN = -1
nSet = set()
while spacesN < N:
    element = ""
    for char in string:
        if char != " ":
            element += char
        else:
            nSet.add(element)
            element = ""
            spacesN += 1
            print((spacesN, N))

print(nSet)
