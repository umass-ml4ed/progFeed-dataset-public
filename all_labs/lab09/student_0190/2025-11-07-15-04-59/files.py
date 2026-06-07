# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def print_stars_to_file(n):
    file = open(f"stars_{n}.txt", "w")

    for i in range(1, n+1):
            spaces = n-i
            stars = 2 * i - 1


            line = " " * spaces + "*" * stars

            file.write(line + "\n")
    file.close()

print_stars_to_file(4)


def calc_avg_from_file():
      file = open("grades.txt", "r")
      
      text = file.read()

      file.close()

      grade_list = text.split('\n')

      total = 0
      count = 0

      for grade in grade_list:
            if grade.strip() != "":
                total += float(grade)
                count += 1 
      if count == 0:
            return 0
      return total/count
      






