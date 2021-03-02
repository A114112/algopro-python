# Tahun Kabisat

def main():
  year = int(input())
  if year % 400 == 0:
      print('is_leap_year')
  elif year % 100 == 0:
      print('not_leap_year')
  elif year % 4 == 0:
      print('is_leap_year')
  else:
      print('not_leap_year')

if __name__ == '__main__':
  main()
