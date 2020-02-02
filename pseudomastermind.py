import random

list = [1, 2, 3, 4]
randList = []

a = random.choice(list)
randList.append(a)
list.remove(a)
b = random.choice(list)
randList.append(b)
list.remove(b)
c = random.choice(list)
randList.append(c)
list.remove(c)
d = random.choice(list)
randList.append(d)
list.remove(d)
#print(list)
#print(randList)

while True:
    print(""" 1. Losuj
2. Zakończ""")
    wybor = int(input())
    if wybor == 1:
        while True:
        
                while True:
                    print("Wprowadź 1. liczbę:  ")
                    liczba1 = int(input())
                    if liczba1 == randList[0]:
                        print("trafiles")
                        print("Pierwsza liczba to:", liczba1)
                        break
                    else:
                        print("Nie trafiłeś. Spróbuj ponownie")
                while True:
                    print("Wprowadź 2. liczbę:  ")
                    liczba2 = int(input())
                    if liczba2 == randList[1]:
                        print("trafiles")
                        print("Druga liczba to:", liczba2)
                        break
                    else:
                        print("Nie trafiłeś. Spróbuj ponownie")
                while True:
                    print("Wprowadź 3. liczbę:  ")
                    liczba3 = int(input())
                    if liczba3 == randList[2]:
                        print("trafiles")
                        print("Trzecia liczba to:", liczba3)
                        break
                    else:
                        print("Nie trafiłeś. Spróbuj ponownie")
                while True:
                    print("Wprowadź 4. liczbę:  ")
                    liczba4 = int(input())
                    if liczba4 == randList[3]:
                        print("trafiles")
                        print("Czwarta liczba to:", liczba4)
                        print("Wygrałeś! Twoja sekwencja liczb to:", randList)
                        break
                    else:
                        print("Nie trafiłeś. Spróbuj ponownie")
          
                        
    elif wybor == 2:
        break