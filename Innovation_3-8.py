'''Sample data for task 1:
5 2
10 8 3 2
2 7 9 5
11 8 2 4
4 5 15 4
3 7 5 3'''

def maximum_points(n, m, cards):
    points = [0] * (5 + n)
    for card in cards:
        for i in range(4):
            points[4 + card[i]] = max(points[4 + card[i]], card[3] + card[2] + card[1])
    for i in range(4, n + 5):
        points[i] = max(points[i], points[i - 1])

    return sum(points[4:4 + m])

# Read data from the file
file_path = r"C:\Users\ASUS\OneDrive\Miscellaneous\Documents\Computer science\MCC data.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()
    n1, m1 = map(int, lines[0].split())
    cards1 = [list(map(int, line.split())) for line in lines[1:]]

    print(maximum_points(n1, m1, cards1))
