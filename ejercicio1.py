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

lineas= texto.splitlines()

for linea in lineas:
 if(('http' in linea)or ('https' in linea)):
  print(linea)
