# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
        if n == 0:
                return None
        else:

                check = True
                file = open ('./stars_' + str(n) + '.txt', 'x')
                with open ('./stars_' + str(n) + '.txt', 'w') as file:
                        for i in range(n):

                                        if i == 0:
                                                file.write((' ' * (n-1)) + '*\n')
                                        elif i == 1:
                                                file.write((' ' * (n-2)) + '***\n')
                                        elif i == 2:
                                                file.write((' ' * (n-3)) + '*****\n')
                                        elif i == 3:
                                                file.write((' ' * (n-4)) + '*******\n')
                                        elif i == 4:
                                                file.write((' ' * (n-5)) + '*********\n')
                                        elif i == 5:
                                                file.write((' ' * (n-6)) + '***********\n')
                                        elif i == 6:
                                                file.write((' ' * (n-7)) + '*************\n')
                                        elif i == 7:
                                                file.write((' ' * (n-8)) + '***************\n')
                                        elif i == 8:
                                                file.write((' ' * (n-9)) + '*****************\n')
                                        elif i == 9:
                                                file.write((' ' * (n-4)) + '*******************\n')
                                        elif i == n:
                                                file.write((' ' * (2*n-1)))

print_stars_to_file(1)

def calc_avg_from_file():
        try:
                with open('grades.txt', 'r') as f:
                        content = f.read()
                        lines = content.split('\n')
                        grades = [float(line) for line in lines if line]
                        if not grades:
                                return 0.0
                        else:
                                average = sum(grades) / len(grades)
                                return average
        except FileNotFoundError:
                print("Error: 'grades.txt' not found.")
                return None
        except ValueError:
                print("Error: 'grades.txt' contains non-numeric data.")
                return None

