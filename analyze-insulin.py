# Se usa la libreria re para trabajar con expresiones regulares
import re

# Abrimos el archivo de texto 
with open("preproinsulin-seq.txt", "r") as f:
    
    # Leemos todo el contenido del archivo
    raw_data = f.read()
    
# Eliminar el ORIGIN
clean_data = re.sub(r"\bORIGIN\b", "", raw_data, flags=re.IGNORECASE)

# Eliminar el terminado de registro
clean_data = clean_data.replace("//", "")

# Eliminar cualquier cosa que no sea letra.
clean_data = re.sub(r"[^A-Za-z]", "", clean_data)

# Convertimos todo a mayusculas
clean_data = clean_data.lower()

# Abrir nuevamente el archivo de preproinsulin.seq.txt
with open("preproinsulin-seq.txt", "w") as f:
    
    # Limpiamos el archivo
    f.write(clean_data)

# Calculamos la longitud de preproinsulin    
print("Longitud de Prepoinsulin = ", len(clean_data))

# Si la secuencia no tiene 110 caracteres, nos salimos del programa
if len(clean_data) != 110:
    print("error la secuencia no tiene 110 caracteres")
    exit()
    
# Extraemos los primeros 24 caracteres 
lsinsulin = clean_data[0:24]

# Extraemos del caracter 25 al caracter 54
binsulin = clean_data[24:54]

# Extraemos del caracter 55 al 89
cinsulin = clean_data[54:89]

# Extraemos del caracter 90 al 110
ainsulin = clean_data[89:110]

# Creamos los diferentes archivos 
with open("lsinsulin-seq-clean.txt", "w") as f:
    
    f.write(lsinsulin)
    
# Creamos los diferentes archivos 
with open("binsulin-seq-clean.txt", "w") as f:
    
    f.write(binsulin)

# Creamos los diferentes archivos 
with open("cinsulin-seq-clean.txt", "w") as f:
    
    f.write(cinsulin)

# Creamos los diferentes archivos 
with open("ainsulin-seq-clean.txt", "w") as f:
    
    f.write(ainsulin)

# Verificamos el tamaño de caracteres
print("lsinsulin = ", len(lsinsulin))

# Verificamos el tamaño de caracteres
print("binsulin = ", len(binsulin))

# Verificamos el tamaño de caracteres
print("cinsulin = ", len(cinsulin))

# Verificamos el tamaño de caracteres
print("ainsulin = ", len(ainsulin))

insulin = binsulin + ainsulin

#Total de insulina
print("Insulina procesada: ", len(insulin))

#Secuencia de la insulina 
print("Secuencia de la insulina =  ", insulin)
