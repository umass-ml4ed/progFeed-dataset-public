# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    # Construct the filename based on the parameter n
    filename = f"stars_{n}.txt"
    
    try:
        # Open the file in write mode
        with open(filename, 'w') as f:
            # Loop through each line from 1 to n
            for i in range(1, n + 1):
                # Calculate number of leading spaces
                spaces = n - i
                # Calculate number of stars (2*i - 1)
                stars = 2 * i - 1
                # Create the line (spaces first, then stars)
                line = ' ' * spaces + '*' * stars
                # Write the line to the file with a newline
                f.write(line + '\n')
    except Exception as e:
        print(f"Error occurred when writing to {filename}: {e}")

def calc_avg_from_file():
    try:
        # Open the grades.txt file in read mode
        with open('grades.txt', 'r') as f:
            # Read the entire content into a string
            text = f.read()

            # Split the text into a list of grade strings
            grade_strings = text.split('\n')

            # Convert each grade string into a float
            grades = [float(g) for g in grade_strings]

            # Calculate the average
            average = sum(grades) / len(grades)

            # Return the average
            return average
    except FileNotFoundError:
        print("Error: grades.txt file not found.")
        return None
    except ValueError:
        print("Error: File contains invalid grade data.")
        return None
