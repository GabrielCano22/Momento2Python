num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
numMayor = lambda n1,n2 :  1 if n1 > n2 else -1
mostrarResultado = lambda : print(f'El segundo numero es mayor') if numMayor(num1,num2) == -1 else print('El primer numero es mayor')
mostrarResultado()