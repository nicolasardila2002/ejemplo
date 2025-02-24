def puede_entrar(nombre, edad):
    if edad < 18:
        return nombre + "No puede entrar"
    else:
        return nombre +" Puede entrar"
    
    print ("Fin de la aplicacion")

print(puede_entrar("NICOLAS", 20))
print
 



