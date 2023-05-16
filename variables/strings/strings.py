""" Strings """

NombreVariable = "String"
DescripcionVariable = """
esta variable contiene
el valor de String
"""

#la coma ',' permite imprimir distintas variables a la vez
print(NombreVariable, DescripcionVariable)

#la funcion len permite saber cuantas letras componen el string
print(len(NombreVariable))

#con los corchetes nos ubicamos en la posición deseada del string
print(NombreVariable[0])

#podemos imprimir secciones usando ':'
# a la izquierda queda el inicio y a la derecha cuantos caracteres se usan
print(NombreVariable[0:6])

#si le damos una expresión sin el valor de longitud total
#python interpreta que debe llegar al ultimo valor del string
#print(NombreVariable)[4: ]
#también funciona a la inversa
#print(NombreVariable)[ :4]
