
def find_freq():
    frequency = 0
    seen_freqs = set()
    seen_freqs.add(frequency)
    with open("day1input.txt", "r") as day1_file:
        while True:
            for line in day1_file:
                change = int(line)
                frequency += change
                if frequency in seen_freqs:
                    return frequency
                seen_freqs.add(frequency)
            day1_file.seek(0)


def main():
    frequency = find_freq()
    print(f"second frequency is {frequency}")


if __name__ == "__main__":
    main()
