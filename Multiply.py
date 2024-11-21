a = 4
b = 5
print("The product is :",a*b)
def print_multiplication_table(start, end):
    for num in range(start, end + 1):
        print(f"\nMultiplication Table for {num}")
        print("=" * 25)
        
        for i in range(1, 11):
            result = num * i
            print(f"{num} × {i:2d} = {result}")
        
        print()  # Extra line between tables

print_multiplication_table(1, 101)