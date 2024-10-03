def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]

    sorted_list = bubble_sort(unsorted_list)

    print(f"Відсортований список: {sorted_list}")