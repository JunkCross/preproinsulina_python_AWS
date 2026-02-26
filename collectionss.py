# Para crear una lista se usan []
#Creamos la lista myFruitList y dentro de ella guardamos las siguientes frutas "apple", "banana", "cherry"
myFruitList = ["apple", "banana", "cherry"]

# Imprimimos la lista de frutas completa
print(myFruitList)

#Imprimimos el tipo de dato que es myFruitList
print(type(myFruitList))

# Imprimimos el valor que es esta en la primera posicion de myFruitList (este valor es apple)
print(myFruitList[0])

# Imprimimos el valor que es esta en la primera posicion de myFruitList (este valor es banana)
print(myFruitList[1])

# Imprimimos el valor que es esta en la primera posicion de myFruitList (este valor es cherry)
print(myFruitList[2])

# Vamos a cambiar el valor de la lista en su posicion 2 que antes era cherry y ahora va hacer orange
myFruitList[2] = "orange"

# Imprimimos la lista completa con el cambio 
print(myFruitList)

# Para crear una tupla usamos parentesis ()
# Creamos la tupla myFinalAnswerTuple y dentro de ella guardamos las siguientes frutas "apple", "banana", "pineapple"
myFinalAnswerTuple = ("apple", "banana", "pineapple")

# Imprimimos la tupla completa
print(myFinalAnswerTuple)

# Imprimos el tipo de dato de myFinalAnswerTuple
print(type(myFinalAnswerTuple))

# Imprimimos el primer valor de la tupla que es la primera posicion de myFinalAnswerTuple (este valor es apple)
print(myFinalAnswerTuple[0])

# Imprimimos el primer valor de la tupla que es la primera posicion de myFinalAnswerTuple (este valor es banana)
print(myFinalAnswerTuple[1])

# Imprimimos el primer valor de la tupla que es la primera posicion de myFinalAnswerTuple (este valor es pineapple)
print(myFinalAnswerTuple[2])

# Para crear un diccionario se utilizan llaves y dentro de ellas se va a crear una clave y un valor. la clave y el valor van separados por 2 puntos : y luego de cada clave valor se separa del siguiente usando coma ,
# Creamos el diccionario myFavoriteFruitDictionary con las siguientes claves "Akua", Saanvi", "Paulo" y sus correspondientes valores "apple", "banana", "pineapple"
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

# Imprimirmos el diccionartio completo
print(myFavoriteFruitDictionary)

#Imprimimos el tipo de valor de myFavoriteFruitDictionary
print(type(myFavoriteFruitDictionary))

# Imprimimos el valor de la clave akua
print(myFavoriteFruitDictionary["Akua"])

# Imprimimos el valor de la clave Saanvi
print(myFavoriteFruitDictionary["Saanvi"])

# Imprimimos el valor de la clave Paulo
print(myFavoriteFruitDictionary["Paulo"])