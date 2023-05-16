
Nombre =  "Josué"
Apellido = "Grádiz"

#un ejemplo de impresión sin formato
#NombreCompleto = Nombre + " " + Apellido

#ejemplo de impresión con formato
NombreCompleto = f"{Nombre} {Apellido}"
print(NombreCompleto)

# las llaves permiten escribir cualquier expresión dentro
NombreCompleto = f"{Nombre[0]}{2 + 6}"
print(NombreCompleto)
