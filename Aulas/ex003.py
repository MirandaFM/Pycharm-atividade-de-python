# Crie um programa que leia dois números e mostre a soma entre eles
n1 =  int (input('digite primeiro valor: '))
n2 = int (input('digite segundo valor: '))
s = n1 + n2
#print ('a soma entre' ,n1, 'e',n2, 'é', s)
print ('a soma entre {} e {} vale {}'.format(n1,n2,s))