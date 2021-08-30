def getMiddleThreeChars(sampleStr):
    mid = int(len(sampleStr) / 2)
    print("Original String", sampleStr)
    middleThree = sampleStr[mid - 1:mid + 2]
    print("Middle Three Char:", middleThree)


getMiddleThreeChars("JhonDipPeta")
