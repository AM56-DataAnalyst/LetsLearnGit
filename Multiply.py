a = 4
b = 5
print("The product is :",a*b)

def print_multiplication_table(start, end):
    # Open a file to write the tables
    with open('multiplication_tables_100_199.txt', 'w') as f:
        # Iterate through each number from 100 to 199
        for num in range(start, end + 1):
            f.write(f"\nMultiplication Table for {num}:\n")
            f.write("=" * 30 + "\n")
            
            # Generate multiplications from 1 to 10
            for i in range(1, 11):
                result = num * i
                f.write(f"{num} × {i} = {result}\n")
            
            f.write("\n")  # Add extra line between tables

# Generate tables for numbers 100-199
print_multiplication_table(100, 199)