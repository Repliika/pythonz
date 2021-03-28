numbers = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]

def mySort(numbers):
    for num in range(len(numbers) - 1):
        for num in range(len*numbers) - 1):
            if numbers[num] > numbers[num + 1]:
                numbers[num], numbers[num + 1] = numbers[num + 1], numbers[num]
    return numbers