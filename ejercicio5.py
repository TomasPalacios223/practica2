texto= input("ingrese una frase ")
palab=input("ingrese una palabra a buscar en la frase ")
cantidad=0

texto=texto.lower()
palab=palab.lower()

texto=texto.split( )
for palabra in texto:
  if (palabra == palab):
      cantidad+=1

print('la cantidad de veces que aparece la palabra ingresada en el texto es: ',cantidad)

