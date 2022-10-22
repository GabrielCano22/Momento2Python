class Cliente:
    datos=[]
    def __init__(self,nombre,apellido,cedula):
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        
    def guardarCliente(self):
        cliente={}
        cliente[self.cedula]={
            "cedula":self.cedula,
            "nombre":self.nombre,
            "apellido":self.apellido
        }
        self.datos.append(cliente)
        