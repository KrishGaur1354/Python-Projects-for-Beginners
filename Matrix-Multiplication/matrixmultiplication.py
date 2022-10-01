matrix_a = []
matrix_b = []

# Choose order of matrix
print(">>> Input order of matrix (MxN)")
row_a = int(input("Insert amount of rows for matrix A: "))
column_a = int(input("Insert amount of columns for matrix A: "))
row_b = column_a
print(f"Rows for matrix B = columns for matrix A: {row_b}")
column_b = int(input("Insert amount of columns for matrix B: "))
print(f"Matrix A {row_a}x{column_a}")
print(f"Matrix B {row_b}x{column_b}")
print('-' * 20)

# Input elements of matrix A and B
print(">>> Input elements of matrix A")
for i in range(row_a):
    matrix_a.append([])
    for j in range(column_a):
        matrix_a[i].append(int(input(f"A {i + 1}, {j + 1}: ")))
print('-' * 20)
print(">>> Input elements of matrix B")
for i in range(row_b):
    matrix_b.append([])
    for j in range(column_b):
        matrix_b[i].append(int(input(f"B {i + 1}, {j + 1}: ")))
print('-' * 20)

# Show matrix A and B
print(">>> Calculation Results")  # Is put here to make output tidier
print("A:")
for i in range(row_a):
    print('\t[', end=' ')
    for j in range(column_a):
        print(f"{matrix_a[i][j]}", end=' ')
    print(']\n', end='')
print("B:")
for i in range(row_b):
    print('\t[', end=' ')
    for j in range(column_b):
        print(f"{matrix_b[i][j]}", end=' ')
    print(']\n', end='')

result_matrix = []

row_a = len(matrix_a)
column_a = len(matrix_a[0])
column_b = len(matrix_b[0])

# Calculate matrix multiplication
for i in range(row_a):
    result_matrix.append([])
    for j in range(column_b):
        result = 0
        for k in range(column_a):
            result += matrix_a[i][k] * matrix_b[k][j]
        result_matrix[i].append(result)

# Show results of matrix A * B
print("A * B:")
for i in range(row_a):
    print('\t[', end=' ')
    for j in range(column_b):
        print(f"{result_matrix[i][j]}", end=' ')
    print(']\n', end='')
