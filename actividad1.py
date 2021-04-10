alumnos = '''
    "Agustin",
    "Alan",
    "Andrés",
    "Ariadna",
    "Bautista",
    "CAROLINA",
    "CESAR",
    "David",
    "Diego",
    "Dolores",
    "DYLAN",
    "ELIANA",
    "Emanuel",
    "Fabián",
    "Facundo",
    "Facundo",
    "FEDERICO",
    "FEDERICO",
    "GONZALO",
    "Gregorio",
    "Ignacio",
    "Jonathan",
    "Jonathan",
    "Jorge",
    "JOSE",
    "JUAN",
    "Juan",
    "Juan",
    "Julian",
    "Julieta",
    "LAUTARO",
    "Leonel",
    "LUIS",
    "Luis",
    "Marcos",
    "María",
    "MATEO",
    "Matias",
    "Nicolás",
    "NICOLÁS",
    "Noelia",
    "Pablo",
    "Priscila",
    "TOMAS",
    "Tomás",
    "Ulises",
    "Yanina",
    '''

eval1 = '''
 81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
 '''

eval2 = '''
 30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
 '''

alumnos = alumnos.replace("\"", " ").replace(",", " ").split()


eval1 = eval1.replace(",", " ").split()
eval2 = eval2.replace(",", " ").split()

calcular_notas_finales = list(map(lambda eval1, eval2: int(eval1)+int(eval2), eval1, eval2))


def calcular_promedio(calcular_notas_finales):
    """esta funcion calcula el promedio de las notas finales"""

    return sum(calcular_notas_finales)/len(alumnos)


def opcion1(calcular_notas_finales, calcular_promedio):
    diccionario = {}

    for x in range(len(alumnos)):
        diccionario[alumnos[x]] = int(eval1[x]) + int(eval2[x])

    print(f'     Nombres           Eval1            Eval2            Sumas')

    for pos in range(len(alumnos)):
        print('%2s' % pos, ' ', alumnos[pos].ljust(11), '%8s' % eval1[pos], ' %15s' % eval2[pos], ' %16s ' % diccionario[alumnos[pos]])

    print('suma total de notas :', sum(calcular_notas_finales))
    print('promedio general de las notas', calcular_promedio(calcular_notas_finales))
   

def opcion2():
    cond = int(input("""Seleccione sobre que valores se realizará el reporte
            1)Eval1
            2)Eval2
            3)Suma de ambas notas
            para sair ingrese 0
            """))
    while True:
        valor1=int(input("ingrese el valor inferior del rango"))
        valor2=int(input("ingrese el valor superior del rango"))
        if(cond == 1):
            suma_notas=[(alumno,int(nota1)) for alumno,nota1 in zip(alumnos,eval1)]
            suma_notas= filter(lambda x: x[1]>=valor1 and x[1]<=valor2,suma_notas)
            print(list(suma_notas))
        elif(cond == 2):
            suma_notas=[(alumno,int(nota2)) for alumno,nota2 in zip(alumnos,eval2)]
            suma_notas= filter(lambda x: x[1]>=valor1 and x[1]<=valor2,suma_notas)
            print(list(suma_notas))
        elif(cond == 3):
            suma_notas=[(alumno,int(nota1)+int(nota2)) for alumno,nota1,nota2 in zip(alumnos,eval1,eval2)]
            suma_notas= filter(lambda x: x[1]>=valor1 and x[1]<=valor2,suma_notas)
            print(list(suma_notas))
        if cond: 0
        break 


def opcion3():
    opc=int(input(""" Seleccione la opción por la cual quiere ordenar los datos
         1)nombre.
         2)nota1.
         3)nota2.
         4)suma de ambas notas.
        para salir ingrese 0.
    """))
    lista=[(alumno.lower(),int(nota1),int(nota2),int(nota1)+int(nota2)) for alumno,nota1,nota2 in zip(alumnos,eval1,eval2)]
    while True:
        if(opc==1):
            l=sorted(lista,key=lambda lista: lista[0])
            print(l)
        if(opc==2):
            l=sorted(lista,key=lambda lista: lista[1])
            print(l)    
        if(opc==3):
             l=sorted(lista,key=lambda lista: lista[2])
             print(l)   
        if(opc==4):
            l=sorted(lista,key=lambda lista: lista[3])
            print(l)     
        if opc:0
        break


def menu():
    cond = int(input(""" Seleccione una opcion del menu :
          1)Calcular el promedio de las notas finales de todxs lxs estudiantes.
          2)realizar reporte
          3)ordenar los datos, eligiendo un criterio
          4)salir del menu con 0
          """))    
    while True:
        if(cond == 1):
            opcion1(calcular_notas_finales, calcular_promedio)    
        elif(cond==2):
            opcion2()
        elif(cond==3):
            opcion3()
        if cond:0
        break

menu()



    