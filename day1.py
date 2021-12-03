

def main():
    file = open('day1input.txt', 'r')
    increases = 0
    previous_line = 9999999
    lines = file.readlines()

    for line in lines:
        strip_line = int(line.strip())
        if strip_line > previous_line:            
            increases += 1
        previous_line = strip_line

    print(increases)


if __name__ == "__main__":
    main()