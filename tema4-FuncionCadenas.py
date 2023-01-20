
cadena="Universidad Tecnologica de León"

print(cadena)
print(cadena.lower())
print(cadena.upper())
print(cadena.title())
print(cadena.find("de")) #Encuentra [Palabra] en la cadena, si no encuentra dara -1
print(cadena.count("a")) #Cuenta las letras que le hayas puesto

textoFinal = cadena.replace("a","4") #Remplaza un caracter por otro
print(textoFinal)
cadenaNueva=cadena.split(" ") #hace la separacion de una cadena
print(cadenaNueva)