#  File: sorting.py
#  Description: We want a driver that will sort various lists using algorithms, calculating their execution time, and printing a table of results: Bubble Sort, Insertion Sort, Selection Sort, Shell Sort, Merge Sort, and Quick Sort
#  Student's Name: Minh-Tri Ho
#  Student's UT EID: mh47723
#  Course Name: CS 313E
#  Unique Number: 50940
#
#  Date Created: 04/16/16
#  Date Last Modified: 04/16/16

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

#Show the table of results from the records
def show(res):
    print("\n__________________Results__________________")
    for i in range(len(res)):
        print("\n")
        if i == 0:
            print("Input type = Random")
        elif i == 1:
            print("Input type = Sorted")
        elif i == 2:
            print("Input type = Reverse")
        elif i == 3:
            print("Input type = Almost Sorted")

        print("".rjust(16) + "avg time".rjust(12) + "avg time".rjust(11) + "avg time".rjust(11))
        print("Sort function".rjust(16) + "(n=10)".rjust(12) + "(n=100)".rjust(11) + "(n=1000)".rjust(11))
        print("-----------------------------------------------------")
        print("bubbleSort".rjust(16) + ((str)(format(res[i][0][0],'.6f'))).rjust(12) + ((str)(format(res[i][0][1],'.6f'))).rjust(11) + ((str)(format(res[i][0][2],'.6f'))).rjust(11))
        print("selectionSort".rjust(16) + ((str)(format(res[i][1][0],'.6f'))).rjust(12) + ((str)(format(res[i][1][1],'.6f'))).rjust(11) + ((str)(format(res[i][1][2],'.6f'))).rjust(11))
        print("insertionSort".rjust(16) + ((str)(format(res[i][2][0],'.6f'))).rjust(12) + ((str)(format(res[i][2][1],'.6f'))).rjust(11) + ((str)(format(res[i][2][2],'.6f'))).rjust(11))
        print("shellSort".rjust(16) + ((str)(format(res[i][3][0],'.6f'))).rjust(12) + ((str)(format(res[i][3][1],'.6f'))).rjust(11) + ((str)(format(res[i][3][2],'.6f'))).rjust(11))
        print("mergeSort".rjust(16) + ((str)(format(res[i][4][0],'.6f'))).rjust(12) + ((str)(format(res[i][4][1],'.6f'))).rjust(11) + ((str)(format(res[i][4][2],'.6f'))).rjust(11))
        print("quickSort".rjust(16) + ((str)(format(res[i][5][0],'.6f'))).rjust(12) + ((str)(format(res[i][5][1],'.6f'))).rjust(11) + ((str)(format(res[i][5][2],'.6f'))).rjust(11))

def main():
    #Save all of the average times from the above test cases, and print them out in a table. (See the "output" section below.)
    res = []
    #Random, Sorted, Reverse, Almost Sorted
    for typeSort in range(4):
        #Repeat steps 1-6 for each of the six sorting algorithms.
        resAlgoNum = []

        for algoNum in range(6):
            #Repeat steps 1-5 three times: once for n=10, once for n=100, and once for n=1000.
            resNbTimes = []

            for nbTimes in range(3):
                listLength = 10**(nbTimes+1)
                totalTime = 0

                #Repeat steps 1-4 five times, and calculate an average time.
                for tryAgain in range(5):
                    #1. Generate a list containing n integers in random order.
                    myList = [i for i in range(listLength)]

                    print("")
                    #Type of List depending on typeSort
                    if typeSort == 0:
                        random.shuffle(myList)
                    elif typeSort == 1: #Sorted order
                        print("Ordered Sorted List")
                    elif typeSort == 2: #Reverse order
                        print("Reverse Ordered List")
                        tempList = []
                        for rev in range(len(myList)):
                            tempList.append(myList[-rev-1])
                        myList = tempList
                    elif typeSort == 3: #Almost Sorted
                        print("Almost Sorted List")
                        #Sorting for 10% of the list
                        for alm in range((int)(len(myList)/10)):
                            randomIndex1 = random.randint(0,len(myList)-1)
                            randomIndex2 = random.randint(0,len(myList)-1)
                            myList[randomIndex1],myList[randomIndex2] = myList[randomIndex2],myList[randomIndex1]

                    print("List Length: " +str(listLength))
                    #Debug: print(myList)

                    #2. Start a timer.
                    print("Start sorting...")
                    startTime = time.perf_counter()

                    #3. Use function to sort the list.
                    if algoNum == 0:
                        #Bubble Sort
                        print("Bubble Sort")
                        bubbleSort(myList)
                    elif algoNum == 1:
                        #Selection Sort
                        print("Selection Sort")
                        selectionSort(myList)
                    elif algoNum == 2:
                        #Insertion Sort
                        print("Insertion Sort")
                        insertionSort(myList)
                    elif algoNum == 3:
                        #Shell Sort
                        print("Shell Sort")
                        shellSort(myList)
                    elif algoNum == 4:
                        #Merge Sort
                        print("Merge Sort")
                        mergeSort(myList)
                    elif algoNum == 5:
                        #Quick Sort
                        print("Quick Sort")
                        quickSort(myList)

                    #4. Stop the timer.
                    endTime = time.perf_counter()
                    elapsedTime = endTime - startTime
                    print("End sorting...")
                    print("Elapsed Time = " +str(elapsedTime))

                    #Add to totalTime
                    totalTime += elapsedTime

                avgTime = totalTime / 5
                resNbTimes.append(avgTime)

            resAlgoNum.append(resNbTimes)

        res.append(resAlgoNum)

    show(res)

main()
