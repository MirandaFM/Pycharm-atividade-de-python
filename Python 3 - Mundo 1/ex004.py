 # Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele
a = input ('Digite algo: ')
print ('O  tipo primitivo desse valor é ',type(a))
print ('Só tem espaço?',a.isspace())
print('È um número',a.isnumeric())
print ('È alfabético?',a.isalpha())
print ('É alfanumérico?',a.isalnum())
print ('Está em maiúsculas?',a.isupper())
print ('Está em minúsculoas',a.islower())
print ('Está capitalizada?',a.istitle())
