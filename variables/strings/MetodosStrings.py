Animal = "   perRIto alegre   "
#el método upper convierte todo a letras mayúsculas
print(Animal.upper())
#el método upper convierte todo a letras minúsculas
print(Animal.lower())
#el método capitalize convierte en mayúscula la primera letra y el resto en minúscula
print(Animal.capitalize())
#el método title hace lo mismo que capitalize pero a cada palabra
print(Animal.title())
#el método strip remueve todos los espacios a la izquierda y derecha
print(Animal.strip())
#los métodos pueden usarse uno sobre otro (encadenarse)
#normalmente antes de un capitalize se usa un strip
print(Animal.strip().capitalize())
#existe lstrip que quita los espacios de la izquierda
#existe rstrip que quita los espacios de la derecha
print(Animal.lstrip())
print(Animal.rstrip())
#con el método find podemos encontrar cadenas dentro de un string
print(Animal.find("RI")) #devuelve el indice de la cadena
print(Animal.find("z")) #si no lo encuentra devuelve -1
#el método replace reemplaza los valores indicados por otros
print(Animal.replace("RIt", "n")) #no cambia nada si no encuentra el argumento
# detecta si se encuentra la cadena de caracteres pero no da el indice
print("RIt" in Animal)
#se puede usar el operador not para identificar si no se encuentra en la cadena
print("RIt" not in Animal)
