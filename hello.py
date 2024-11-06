def calculate_area(length, width):
    # Use multiplication for calculating area
    area = length * width
    return area

try:
    # Get user inputs and convert to integers
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    
    # Call function and print area
    print("The area of the rectangle is:", calculate_area(length, width))

except ValueError:
    # Handle non-numeric input
    print("Please enter valid numbers for length and width.")
