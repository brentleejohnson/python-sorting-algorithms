numbers = [45, 2, 1, 6, 7, 10]


def selSort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[smallest] > nums[j]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]


selSort(numbers)
for x in range(len(numbers)):
    print(numbers[x])
