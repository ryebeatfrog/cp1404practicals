name = input("filename: ")
FILENAME = f'{name}.txt'
in_file = open(FILENAME, 'r') as f:
for line in in_file():
    number_of_lines = sum(1 for line in f)
print(number_of_lines)
