from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
contents = contents.rstrip()
print(contents)