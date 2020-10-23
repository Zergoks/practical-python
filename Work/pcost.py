# pcost.py
#
# Exercise 1.27
file_path = './Data/portfolio.csv'
result = 0

with open(file_path, 'rt') as file:
    for line in file:
        try:
            data = line.split(',')
            result += int(data[1]) * float(data[2])
        except ValueError:
            pass
print(result)

