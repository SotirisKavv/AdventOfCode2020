def readFile(filename):
    f = open(filename)
    words = f.read().splitlines()
    words = [int(i) for i in words]
    f.close()
    return words

def candidate2Product(arr, val):
    i = 0
    j = len(arr) - 1

    arr.sort()

    while i < j:
        a = int(arr[i])
        b = int(arr[j])

        if a + b < val:
            i=i+1
        elif a + b > val:
            j=j-1
        elif a + b == val:
            return a*b
    return 0

def candidate3Product(arr, val):
    arr.sort()

    for i in range(0, len(arr)):
        j = i + 1
        k = len(arr) - 1

        a = int(arr[i])

        while j < k:
            b = int(arr[j])
            c = int(arr[k])

            if a + b + c < val:
                j=j+1
            elif a + b + c > val:
                k=k-1
            elif a + b + c == val:
                return a*b*c
    return 0

entries = readFile('input1')
print(candidate2Product(entries, 2020))
print(candidate3Product(entries, 2020))
