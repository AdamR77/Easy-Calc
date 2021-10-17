#import logging
#logging.basicConfig(level=logging.DEBUG)

print("podaj działanie które chcesz wykonać: ")
print(" 1. dodawanie")
print(" 2. odejmowanie")
print(" 3. mnożenie")
print(" 4. dzielenie")
choice = int(input("twój wybór: "))
print("")

def _sum(args):
  sum_result = 0
  for arg in args:
    sum_result += float(arg)
  return sum_result

def _subtract(args):
  subtract_result = float(args[0])
  for x in range(1,len(args)):
      subtract_result -= float(args[x]) 
  return subtract_result

def _multiple(args):
  multiple_result = args[0]
  for x in range(1, len(args)):
    multiple_result = multiple_result * args[x]
  return multiple_result

def _divide(args):
  divide_result = args[0]
  for x in range(1, len(args)):
    divide_result = divide_result / args[x]
  return divide_result

def taking_args():
  counter = 1
  arg = 1
  numbers = []
  while arg != "end":
    arg = input(f"Podaj liczbe {counter}: ")
    numbers.append(arg)
    counter += 1
  numbers.remove("end")
  numbers = [float(x) for x in numbers]
  args = tuple(numbers)
  return args 



if choice == 1:
  print("dodawanie: liczba.1 + liczba.2 + ... end (koniec -> wynik) ")
  args = taking_args()
  print(_sum(args))


if choice == 2:
  print("odejmowanie: liczba.1 - liczba.2 - ...  koniec (end) ")
  args = taking_args()
  print(_subtract(args))

if choice == 3:
  print("mnożenie: liczba.1 - liczba.2 - ...  koniec (end) ")
  args = taking_args()
  print(_multiple(args))

if choice == 4:
  print("dzielenie: liczba.1 - liczba.2 - ...  koniec (end) ")
  args = taking_args()
  print(_divide(args))





