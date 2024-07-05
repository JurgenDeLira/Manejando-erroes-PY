edad = input('Ingresa tu edad: ')
try:
  age = int(age)
except ValueError:
  print('Lo siento, ese no es número válido.')