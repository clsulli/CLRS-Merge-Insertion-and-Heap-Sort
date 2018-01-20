import time

def insertionSort(list):
    for index in range(1, len(list)):

        currentvalue = list[index]
        position = index

        while position > 0 and list[position - 1] > currentvalue:
            list[position] = list[position - 1]
            position = position - 1

        list[position] = currentvalue

def listToArray(file):
    fObj = open(file, "r")
    tempArr = []
    for line in fObj:
        tempArr.append(line)

    return tempArr

def selectSort():
    print("Select Sorting Algorithm:")
    print("     (a) Insertion Sort")
    print("     (b) Merge Sort")
    print("     (c) Heap Sort")
    print("     (d) Build Heap")

    choice = input(">> ")

    if choice == "a" or choice == "A":
        return 1
    elif choice == "b" or choice == "B":
        return 2
    elif choice == "c" or choice == "C":
        return 3
    elif choice == "d" or choice == "D":
        return 4

def selectSize():
    print("Select Size:")
    print("     (a) 30K")
    print("     (b) 60K")
    print("     (c) 90K")
    print("     (d) 120K")
    print("     (e) 150K")

    choice = input(">> ")

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

def selectPorS():
        print("Select if Initially Sorted or Permutated:")
        print("     (a) Permutated")
        print("     (b) Sorted")

        choice = input(">> ")

        if choice == "a" or choice == "A":
            return 1
        elif choice == "b" or choice == "B":
            return 2

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
startTime = time.clock()
insertionSort(currFile)
finTime = time.clock() - startTime
print(currFile)
print(str(finTime) + " Secconds")





