
frase="""Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaríaautomatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple computadoras."""

frase=frase.split(  )

contador = { }


for palabra in frase:
  palabra=palabra.strip(',').strip('. ')
  if( palabra not in contador ):
      contador[palabra]= 1
  else:
     contador[palabra]+= 1

for c,v in contador.items():
    if((v==1 )and (c.islower())):
       print(c )

print(contador)
