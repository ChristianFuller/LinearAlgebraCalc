
def multiply_two_matrix(Matrix1, Matrix2):

    # 2 2 2 2
    # 2 2 2 2

    # 1 2
    # 1 2 
    # 1 2 

    #& Matrix is like [[1,2,3], [4,5,6]] Each index is a row
    rows1 = len(Matrix1)
    
    #& Matrix is like [[1,2,3], [4,5,6]] Lengh of 0 is the column length
    cols1 = len(Matrix1[0])

    rows2 = len(Matrix2)
    cols2 = len(Matrix2[0])

    #& Make sure you can multiply
    if cols1 != rows2:
        raise ValueError("Matrix1 columns must equal Matrix2 rows")

    result = []

    #& go through the rows length
    for row in range(rows1):
        row_result = []
        #&Go through the column 2 length
        for column2index in range(cols2):
            total = 0
            #&Go through the column 1 length
            for column1index in range(cols1):
            #M1
            # a1 b1
            # c1 d1 
            # e1 f1

            #M2
            # a2 b2 c2 d2
            # e2 f2 g2 h2

            
            #When
            # row = 0
            # column1index = 0
            # column2index = 0

            #M1[0][0] = a1 * M2[0][0] = a2
            
            # add 1 to column1index
            #M1[0][1] = b1 * M2[1][0] = e2

            #Now add one to col2index
            #M1[0][0] = a1 * M2[0][1] = b2
            
            # add 1 to column1index
            #M1[0][1] = b1 * M2[1][1] = f2

                print(f"{Matrix1[row][column1index]} * {Matrix2[column1index][column2index]}")
                total += Matrix1[row][column1index] * Matrix2[column1index][column2index]
            row_result.append(total)
        result.append(row_result)

    return result
