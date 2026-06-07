# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
	filename = f"stars_{n}.txt"
	with open(filename, 'w', encoding='utf-8') as f:
		for i in range(1, n + 1):
			leading_spaces = n - i
			stars = 2 * i - 1
			line = (' ' * leading_spaces) + ('*' * stars)
			f.write(line + '\n')

def calc_avg_from_file():
	filename = "grades.txt"
	with open(filename, 'r', encoding='utf-8') as f:
		text = f.read()
	parts = text.split('\n') if text else []
	numbers = [float(s) for s in parts if s.strip() != ""]
	if not numbers:
		return 0.0
	return sum(numbers) / len(numbers)
