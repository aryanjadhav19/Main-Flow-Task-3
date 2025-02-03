def table_of_number(n):
    print(f"Multiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def swap_two_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")

def check_substring(s1, s2):
    if s2 in s1:
        print(f"'{s2}' is a substring of '{s1}'")
    else:
        print(f"'{s2}' is NOT a substring of '{s1}'")

def decimal_to_binary(n):
    print(f"Binary representation of {n}: {bin(n)[2:]}")

def matrix_addition(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    print("Matrix Addition Result:")
    for row in result:
        print(row)

def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    print("Matrix Multiplication Result:")
    for row in result:
        print(row)

def find_second_largest(lst):
    if len(lst) < 2:
        print("List must have at least two elements.")
        return
    lst = list(set(lst))  # Remove duplicates
    if len(lst) < 2:
        print("List has only one unique element.")
        return
    lst.sort(reverse=True)
    print(f"Second largest element: {lst[1]}")

def check_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        print(f"'{str1}' and '{str2}' are anagrams.")
    else:
        print(f"'{str1}' and '{str2}' are NOT anagrams.")

def main():
    while True:
        print("\nMenu:")
        print("1. Table of a Number")
        print("2. Swap Two Numbers")
        print("3. Check Substring")
        print("4. Decimal to Binary")
        print("5. Matrix Addition")
        print("6. Matrix Multiplication")
        print("7. Find Second Largest")
        print("8. Check Anagram")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter a number to print the multiplication table: "))
            table_of_number(n)
        elif choice == 2:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            swap_two_numbers(a, b)
        elif choice == 3:
            s1 = input("Enter the main string: ")
            s2 = input("Enter the substring: ")
            check_substring(s1, s2)
        elif choice == 4:
            n = int(input("Enter a decimal number: "))
            decimal_to_binary(n)
        elif choice == 5:
            matrix1 = []
            matrix2 = []
            rows = int(input("Enter number of rows for matrices: "))
            cols = int(input("Enter number of columns for matrices: "))

            print("Enter elements for first matrix:")
            for i in range(rows):
                row = list(map(int, input(f"Enter row {i + 1} (space separated): ").split()))
                matrix1.append(row)

            print("Enter elements for second matrix:")
            for i in range(rows):
                row = list(map(int, input(f"Enter row {i + 1} (space separated): ").split()))
                matrix2.append(row)

            matrix_addition(matrix1, matrix2)
        elif choice == 6:
            matrix1 = []
            matrix2 = []
            rows1 = int(input("Enter number of rows for first matrix: "))
            cols1 = int(input("Enter number of columns for first matrix: "))
            rows2 = int(input("Enter number of rows for second matrix: "))
            cols2 = int(input("Enter number of columns for second matrix: "))

            if cols1 != rows2:
                print(
                    "Matrix multiplication is not possible. Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
                continue

            print("Enter elements for first matrix:")
            for i in range(rows1):
                row = list(map(int, input(f"Enter row {i + 1} (space separated): ").split()))
                matrix1.append(row)

            print("Enter elements for second matrix:")
            for i in range(rows2):
                row = list(map(int, input(f"Enter row {i + 1} (space separated): ").split()))
                matrix2.append(row)

            matrix_multiplication(matrix1, matrix2)
        elif choice == 7:
            lst = list(map(int, input("Enter a list of numbers (space separated): ").split()))
            find_second_largest(lst)
        elif choice == 8:
            str1 = input("Enter the first string: ")
            str2 = input("Enter the second string: ")
            check_anagram(str1, str2)
        elif choice == 9:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()