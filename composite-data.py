#La libreria CSV nos perrmite trabajar con archivos separados por comas ,
import csv
# La liberia copy nos permite tomar datos de un archivo y usarlos dentro de un programa 
import copy

# Se crea el diccionario myVehicle
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#Se crea un ciclo for para imprimir  cada una de las claves: valor que hay dentro del diccionario
for key, value in myVehicle.items():
    # Se imprime la clave : valor
    print("{} : {}".format(key,value))
    
# Se crea la lista myInventoryList 
myInventoryList = []

# Se abre el archivo car_fleet.csv   y se guarda dentro de la variable csvfile
with open('car_fleet.csv') as csvFile:
    # Se lee el archivo csvReader donde su delimitador son 
    csvReader = csv.reader(csvFile, delimiter=',')  
    # Se crea la variable lineCount y se le asigna el valor de 0
    lineCount = 0  
    # Se lee cada una  de las lineas, filas o renglones del archivo csvReader
    for row in csvReader:
        # Si el valor de las lineas es 0
        if lineCount == 0:
            # Se imprime el nombre de la columna
            print(f'Column names are: {", ".join(row)}')  
            # Se aumenta en 1 el valor de lineCount 
            lineCount += 1  
        # Si el valor de la linea noe es 0
        else:  
            # Imprime en cada una de las claves la posicion que fue separada por comas, anteriomente
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            # Se copia el valor de las variables dentro del diccionario myVehicule
            currentVehicle = copy.deepcopy(myVehicle)  
            # Se copia el valor de las variables dentro del diccionario myVehicle
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]
            # Se agregan a las lsita un vehiculo
            myInventoryList.append(currentVehicle)  
            # Se aumenta en 1 el valor de lineCount
            lineCount += 1  
    # Se imprime el total de lineas/renglones/filas 
    print(f'Processed {lineCount} lines.')
    
    # Se crea un for para imprimir cada vehiculo de la lista
    for myCarProperties in myInventoryList:
        # Se imprimen los datos de cada vehiculo 
        for key, value in myCarProperties.items():
            # Se imprime la llave : valor
            print("{} : {}".format(key,value))
            # Se imprime un separador
            print("-----")