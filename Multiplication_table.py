def multiplication_table(size):
    table = []
    for num in range(1, size + 1):
        row = []
        for colum in range(1, size + 1):
            row.append(num * colum)
        table.append(row)
    return table
