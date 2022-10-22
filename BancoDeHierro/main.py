from Cuenta import Cuenta
from Cliente import Cliente
n=None
while n!=0:
    try:
        op=int(input('''Que desea hacer? 
           0.Salir
           1.registrar Cliente
           2.consultar saldo
           3.retirar dinero
           4.recargar cuenta: '''))
        
    except TypeError:
       print('Debes digitar un numero')
    else:
        if op ==1:
            ct=input('ingrese cedula de titular de cuenta: ')
            nt=input('ingrese Nombre de titular de cuenta: ')
            at=input('ingrese Apellido de titular de cuenta: ')
            ncuenta=input('Ingrese el numero de cuenta: ')
            try:
                saldo=0
                while saldo<=0:
                    r=int(input('Ingrese el saldo de la cuenta: '))
                    if r<=0:
                        print('el saldo debe ser mayor a 0')
                    else:
                        saldo=r                  
            except TypeError:
                print('Debe digitar un numero')
            objtc=Cliente(nt,at,ct)
            Cliente.guardarCliente(objtc)
            objtcuenta=Cuenta(ncuenta,saldo,ct)
            Cuenta.guardarCuenta(objtcuenta)
            print('Cliente registrado con exito...')
        elif op ==2:
            ncuenta=input('Ingrese el numero de cuenta: ')
            Cuenta.consultarSaldo(ncuenta)
        elif op ==3:
            ncuenta=input('Ingrese el numero de cuenta: ')
            saldo=int(input('Ingrese el valor a retirar: '))
            Cuenta.retirarDinero(ncuenta,saldo)
        elif op ==4:
            ncuenta=input('Ingrese el numero de cuenta: ')
            saldo=int(input('Ingrese el valor a recargar: '))
            Cuenta.recargarCuenta(ncuenta,saldo)
        elif op==0:
            n=0
        else: print('Digito invalido, la respuesta debe estar entre el rango')
print('Fin de programa...')      
    
    

    
