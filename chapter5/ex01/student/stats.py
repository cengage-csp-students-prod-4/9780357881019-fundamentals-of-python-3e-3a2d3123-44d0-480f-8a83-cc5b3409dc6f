def mean(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


def mode(numbers):
    if len(numbers) == 0:
        return 0

    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    highest_count = max(counts.values())

    for number in numbers:
        if counts[number] == highest_count:
            return number


def median(numbers):
    if len(numbers) == 0:
        return 0

    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 1:
        return sorted_numbers[middle]
    else:
        return (sorted_numbers[middle - 1] +
                sorted_numbers[middle]) / 2


def main():
    numbers = [8, 2, 5, 3, 9, 6, 2, 7]

    print("List:", numbers)
    print("Mode:", mode(numbers))
    print("Median:", median(numbers))
    print("Mean:", mean(numbers))


if __name__ == "__main__":
    main()