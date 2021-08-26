x = [[1,2,3,4],[5,6,7,8],[5,6,7,8],[1,2,3,4]]
y = [[1,2,3,4],[5,6,7,8],[5,6,7,8],[1,2,3,4]]

## Add validation step that x row size == y columns.
n = len(x)
first_row_len = len(x[0])  # Allows us to multiply matrices of any length.
c = [[0]*n for i in range(n)]

for i in range(n):
  for j in range(n):
    for k in range(first_row_len):
      c[i][j] = c[i][j] + x[i][k]*y[k][j]
  
print (c)