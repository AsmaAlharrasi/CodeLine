print("Welcome to the Menu-Based Program!")

while True:
    print("\nPlease select an option:")
    print("1. Print Pattern")
    print("2. Rotate Array")
    print("3. Help")
    print("4. Exit")
    
    option = input("Option: ")
    
    if option == '1':
        n = int(input("Enter a positive number: "))
        for i in range(n, 0, -1):
            print('*' * i)
    elif option == '2':
        n = int(input("Enter the number of elements (n): "))
        k = int(input("Enter the number of steps (k): "))
        arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
        k = k % n
        rotated_arr = arr[-k:] + arr[:-k]
        print("Output:", rotated_arr)
    elif option == '3':
        print("--- Help ---")
        print("Option 1: Print a pattern with 'n' rows of decreasing asterisks.")
        print("Option 2: Rotate an array of 'n' elements to the right by 'k' steps.")
        print("Option 3: Display this help message.")
        print("Option 4: Exit the program.")