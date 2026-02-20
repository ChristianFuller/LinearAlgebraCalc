def make_vector_into_ArrayMatrix_Square(vector, size):
    if len(vector) != size * size:
        raise ValueError(
            f"Vector length ({len(vector)}) does not match {size}x{size} matrix ({size*size})"
        )
    
    FinalVector = []
    tempVector = []
    index = 0
    for x in range(size):
        for y in range(size):
            tempVector.append(vector[index])
            index += 1
        FinalVector.append(tempVector)
        tempVector = []
    return FinalVector

def make_vector_into_ArrayMatrix(vector, rows, cols):
    if len(vector) != rows * cols:
        raise ValueError(
            f"Vector length ({len(vector)}) does not match "
            f"{rows}x{cols} matrix ({rows * cols})"
        )

    matrix = []
    index = 0

    #& Go through Rows 
    for r in range(rows):
        row = []
        #& Go through Columns
        for c in range(cols):
            #& Create the row to add to the matrix
            row.append(vector[index])
            index += 1
        #& Add the created row to the matrix and go to next row
        matrix.append(row)

    return matrix