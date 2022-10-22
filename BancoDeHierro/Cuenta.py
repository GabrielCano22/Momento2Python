cuentas=[]
class Cuenta:
     
    def __init__(self,numeroCuenta,saldo,cedula):
        self.numeroCuenta=numeroCuenta
        self.saldo=saldo
        self.cedula=cedula
    
    def guardarCuenta(self):
        cuenta={}
        cuenta={
            "cedula":self.cedula,
            "numeroCuenta":self.numeroCuenta,
            "saldo":self.saldo
        }
        cuentas.append(cuenta)
    
    def consultarSaldo(cuenta):
        for i in cuentas:
            if i['numeroCuenta']==cuenta:
                s=i['saldo']
                print(f'su saldo es: {s}')
            
    def retirarDinero(cuenta,valor):
        for i in cuentas:
            print(i['numeroCuenta'])
            if i['numeroCuenta']==cuenta:
                
                if i['saldo']<valor:    
                    print('Saldo insuficiente! cupo disponible',s)
                elif i['saldo']>=valor:
                    i['saldo']-=valor
                    s=i['saldo']
                    print('Exito en retiro... nuevo saldo: ',s)
                
    def recargarCuenta(cuenta,valor):
        for i in cuentas:
            print(i['numeroCuenta'])
            if i['numeroCuenta']==cuenta:
                if valor<=0:
                    print('valor a abonar invalido')
                else:
                    i['saldo']+=valor
                    s=i['saldo']
                    print(f'Exito en recarga...su nuevo saldo es: {s}')
                    