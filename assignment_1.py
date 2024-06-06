# Create lower triangular, upper triangular and pyramid containing the "*" character.

# Function to create lower triangular
def lower_triangular(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()

# Function to create upper triangular
def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if i <= j:
                print("*", end="")
            else:
                print(" ", end="")
        print()    

# Function to create pyramid

def pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()




print("Lower Triangular")
lower_triangular(4)
print("\nUpper Triangular")
upper_triangular(4)
print("\nPyramid")
pyramid(4)
