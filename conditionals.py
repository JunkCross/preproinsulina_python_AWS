# Se va a creear un validador para saber si podemo o no podemos entrar a un fiesta, es importante agregar que para entrar a la fiesta debes ser mayor de edad 
# Se crea la variable edad y en ella se va a aguardar lo que esriba el usuario
edad = input("Escriba su edad: ")

# Convertimos la variable entrada a entero devido a que cuando se escribe por consola el valor que se guarda es el de un texto (str)
edad = int(edad)

# Vamos a comprar si la edad es mayor o igual a 18
if edad >= 18 : 
   # Imprime que lo deje entrar
   print ("Puede entrar")
else :
    # Si no se cumple la condicion de ser mayor de 18 años, imprime no puede entrar
    print("No puede entrar")
    
# Ahora se va a validar si la persona es mayor de edad y tiene mas de 600 pesos 
# Se crea la variable edad y en ella se guarda lo que escriba el usurio
edad = input("Escriba su edad: ")

# Convertimos la variable entrada a entero devido a que cuando se escribe por consola el valor que se guarda es el de un texto (str)
edad = int(edad)

# Se crea la variable edad y en ella se guarda lo que escriba el usurio
dinero = input("Escriba su dinero: ")

# Convertimos la variable entrada a entero devido a que cuando se escribe por consola el valor que se guarda es el de un texto (str)
dinero = int(dinero)


# Vamos a comprar si la edad es mayor o igual a 18
if edad >= 18 : 
   # Verifica si cuenta con el dinero
    if dinero >= 600 :
        # Imprime que lo deja entrar
        print("Puede entrar")
    else: 
        # Como no tiene dinero no puede entrar
        print("No puede entrar")
else:
    # Como no tiene la edad no puede entrar
    print("No puede entrar")
   
#
# Vamos a comprar si la edad es mayor o igual a 18 VERSION 2
if edad >= 18 & dinero >= 600: 
    # Imprime que lo deja entrar
    print("v2 Puede entrar")
else:
    # Como no tiene la edad no puede entrar
    print("v2 No puede entrar")
    
#-------------------------------------------------------------------------------
#Condicional con multiples comparaciones 

# Creamos la variable llamada dinero
dinero = input("Escriba el dinero con el que cuenta: ")

#Convertir la cariable de str a entero
dinero = int(dinero)

# Convirtamos la variable de str a entero}
if(dinero < 100):
    print("Le compro unas galletas")
elif(dinero >= 100 and dinero <= 200):
    print("Le compra unos chocolates")
elif(dinero > 200 and dinero <= 300):
    print("Le compro unas 300 picafresas")
else:
    print ("Le compro un peluche")
    
    
# -----------------------------LABORATORIO--------------------------------------
# Creamos la variable userReply y en ella guardamos lo que escriba el usurio 
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Si lo que hay dentro de la variable es exactamente igual a "yes"
if userReply == "yes":
    # Imprime que nos puede ayudar
    print("We can help you ship that package!")
# De lo contrario dice que no
else:
    print("Please come back when you need to ship a package. Thank you.")
    
    
# -----------------------Ejercicio 3: Trabajo con la instrucción elif-----------
# En la variable userReply vamos a guardar una de estas opciones (stamps, envelope, or copy) que deben ser escritas en la consola. Si no se escribe ninguna de ellas se imprime un mensaje de despedida
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

# Si la variable es exactamente igual a "Stamps" imprime el mensaje con stamps
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
    # Si la variable es exactamente igual a "envelope" imprime el mensaje con envelope
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
    # Si la variable es exactamente igual a "copy" imprime el mensaje con copy
elif userReply == "copy":
    # Se crean las variables copies y se almacena el numero de cipoas que desea crear el usuario
    copies = input("How many copies would you like? (Enter a number) ")
    # Imprime el numero de copias 
    print("Here are {} copies.".format(copies))
else:
    # Se imprime, mensaje de despedida
    print("Thank you, please come again.")