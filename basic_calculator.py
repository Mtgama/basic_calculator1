from tkinter import W
import pyfiglet
from termcolor2  import colored
esm = "calculator"
mse = pyfiglet.figlet_format(esm)
mse = colored(mse , color="red")
print(mse)
print("wellcom to my calculator! \n")
select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: quit \n select option:')
ask = True
while ask:
 if select == "1":
    print('insert first number :')
    number_1 = int(input())
    print("insert secent number")
    number_2 = int(input())
    x = number_1 + number_2
    print(f"your solve is : {x} \n")
    soal = input(" continue or break? \n n : braek \n y : continue \n m : main menu \n")
    if soal == "n":
      break
    elif soal == "m":
      select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: quit \n select option:')

      print(select)
    elif soal == "y":
      continue
    else:
      print("your select number not avalebale! app exit automatic")
      break

 elif select == "2":
    print('insert first number :')
    number_1 = int(input())
    print("insert secent number")
    number_2 = int(input())
    x = number_1 * number_2
    print(f"your solve is : {x}")
    soal = input(" continue or break? \n n : braek \n y : continue  \n m : main menu \n")
    if soal == "n":
      break
    elif soal == "m":
      select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: quit \n select option:')

      print(select)
    elif soal == "y":
      continue
    else:
      print("your select number not avalebale! app exit automatic")
      break

 elif select == "3":
    print('insert first number :')
    number_1 = int(input())
    print("insert secent number")
    number_2 = int(input())
    x = number_1 / number_2
    print(f"your solve is : {x}")
    soal = input(" continue or break? \n n : braek \n y : continue   \n m : main menu \n")
    if soal == "n":
      break
    elif soal == "m":
      select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: quit \n select option:')

      print(select)
    elif soal == "y":
      continue
    else:
      print("your select number not avalebale! app exit automatic")
      break

 elif select == "4":
    print('insert first number :')
    number_1 = int(input())
    print("insert secent number")
    number_2 = int(input())
    x = number_1 - number_2
    print(f"your solve is : {x}")
    soal = input(" continue or break? \n n : braek \n y : continue  \n m : main menu \n")
    if soal == "n":
      break
    elif soal == "m":
      select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: quit \n select option:')

      print(select)
    elif soal == "y":
      continue
    else:
      print("your select number not avalebale! app exit automatic")
      break

 elif select == "5":
    print("okey! see you later!")
    break
 else:
   print("your select number not avalebale! app exit automatic")
   break



print(select)
