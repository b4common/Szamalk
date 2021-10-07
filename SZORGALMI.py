# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#A Simple loop for exercise
#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
 #   print(x)
  #  if x == "banana":
   #     break


#Reverse a string.
#def reverse(x):
 #   return x[::-1]

#mytext = reverse("Reverse this string")
#print(mytext)


#Converts the input to Kg or Lbs.

#weight = int(input("Give me a weight: "))
#measurement = input("Kg or Lbs: ? ")
#if measurement == "Kg":
 #   converted = weight / 0.45
  #  print("Your weight in lbs: ", converted)

#elif measurement == "Lbs":
 #   converted = weight * 0.45
  #  print("Your weight in kgs: ", converted)

'''
#This is a Elevator Simulator!
# Loops through as many times as many user is set to.
user = [1,2]
current_floor = [0]
NumberOfFloors = [1, 2, 3, 4, 5, 6, 7]
for x in user :
    selected_floor = int(input("Please select a floor between 1-7: "))
    indice = [floors]
    selected_element = []
    for index in indice:
        selected_element.append(NumberOfFloors[index-1])
        print("You arrived at floor:",selected_element)
    if current_floor == 0 or current_floor[-1] == floors:
        print("Already here")
    current_floor.append(floors)
'''
def Checking():
    valasztas = input("Válasszon: ")
    valasztas = int(valasztas)
    check_float = isinstance(valasztas, float)
    valasztas = str(valasztas)
    check_string = isinstance(valasztas, str)
    if  check_float:
        print("float nem elfogadható")
    elif  check_string:
        print("string nem elfogadható")
    else:
        valasztas = int(valasztas)
    return valasztas

import math
while (True) :
    szöveg1 = 'Ön a'
    szöveg2 = 'kerület, terület számítását választotta,'
    print('Mit szeretne ?')
    print('-----------')
    print('  Négyzet kerülete, területe --> 1')
    print('  Téglalap kerülete, területe --> 2')
    print('  Rombusz kerülete, területe --> 3')
    print('  Kör kerülete, területe --> 4')
    print("  Kilépés --> 5")
    helyes_valasz = Checking()

    if helyes_valasz > 5 :
        print('Nem választotta egyik lehetőséget sem !!!')
    if helyes_valasz == 5:
        print("Ön kilépett a programból!")
        break
    while (helyes_valasz != None) :
        if helyes_valasz == 1:
            # print('Ön a négyzet kerület, terület számítását választotta,')
            print(szöveg1, 'négyzet', szöveg2)
            a = float(input('Adja meg a négyzet oldalát: '))
            K = 4 * a
            T = a ** 2
            print('A négyzet kerülete:', K, 'területe:', T)
            break
        elif helyes_valasz == 2:
            # print('Ön a téglalap kerület, terület számítását választotta,')
            print(szöveg1, 'téglalap', szöveg2)
            a = float(input('Adja meg a téglalap egyik oldalát: '))
            b = float(input('Adja meg a téglalap másik oldalát: '))
            K = 2 * (a + b)
            T = a * b
            print('A téglalap kerülete:', K, 'területe:', T)
            break
        elif helyes_valasz == 3:
            # print('Ön a rombusz kerület, terület számítását választotta,')
            print(szöveg1, 'rombusz', szöveg2)
            a = float(input('Adja meg a rombusz oldalát: '))
            alfa = float(input('Adja meg a bezárt szöget: '))
            K = 4 * a
            T = a ** 2 * (math.sin(alfa * 0.017453292519943))
            print('A rombusz kerülete:', K, 'területe:', round(T, 4))
            break
        elif helyes_valasz == 4:
            # print('Ön a kör kerület, terület számítását választotta,')
            print(szöveg1, 'kör', szöveg2)
            r = float(input('Adja meg a kör sugarát: '))
            K = 2 * r * math.pi
            T = r ** 2 * math.pi
            print('A kör kerülete:', round(K, 4), 'területe:', round(T, 4))
            break
        elif helyes_valasz < 0:
            print("Negatív szám , nem elfogadható!!")
            break





