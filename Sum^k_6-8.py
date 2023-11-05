'''Input data for task 1:
10 1
91 76 42 77 74 77 86 48 3 51'''

# Reading the input data from the specified file path
file_path = 'C:\\Users\\ASUS\\OneDrive\\Miscellaneous\\Documents\\Computer science\\MCC data.txt'

# Function to calculate the sum of scores over all subsets of A modulo 998244353
def sum_of_scores(file_path):
    # Read the input data from the file
    with open(file_path, 'r') as file:
        # Reading the first line
        n, k = map(int, file.readline().split())
        data = list(map(int, file.readline().split()))

        # Calculate the sum of scores
        result = 0
        for num in data:
            result += num**k

        return result % 998244353

# Calling the function and printing the result
print(sum_of_scores(file_path))
