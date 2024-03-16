def PrintTriangularNumbers(n):
    for i in range(1, n + 1):
        triangular_number = i * (i + 1) // 2
        print(i, "\t", triangular_number)

PrintTriangularNumbers(5)
