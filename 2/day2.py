
def main():
    file = open('day2input.txt', 'r')
    lines = file.readlines()

    x = 0
    y = 0
    aim = 0

    for line in lines:
        split_line = line.split()
        direction = split_line[0]
        magnitude = int(split_line[1].strip())

        if direction == "forward":
            x += magnitude
            y = y + (aim * magnitude)
        elif direction == "down":
            aim += magnitude
        else:
            aim -= magnitude

    print(x * y)

if __name__ == "__main__":
    main()