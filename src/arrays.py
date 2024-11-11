print("Arrays")
print("1. Creating an array")
array = [1, 2, 3, 4, 5]
print(array)

print("2. Accessing elements in an array")
print("The first element is: " + str(array[0]))
print("The last element is: " + str(array[-1]))

print("3. Modifying elements in an array")
array[0] = 10
print("The modified array is: " + str(array))

print("4. Adding elements to an array")
array.append(6)
print("The array with the added element is: " + str(array))

print("5. Removing elements from an array")
array.pop()
print("The array with the last element removed is: " + str(array))

print("6. Iterating over an array")
for element in array:
    print(element)

print("7. Checking if an element is in an array")
if 3 in array:
    print("3 is in the array")
else:
    print("3 is not in the array")

print("8. Getting the length of an array")
print("The length of the array is: " + str(len(array)))

print("9. Slicing an array")
sliced_array = array[1:3]
print("The sliced array is: " + str(sliced_array))

print("10. Copying an array")
copied_array = array.copy()
print("The copied array is: " + str(copied_array))

print("11. Clearing an array")
array.clear()
print("The cleared array is: " + str(array))

print("12. Creating a multidimensional array")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)

print("13. Accessing elements in a multidimensional array")
print("The element in the second row and third column is: " + str(matrix[1][2]))

print("14. Modifying elements in a multidimensional array")
matrix[1][2] = 10
print("The modified matrix is: " + str(matrix))

print("15. Adding rows to a multidimensional array")
matrix.append([11, 12, 13])
print("The matrix with the added row is: " + str(matrix))

print("16. Removing rows from a multidimensional array")
matrix.pop()
print("The matrix with the last row removed is: " + str(matrix))

print("17. Iterating over a multidimensional array")
for row in matrix:
    for element in row:
        print(element)

print("18. Checking if an element is in a multidimensional array")
if [4, 5, 6] in matrix:
    print("[4, 5, 6] is in the matrix")
else:
    print("[4, 5, 6] is not in the matrix")

print("19. Getting the length of a multidimensional array")
print("The number of rows in the matrix is: " + str(len(matrix)))

print("20. Slicing a multidimensional array")
sliced_matrix = matrix[1:6]
print("The sliced matrix is: " + str(sliced_matrix))

print("21. Copying a multidimensional array")
copied_matrix = [row.copy() for row in matrix]
print("The copied matrix is: " + str(copied_matrix))

print("22. Clearing a multidimensional array")
matrix.clear()

print("23. Creating an empty array")
empty_array = []

print("24. Checking if an array is empty")
if not empty_array:
    print("The array is empty")

print("25. Creating an array with a specific length")
length = 5
array = ["a"] * length
print("The array with a specific length is: " + str(array))