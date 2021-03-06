f = open("quicksort.txt")
a=[]
for lines in f:
    a.append(lines.strip('\n'))
a = list(map(int, a))
    
count = 0

def getmed(x):
    if len(x) % 2 == 0:
        return int(len(x)/2 - 1)
    else:
        return int(len(x)//2)
    

def quicksort_division(x) :
    med_rank = getmed(x)
    if (x[med_rank] - x[0]) * (x[med_rank] - x[-1]) < 0:
        x[med_rank], x[0] = x[0], x[med_rank]
    if (x[-1] - x[0]) * (x[-1] - x[med_rank]) < 0 :
        x[-1], x[0] = x[0], x[-1]
    
    first = x[0]
    n = len(x)
    i = 0
    for j in range(1, n) :
        if x[j] < first:
            i = i + 1 
            x[i], x[j] = x[j], x[i]
    x[i], x[0] =  x[0], x[i]
    return i, x


def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    global count
    count += len(x) - 1
    k = quicksort_division(x)
    pivot = k[0]
    new_x = k[1]
    left = quicksort(new_x[:pivot])
    right = quicksort(new_x[pivot + 1:])
    left.append(new_x[pivot])
    return left + right

quicksort(a)
count

    
