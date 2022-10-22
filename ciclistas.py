""" Codificar un programa en Python utilizando funciones que permita 
recibir: Nombre, edad, País, Equipo y tiempo en minutos de 
múltiples ciclistas. El software estará en la capacidad de calcular y 
mostrar en pantalla cual fue el ciclista más rápido"""
n=6
ciclistas=[]
while(n!=0):
    obj={}
    n=int(input("""elija el proceso que desea realisar:
          1.Agregar ciclista
          2.ver resultados
          0.Salir"""))
    if(n==1):
        nombre=input("Escriba el nombre: ")
        edad= input("escriba la edad: ")
        pais=input("escriba el pais: ")
        tiempo=int(input("Escriba el tiempo del ciclista en minutos: "))
        obj={
            "nombre":nombre,
            "edad":edad,
            "pais":pais,
            "tiempo":tiempo
        }
        ciclistas.append(obj)
    elif n == 2 :
        
        c= ciclistas[0]
        for i in range(len(ciclistas)):
            
            if ciclistas[i]['tiempo']<c['tiempo']:
                c=ciclistas[i]
                
        print(f"el ciclista mas rapido es: {c['nombre']} con un tiempo de: {c['tiempo']}")
        
        
        