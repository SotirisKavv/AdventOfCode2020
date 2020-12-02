def readFile(filename):
    f = open(filename)
    words = f.read().splitlines()
    f.close()
    return words

def charInstr(str, ch):
    return len([i for i, ltr in enumerate(str) if ltr == ch])

def isValidOcc(line):

    contents = line.split(': ')
    password = contents[1]
    policy = contents[0]

    contents = policy.split()
    char = contents[1]
    limits = contents[0]

    contents = limits.split('-')
    max = int(contents[1])
    min = int(contents[0])

    t = charInstr(password, char)
    if (min <= t) and (max >= t):
        return 1
    else:
        return 0

def isValidPos(line):

    contents = line.split(': ')
    password = contents[1]
    policy = contents[0]

    contents = policy.split()
    char = contents[1]
    limits = contents[0]

    contents = limits.split('-')
    max = int(contents[1])
    min = int(contents[0])

    if (char == password[min-1] and char != password[max-1]) or\
        (char == password[max-1] and char != password[min-1]):
        return 1
    else:
        return 0

lines = readFile('day2/input1')

tot1 = 0
tot2 = 0
for l in lines:
     tot1 += isValidOcc(l)
     tot2 += isValidPos(l)

print(tot1)
print(tot2)
