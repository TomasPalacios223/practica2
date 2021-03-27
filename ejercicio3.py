texto= """ python es el mejor lenguaje de programacion """

cadena= input("ingrese una letra ")
if cadena.isupper():
  cadena=cadena.lower()
texto= texto.split( )
if(cadena < "a" or cadena > "z") :
    print("error, no ingresaste una letra")
else:   
  for palabra in texto:
    if(palabra[0] == cadena ):
      print("las palabras que empiezan con esa letra son :", palabra)
 
      