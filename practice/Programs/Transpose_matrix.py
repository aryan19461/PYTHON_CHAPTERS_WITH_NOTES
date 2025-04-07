arr = [
    [1,2,3],
    [4,5,6],
  ]
transpose = [
    [0,0],
    [0,0],
    [0,0],
]

for i in range(len(arr)) :
    for  j in range(len(arr[0])):
        transpose[j][i] = arr[i][j]
    
print(transpose)