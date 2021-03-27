texto= """NumPy is the fundamental package needed for scientific computing with Python.

    Website: https://www.numpy.org
    Documentation: https://numpy.org/doc
    Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
    Source code: https://github.com/numpy/numpy
    Contributing: https://www.numpy.org/devdocs/dev/index.html
    Bug reports: https://github.com/numpy/numpy/issues
    Report a security vulnerability: https://tidelift.com/docs/security

It provides:

    a powerful N-dimensional array object
    sophisticated (broadcasting) functions
    tools for integrating C/C++ and Fortran code
    useful linear algebra, Fourier transform, and random number capabilities

Testing:

NumPy requires pytest. Tests can then be run after installation with:

python -c 'import numpy; numpy.test()'

"""


contador={}
texto= texto.lower()
texto=texto.split(  )

for palabra in texto:
  
   if (palabra not in contador):
     contador[palabra]= 1
   else:
     contador[palabra]+= 1


for palabra in sorted(contador, key= contador.get,reverse=True)[:1]:
   print('la palabra que mas se repite es: ' ,palabra ,'con ', contador[palabra], 'ocurrencias ')

