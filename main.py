word = ""
n = int(input('choose your number: \n '))
if n % 3 == 0:
    word += 'Pling'
if n % 5 == 0:
    word += 'Plang'
if n % 7 == 0:
    word += 'Plong'
if n % 3 != 0 or n % 5 != 0 or n % 7 != 0:
    word += str(n)
print(word)