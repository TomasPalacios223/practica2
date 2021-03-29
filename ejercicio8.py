nombres_1 =  ''''Agustin','Alan','Andrés','Ariadna','Bautista','CAROLINA','CESAR','David','Diego','Dolores','DYLAN','ELIANA','Emanuel','Fabián','Facundo','Facundo','FEDERICO','FEDERICO','GONZALO','Gregorio','Ignacio','Jonathan','Jonathan','Jorge','JOSE','JUAN','Juan','Juan','Julian','Julieta','LAUTARO','Leonel','LUIS','Luis','Marcos','María','MATEO','Matias','Nicolás','NICOLÁS','Noelia','Pablo','Priscila','TOMAS','Tomás','Ulises','Yanina '''
nombres_2 =  ''''Agustin','AGUSTIN','Agustín','Ailen','Alfredo','Amalia','Ariana','Bautista','Braian','Carla','CESAR','Daniel','Diego','ELIANA','Facundo','Facundo','Facundo','Facundo','Federico','Federico','Flavia','Francisco','Germán','Guido','GUSTAVO','Hilario','Ignacio','IVAN','Jimmy','Joaquín','Jose','Josue','JUAN','Juan','Laura','LAURA','Lautaro','Lautaro','Ludmila','Marcos','Marcos','MARIANELA','MARTIN','MATEO','Mateo','Matias','MAURO','Maximiliano','NESTOR','Nicolas','Pedro','Ramiro','Sofía','Tobias','Tomás','Tomás','Ulises','Yanina' '''  


nombres_1=nombres_1.replace("' "," ")
nombres_2=nombres_2.replace("' "," ")
nombres_1=nombres_1.lower().split(',')
nombres_2=nombres_2.lower().split(',')

nombres= [nombre for nombre in nombres_1 if nombre in nombres_2]
print(nombres)

notas1='''81,60,72,24,15,91,12,70,29,42,16,3,35,67,10,57,11,69,12,77,13,86,48,65,51,41,87,43,10,87,91,15,44,85,73,37,42,95,18,7,74, 60,9,65,93,63,74'''

notas2='''30,95,28,84,84,43,66,51,4,11,58,10,13,34,96,71,86,37,64,13,8,87,14,14,49,27,55,69,77,59,57,40,96,24,30,73,95,19,47,15,31,39,15,74,33,57,10'''
notas1=notas1.split(',')
notas2=notas2.split(',')
diccionario={}

for i in range (len(nombres_1)):
    diccionario[nombres_1[i]]= int(notas1[i])+ int(notas2[i])

print(f'     nombre    evaluacion1     evaluacion2           total')

cont=0
for nombre in range(len (nombres_1)):
    print('%2s' % cont,' %2s ' % nombres_1[nombre].ljust(9),'%12s ' % notas1[nombre].ljust(9),' %12s' % notas2[nombre].ljust(9) ,' %12s ' %  diccionario[nombres_1[nombre]])
    cont+=1

