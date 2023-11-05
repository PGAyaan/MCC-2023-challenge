'''Input data for task 1:
7 5
3 2
2 2
2 4
4 2
4 2
2 4
3 4'''

# Function to calculate the minimum total area of blue rectangles to cover all red rectangles
def minimum_total_area(n, k, rectangles):
    rectangles.sort(reverse=True)  # Sorting the rectangles in descending order based on height
    total_area = 0  # Initializing the total area

    # Calculating the total area of blue rectangles
    for i in range(k, n, k):
        total_area += rectangles[i - 1][0] * rectangles[i - 1][1]

    return total_area

# Reading input from the file
file_path = r"C:\Users\ASUS\OneDrive\Miscellaneous\Documents\Computer science\MCC data.txt"
with open(file_path, 'r') as file:
    n, k = map(int, file.readline().split())
    rectangles = []
    for _ in range(n):
        h, w = map(int, file.readline().split())
        rectangles.append((h, w))

# Calling the function and printing the result
result = minimum_total_area(n, k, rectangles)
print(result)
