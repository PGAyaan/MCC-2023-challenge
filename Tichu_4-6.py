'''Sample data for task 1:
10 0
4 10 1 8 12 8 1 11 3 7'''


def max_run(cards):
    cards.sort()
    run = max_run_so_far = 0
    prev = -1
    for c in cards:
        if c - prev == 1:
            run += 1
        else:
            run = 1
        max_run_so_far = max(max_run_so_far, run)
        prev = c
    return max_run_so_far

# Specify the file path
file_path = r"C:\Users\ASUS\OneDrive\Miscellaneous\Documents\Computer science\MCC data.txt"

# Read the data from the file
with open(file_path, 'r') as file:
    data = file.readline().strip().split()
    cards = list(map(int, data))

# Call the function with the cards data and print the result
print(max_run(cards))
