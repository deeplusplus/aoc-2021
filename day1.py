
def main():
    file = open('day1input.txt', 'r')
    increases = 0
    previous_window = 999999
    lines = file.readlines()

    start = 0
    end = 3

    while end <= len(lines):
        window = lines[start:end]
        print(window)
        num1 = int(window[0].strip())
        num2 = int(window[1].strip())
        num3 = int(window[2].strip())

        window1 = num1 + num2 + num3

        if window1 > previous_window:            
            increases += 1
        previous_window = window1
        start+=1
        end+=1

    print(increases)


if __name__ == "__main__":
    main()