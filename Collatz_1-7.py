'''Evirir the dragon has a list of n integers a1, a2,…, an. Evirir will repeat the following procedure k times: 

For each integer ai in the list:
If ai is even, replace ai with (ai)/2. 
Otherwise, replace ai with 3ai+1.

In the end, what is the sum of all integers in the list?

Input Format:
The first line consists of two integers n
 and k (1≤n≤1000, 1≤k≤1000). Then n
 integers follow: a1, a2…, an (1≤ai≤104).

Output Format:
Output a single integer, the sum of the integers in the final list.'''

#Code below using file handling for many data items.
#One algorithm works for all the 7 tasks.

# Read the input data from the file
with open(r"C:\Users\ASUS\OneDrive\Miscellaneous\Documents\IGCSE Computer science\MCC data.txt", 'r') as file:

    n, k = map(int, file.readline().split())
    a = list(map(int, file.readline().split()))

# Apply the transformations
for _ in range(k):
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] //= 2
        else:
            a[i] = 3 * a[i] + 1

# Calculate the sum of the integers in the final list
sum_of_integers = sum(a)
print(sum_of_integers)

