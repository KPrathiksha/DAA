def strassen_matrix_multiply(A, B):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]
    P1 = (a + d) * (e + h)
    P2 = (c + d) * e
    P3 = a * (f - h)
    P4 = d * (g - e)
    P5 = (a + b) * h
    P6 = (c - a) * (e + f)
    P7 = (b - d) * (g + h)
    p11 = P1 + P4 - P5 + P7
    p12 = P3 + P5
    p21 = P2 + P4
    p22 = P1 - P2 + P3 + P6
    C = [[p11, p12], [p21, p22]]
    return C
A = [[1, 7], [3, 5]]
B = [[6, 8], [4, 2]]
C = strassen_matrix_multiply(A, B)
print("The product matrix C is:")
for row in C:
    print(row)
