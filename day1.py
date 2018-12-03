def main():
    frequency = 0
    with open("day1input.txt", "r") as day1_file:
        for line in day1_file:
            change = int(line)
            frequency += change
    print(f"Final frequency is {frequency}")


if __name__ == "__main__":
    main()
