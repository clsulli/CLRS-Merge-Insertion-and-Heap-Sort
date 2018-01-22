import time

#Insertion Sort #Page 17
def insertionSort(a):
    for j in range(len(a)):

        key = a[j]
        i = j - 1

        while i > -1 and a[i] > key:
            a[i+1] = a[i]
            i = i - 1

        a[i+1] = key

    return a

#Merge Sort #Page 34
def mergeSort(a):
    #base case
    if len(a) == 1:
        return a

    middle = len(a)//2

    #Split array until single elements
    left = mergeSort(a[:middle])
    right = mergeSort(a[middle:])

    #Build elements back into single array
    return merge(left,right)

def merge(left, right):
    mergeArray = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            mergeArray.append(left[i])
            i = i + 1
        elif right[j] < left[i]:
            mergeArray.append(right[j])
            j = j + 1

    #Handles Odd amount of elements
    if i < len(left):
        mergeArray.extend(left[i:]) #extend appends the elements left in array "left" to mergeArray
    elif j < len(right):
        mergeArray.extend(right[j:])

    return mergeArray

#Heap Sort #Page 160
def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def heapify(arr, i, size):
    left = 2*i + 1
    right = 2*i + 2

    if left <= size and arr[left] > arr[i]:
        max = left
    else:
        max = i
    if right <= size and arr[right] > arr[max]:
        max = right
    if max != i:
        swap(arr, i, max)
        heapify(arr, max, size)

def buildHeap(arr):
    heapSize = len(arr) - 1
    i = (heapSize//2)

    while i > 0:
        heapify(arr, i, heapSize)
        i = i - 1

def heapSort(arr):
    heapSize = len(arr) - 1
    heapStart = time.clock()
    buildHeap(arr)
    heapFin = time.clock() - heapStart
    print("Heap Build Time: " + str(heapFin) + " Seconds")
    i = len(arr) - 1
    while i > 0:
        swap(arr,0,i)
        heapSize = heapSize - 1
        heapify(arr, 0, heapSize)
        i = i - 1

    return arr

#Save Input File to Array
def listToArray(file):
    fObj = open(file, "r")
    tempArr = []
    for line in fObj:
        tempArr.append(line.strip("\n"))

    return tempArr

#Select the Sort Method
def selectSort():
    print("Select Sorting Algorithm:")
    print("     (a) Insertion Sort")
    print("     (b) Merge Sort")
    print("     (c) Heap Sort")

    choice = raw_input(">> ")

    if choice == "a" or choice == "A":
        return 1
    elif choice == "b" or choice == "B":
        return 2
    elif choice == "c" or choice == "C":
        return 3

#Select File Size
def selectSize():
    print("Select Size:")
    print("     (a) 30K")
    print("     (b) 60K")
    print("     (c) 90K")
    print("     (d) 120K")
    print("     (e) 150K")

    choice = raw_input(">> ")

    if choice == "a" or choice == "A":
        return 1
    elif choice == "b" or choice == "B":
        return 2
    elif choice == "c" or choice == "C":
        return 3
    elif choice == "d" or choice == "D":
        return 4
    elif choice == "e" or choice == "E":
        return 5

#Select Permutated or Sorted
def selectPorS():
        print("Select if Initially Sorted or Permutated:")
        print("     (a) Permutated")
        print("     (b) Sorted")

        choice = raw_input(">> ")

        if choice == "a" or choice == "A":
            return 1
        elif choice == "b" or choice == "B":
            return 2

def implementSort(arr):
    if algo == 1:
        sortedArr = insertionSort(arr)
    elif algo == 2:
        sortedArr = mergeSort(arr)
    elif algo == 3:
        sortedArr = heapSort(arr)

    return sortedArr

#Init Dependencies
perm30K = "Wordlists/perm30K.txt"
perm60K = "Wordlists/perm60K.txt"
perm90K = "Wordlists/perm90K.txt"
perm120K = "Wordlists/perm120K.txt"
perm150K = "Wordlists/perm150K.txt"
sorted30K = "Wordlists/sorted30K.txt"
sorted60K = "Wordlists/sorted60K.txt"
sorted90K = "Wordlists/sorted90K.txt"
sorted120K = "Wordlists/sorted120K.txt"
sorted150K = "Wordlists/sorted150K.txt"

####MAIN####
algo = selectSort()
size = selectSize()
meth = selectPorS()

#Determine Selected File
if meth == 1 and size == 1:
    currFile = perm30K
elif meth == 1 and size == 2:
    currFile = perm60K
elif meth == 1 and size == 3:
    currFile = perm90K
elif meth == 1 and size == 4:
    currFile = perm120K
elif meth == 1 and size == 5:
    currFile = perm150K
elif meth == 2 and size == 1:
    currFile = sorted30K
elif meth == 2 and size == 2:
    currFile = sorted60K
elif meth == 2 and size == 3:
    currFile = sorted90K
elif meth == 2 and size == 4:
    currFile = sorted120K
elif meth == 2 and size == 5:
    currFile = sorted150K

currFile = listToArray(currFile)
startAlgo = time.clock()
listS = implementSort(currFile)
finAlgo = time.clock() - startAlgo
print("Sort took " + str(finAlgo) + " Secconds")

fileW = open('outputSorted.txt', 'w')
for item in listS:
  fileW.write("%s\n" % item)

fileW.write(str(finAlgo))
print("Output File Stored at \outputSorted.txt")




