
import copy

def main():
    file = open('day6input.txt', 'r')
    initial_fish = [int(fish.strip()) for fish in file.readlines()[0].split(",")]
    fish_buckets = {}
    total_fish = 0

    for i in range(0, 9):
        fish_buckets[i] = 0

    for fish in initial_fish:
        fish_buckets[fish] += 1

    print(fish_buckets)

    for step in range(0, 256):
        buckets_copy = copy.deepcopy(fish_buckets)
        fish_buckets[0] = buckets_copy[1]
        fish_buckets[1] = buckets_copy[2]
        fish_buckets[2] = buckets_copy[3]
        fish_buckets[3] = buckets_copy[4]
        fish_buckets[4] = buckets_copy[5]
        fish_buckets[5] = buckets_copy[6]
        fish_buckets[6] = buckets_copy[7] + buckets_copy[0]
        fish_buckets[7] = buckets_copy[8]
        fish_buckets[8] = buckets_copy[0]

    for count in fish_buckets.values():
        total_fish += count
    print(total_fish)

    



if __name__ == "__main__":
    main()