year = int(input())
print(True if year % 400 == 0 and year % 100 != 0 or year % 4 == 0 else False)