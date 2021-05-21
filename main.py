numbers = [45, 2, 1, 6, 7, 10]


def selSort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[smallest] > nums[j]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]


def bubbles(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


selSort(numbers)
for x in range(len(numbers)):
    print(numbers[x])
