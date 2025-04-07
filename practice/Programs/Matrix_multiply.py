arr1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

arr2 = [
    [2, 1, 4, 1 ],
    [5, 0, 0, 2 ],
    [10, 1, 2,4 ]
]

result = [
    [0, 0, 0,0],
    [0, 0, 0,0],
    [0, 0, 0,0]
]
for i in range(len(arr1)): # arr1 rows considers
    for j in range(len(arr2[0])): # arr2 columns considers
        for k in range(len(arr2)): # arr1 columns considers
            result[i][j] = arr1[i][k] * arr2[k][j]

print(result)
print("\nProper form output:\n")
#to get output in proper form
for i in result:
    print(i)
