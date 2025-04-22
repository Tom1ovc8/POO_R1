# Ejercicio 5

def mismos_caracteres(lista):
    resultado = []
    for palabra in lista:
        for otra_palabra in lista:
            if palabra != otra_palabra and sorted(palabra) == sorted(otra_palabra):
                resultado.append(palabra)
                break
    return resultado
if __name__ == "__main__":
    lista = input("Introduce una lista de palabras separadas por espacios: ").split()
    print(mismos_caracteres(lista))

"""
1. Se define la función `mismos_caracteres` que toma una lista de palabras como objeto a trabajar.
2. Se define el resultado como una lista vacía.
3. Se pide que se introduzca una lista de palabras separadas por espacios.
4. Se separan las palabras y se almacenan en la variable `lista`.
5. Se itera sobre cada palabra en la lista.
6. Se compara cada palabra con las demás palabras de la lista.
7. Si las palabras son diferentes y tienen los mismos caracteres (ordenados), se añade la palabra a la lista de resultados.
8. Se imprime la lista de palabras que tienen los mismos caracteres.
"""