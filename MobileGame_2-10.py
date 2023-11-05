'''Sample data from task 2:
5
10 34 556
84 34 91 84 33 97 29 57 13 34
14 18 520
96 83 6 32 16 37 73 52 100 19 17 75 6 79
14 98 975
96 17 41 71 14 99 90 84 90 50 83 69 74 97
14 41 1418
7 70 9 76 42 10 58 72 28 77 41 35 59 23
10 85 490
98 43 94 3 77 91 28 84 86 94'''


# Define the file path
file_path = r'C:\Users\ASUS\OneDrive\Miscellaneous\Documents\Computer science\MCC data.txt'

# Open the file and read the content
with open(file_path, 'r') as file:
    # Read the number of test cases
    T = int(file.readline())

    # Iterate through each test case
    for _ in range(T):
        # Read the inputs for each test case
        N, A, B = map(int, file.readline().split())
        enemies = list(map(int, file.readline().split()))

        # Initialize variables
        enemies_to_kill = 0
        current_power = A

        # Iterate through each enemy's power level
        for power in enemies:
            # If the enemy's power is less than Alice's power and Alice's current power is less than the required power
            if power < current_power and current_power < B:
                current_power += power
                enemies_to_kill += 1

        # If the current power is still less than the required power, set enemies_to_kill to -1
        if current_power < B:
            enemies_to_kill = -1

        # Print the result for the current test case
        print(enemies_to_kill)
