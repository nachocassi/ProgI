def leerArchivo(directorio):
    """Lee el archivo una vez y obtiene todas sus palabras en una cadena."""
    try:
        arch=open(directorio,"rt")
        lineasarchivo=arch.read()
        return lineasarchivo
    except IOError:
        print("Error al intentar abrir el archivo. ")
    finally:
        try:
            arch.close()
        except:
            pass
    
def obtenerLineas(lineasarchivo):
    """Recibe todas las palabras del archivo en una cadena, obtiene cada linea en una lista, borra el salto de línea y las convierte a minúscula finalmente devuelve la lista."""
    lineas=lineasarchivo.split("\n")
    for i in range(len(lineas)):
        lineas[i]=lineas[i].replace("\n","")
        lineas[i]=lineas[i].lower()
    return lineas

def obtenerDatosLineas(lineas):
    """Para cada linea: quita los caracteres no alfabeticos, cuenta los caracteres mediante funcion recursiva y si son más de 3: verifica si existen en dicc
    para contar sus repeticiones. """
    datos=dict()
    for i in range(len(lineas)):
        linealimpia="".join([item for item in lineas[i] if item.isalpha()]) #Obtiene la cadena sin puntuacion
        lineas[i]=linealimpia                                           #La reemplaza en la lista
        caracteres=contarCaracteresRecursiva(lineas[i])                 #Cuenta los caract
        if caracteres>3:                                                #Si la palabra tiene más de 3 caracteres
            if lineas[i] not in datos:
                datos[lineas[i]]=1
            else:
                datos[lineas[i]]+=1
    return datos
            
def mostrarDatosLineas(datos):
    """Ordena alfabeticamente el diccionario con los datos y para cada palabra: muestra la misma y sus repeticiones."""
    listadatos=list(datos.items())
    listadatos.sort(key=lambda item:item[0])
    for i in range(len(listadatos)):
        print("Palabra: "+listadatos[i][0]+" Repeticiones: "+str(listadatos[i][1])+".")

def contarCaracteresRecursiva(cadena,caracteres=0):
    """Cuenta los caracteres de una palabra mediante un contador(caracteres) que se incrementa en cada ejecución de la función recursiva.
    Caso base: caracteres es igual al largo de la cadena"""
    if caracteres==len(cadena):
        return caracteres
    else:
        caracteres+=1
        return contarCaracteresRecursiva(cadena,caracteres)
    
def crearMatriz(N=3):
    """Crea y devuelve una matriz con las dimensiones recibidas por parámetro: N*N"""
    matriz=[]
    for f in range(N):
        matriz.append([])
        for c in range(N):
            matriz[f].append(0)
    return matriz

def zigzagMatriz(matriz):
    """Recibe una matriz por parámetro y reemplaza sus valores"""
    N=len(matriz)
    total=N*N
    contador=1
    f=0
    c=0
    
    #Primer elem
    matriz[f][c]=contador
    contador+=1
    while(contador<=total):
        try:
            if contador%2==0:
                #Si es par baja
                matriz[f+1][c]=contador
                contador+=1
                f+=1
            else:
                #Si no es par va a la derecha
                try:
                    matriz[f-1][c+1]=contador
                    contador+=1
                    f-=1
                    c+=1
                except IndexError:
                    #print("Se sale de la matriz por la derecha. ")
                    pass
                    try:
                        matriz[f+1][0]=contador
                        contador+=1
                        f+=1
                        c=0
                    except IndexError:
                        #print("Se sale de la matriz al saltar de línea.")
                        pass
        except IndexError:
            #print("Se sale de la matriz al bajar. ")
            pass
            #Va a la derecha
            while contador<=total:
                matriz[f][c+1]=contador
                contador+=1
                c+=1
        
def mostrarMatriz(matriz):
    """Recibe una matriz por parámetro y la muestra fila por fila."""
    for fila in range(len(matriz)):
        print(matriz[fila])
        
def sumaDeFilas(matriz):
    sumaFilas=[sum(fila) for fila in matriz]
    print(sumaFilas)
    return sumaFilas

def mostrarLista(lista):
    print("")
    print("Las sumas de los elementos de cada fila de la matriz son:")
    print("")
    for i in range(len(lista)):
        print("Fila "+str(i)+" :"+str(lista[i])+".")

def quitarRepetidosLista(lista,nuevalista=[],contador=0):
    if contador==len(lista)-1:
        return nuevalista
    else:
        item=lista[contador]
        if item not in nuevalista:
            nuevalista.append(item)
        contador+=1
        return quitarRepetidosLista(lista,nuevalista,contador)

def __main__():
    #Ejercicio 1
    print("")
    print("Ejercicio 1: ")
    print("")
    
    lineasarchivo=leerArchivo(r"C:\Users\Nacho\Desktop\Python\Práctica\ProgI\ProgI\frases.txt")
    lineas=obtenerLineas(lineasarchivo)
    datos=obtenerDatosLineas(lineas)
    mostrarDatosLineas(datos)
    
    #Ejercicio 2
    print("")
    print("Ejercicio 2:")
    print("")
    
    matriz=crearMatriz(4)
    zigzagMatriz(matriz)
    mostrarMatriz(matriz)
    listacomprension=sumaDeFilas(matriz)
    mostrarLista(listacomprension)
    
    #Ejercicio 3
    print("")
    print("Ejercicio 3:")
    print("")
    
    lista=[1,2,3,3,4,5,5,6]
    print("Lista original: "+str(lista))
    nuevalista=quitarRepetidosLista(lista)
    print("Lista nueva sin repetidos: "+str(nuevalista))
    
if __name__=="__main__":
    __main__()