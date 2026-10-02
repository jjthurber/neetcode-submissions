def add_two_numbers() -> int:
    nums = input("")
    numSplit = nums.split(",")
    rSum = 0
    for i in numSplit:
        rSum += int(i)
    return rSum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
