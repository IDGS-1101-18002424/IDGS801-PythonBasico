

texto1="¡¡Hola"
texto2="Mundo!!"
textoFinal=texto1+" "+texto2
print(textoFinal)

print("El saludo es: %s %s " % (texto1,texto2))


cadena= "Saludor dos: {} {}".format(texto1,texto2)
# [{0} {1}] = Hola mundo
# [{1} {0}] = mundo Hola
print(cadena)
