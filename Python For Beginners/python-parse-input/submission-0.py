from typing import List

def read_integers() -> List[int]:
    inputList = input("")
    newList = inputList.split(",")
    for i in range(0, len(newList)):
        newList[i] = int(newList[i])
    return newList


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
