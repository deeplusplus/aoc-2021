import statistics

def main():
    file = open('day7input.txt', 'r')
    crab_positions = [int(crab.strip()) for crab in file.readlines()[0].split(",")]

    # 347 too low
    ideal_position = statistics.median(crab_positions)

    total_fuel_consumption = 0
    for crab_position in crab_positions:
        total_fuel_consumption += abs(crab_position - ideal_position)

    print(total_fuel_consumption)

if __name__ == "__main__":
    main()